import click
import sys
import os
import tomllib
# telnet is the only protocol supported by the squeezebox server
from telnetlib import Telnet    # nosec
import socket
from tabulate import tabulate
import curses


from squeezebox_cli.player import playlist_remove, Shuffle, Repeat, \
        id_from_index_or_name, list_all, stop, playlist_query_shuffle, \
        playlist_set_shuffle, playlist_toggle_shuffle, playlist_query_repeat, \
        playlist_toggle_repeat, playlist_set_repeat, play, pause, next, \
        previous, playlist_add, playlist_insert, set_volume, status, listen, \
        notification_handlers
from squeezebox_cli.database import search, songinfo
from squeezebox_cli.display import format_status, show, format_playlist

sb_server = None
player_id = None


@click.group()
@click.option(
        '--host', type=str,
        help='hostname for squeezebox server')
@click.option(
        '--port', type=int,
        help='port for squeezebox server (default 9090)')
def ui_main(host, port):
    try:
        with open(os.path.expanduser('~/.squeezebox-cli.toml'), 'rb') as f:
            cfg = tomllib.load(f)
            if not host:
                try:
                    host = cfg['server']['host']
                except KeyError:
                    pass
            if not port:
                try:
                    port = cfg['server']['port']
                except KeyError:
                    pass
    except FileNotFoundError:
        pass
    if not host:
        click.echo('ERROR: you must specify a host.'
                   ' Either in configuration (~/.squeezebox-cli.toml)'
                   ' or by argument (--host=).')
        sys.exit(1)
    if not port:
        port = 9090
    global sb_server
    try:
        sb_server = Telnet(host, port)
    except (ConnectionRefusedError, socket.gaierror):
        click.echo(f'ERROR: could not connect to {host}:{port}')
        sys.exit(1)


@ui_main.command(name='players', help='list the currently connected players')
def ui_players():
    # TODO: options for columns to show?
    ps = list_all(sb_server)
    click.echo(tabulate(
        [(p['playerindex'], p['name'], 'yes' if p['isplaying'] else 'no')
            for p in ps],
        headers=['index', 'name', 'is playing?']))


@ui_main.command(name='search', help='search the music database')
@click.argument('term')
def ui_search(term):
    reply = search(sb_server, term)
    artists = reply['artists']
    click.echo(tabulate(
        [(artist, id) for id, artist in artists.items()],
        headers=['artist', 'id']))
    click.echo()
    albums = reply['albums']
    click.echo(tabulate(
        [(album, id) for id, album in albums.items()],
        headers=['album', 'id']))
    click.echo()
    tracks = reply['tracks']
    click.echo(tabulate(
        [(track, id) for id, track in tracks.items()],
        headers=['track', 'id']))


@ui_main.group(name='player',
               help='view and control a player by name or index')
@click.argument('player-name')
def player(player_name):
    global player_id
    player_id = id_from_index_or_name(
            sb_server, player_name)
    if not player_id:
        click.echo(f'ERROR: no such player: {player_name}')
        sys.exit(1)


@player.command(name='stop', help='stop the specified player')
def ui_stop():
    print('STOPPING>>>')
    stop(sb_server, player_id)
    print('>>>STOPPED')


SHUFFLE_BY_STRING = {
        'none': Shuffle.NONE,
        'song': Shuffle.SONG,
        'album': Shuffle.ALBUM,
        }

SHUFFLE_TO_STRING = {v: k for k, v in SHUFFLE_BY_STRING.items()}


@player.command(help='query shuffle state on the specified player')
def shuffled():
    click.echo(
            SHUFFLE_TO_STRING[playlist_query_shuffle(sb_server, player_id)])


@player.command(help='set the shuffle state on the specified player')
@click.argument('shuffle-type',
                type=click.Choice(['none', 'song', 'album']),
                required=False)
def shuffle(shuffle_type):
    try:
        playlist_set_shuffle(
                sb_server, player_id, SHUFFLE_BY_STRING[shuffle_type])
    except KeyError:
        playlist_toggle_shuffle(sb_server, player_id)


@player.command(help='query the repeat state of the specified player')
def repeating():
    click.echo(
            REPEAT_TO_STRING[playlist_query_repeat(sb_server, player_id)])


REPEAT_BY_STRING = {
        'none': Repeat.NONE,
        'song': Repeat.SONG,
        'all': Repeat.ALL,
        }

REPEAT_TO_STRING = {v: k for k, v in REPEAT_BY_STRING.items()}


@player.command(help='set the repeat state on the specified player')
@click.argument('repeat-type',
                type=click.Choice(['none', 'song', 'all']),
                required=False)
def repeat(repeat_type):
    try:
        playlist_set_repeat(
                sb_server, player_id, REPEAT_BY_STRING[repeat_type])
    except KeyError:
        playlist_toggle_repeat(sb_server, player_id)


@player.group(name='play', help='play a track or album')
def ui_play():
    pass


@ui_play.command(name='track', help='play the specified track')
@click.argument('track_id', type=int)
def play_track(track_id):
    play(sb_server, player_id, track_id=track_id)


@ui_play.command(name='album', help='play the specified album')
@click.argument('album_id', type=int)
def play_album(album_id):
    play(sb_server, player_id, album_id=album_id)


@player.command(name='pause', help='pause/unpause the specified player')
def ui_pause():
    pause(sb_server, player_id)


@player.command(name='status', help='status of the specified player')
@click.option(
        '--long/--short', default=False,
        help='verbose output, playlist etc.')
@click.option(
        '--listen/--return', default=False,
        help='listen for and display notificataions')
@click.option('--max-tracks', type=int)
def ui_status(long, listen, max_tracks):
    s = status(sb_server, player_id)

    def show_status():
        click.echo(format_status(s))
        if long:
            click.echo(format_playlist(
                [songinfo(sb_server, id)
                    if id > 0
                    else dict(title=t, album='[Radio]', artist=None)
                 for id, t in s['playlist']],
                s['playlist_cur_index'],
                max_tracks))
    show_status()
    if listen:
        for n in listen(
                Telnet(sb_server.host, sb_server.port), s['playerid']):
            for handler in notification_handlers:
                if handler(s, n, sb_server):
                    show_status()
                    break


@player.command(help='monitor the specified player')
def monitor():

    def do_tui(screen):
        curses.curs_set(0)
        show(screen, sb_server, player_id)
        for n in listen(
                Telnet(sb_server.host, sb_server.port), player_id):
            show(screen, sb_server, player_id)

    curses.wrapper(do_tui)


@player.command(name='next',
                help='play the next track in the current playlist')
def ui_next():
    next(sb_server, player_id)


@player.command(name='previous',
                help='play the previous track in the current playlist')
def ui_previous():
    previous(sb_server, player_id)


@player.group(help=('add a track or album to the end of the current playlist'))
def add():
    pass


@add.command(name='track',
             help='add a track to the end of the current playlist')
@click.argument('track_id')
def add_track(track_id):
    playlist_add(sb_server, player_id, track_id=track_id)


@add.command(name='album',
             help='add an album to the end of the current playlist')
@click.argument('album_id')
def add_album(album_id):
    playlist_add(sb_server, player_id, album_id=album_id)


@player.group(help='insert a track or album after the current track')
def insert():
    pass


@insert.command(name='track', help='insert a track after the current one')
@click.argument('track_id')
def insert_track(track_id):
    playlist_insert(sb_server, player_id, track_id=track_id)


@insert.command(name='album', help='insert an album after the current track')
@click.argument('album_id')
def insert_album(album_id):
    playlist_insert(sb_server, player_id, album_id=album_id)


@player.command(help='set or change the player volume N, +N or -- -N')
@click.argument('vol', type=str)
def volume(vol):
    set_volume(sb_server, player_id, vol)


@player.command(help='remove a track from the current playlist by index')
@click.argument('index', type=int)
def remove(index):
    playlist_remove(sb_server, player_id, index - 1)
