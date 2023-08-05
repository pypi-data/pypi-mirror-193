#!/usr/bin/env python3

import click
import sys
import os
import tomllib
# telnet is the only protocol supported by the squeezebox server
from telnetlib import Telnet    # nosec
from tabulate import tabulate
import curses
import squeezebox_cli.player
import squeezebox_cli.database
import squeezebox_cli.display

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
    if not port:
        port = 9090
    global sb_server
    sb_server = Telnet(host, port)
    if not sb_server.sock:
        click.echo(f'ERROR: could not connect to {host}:{port}')
        sys.exit(1)


@ui_main.command(help='list the currently connected players')
def players():
    # TODO: options for columns to show?
    ps = squeezebox_cli.player.list_all(sb_server)
    click.echo(tabulate(
        [(p['playerindex'], p['name'], 'yes' if p['isplaying'] else 'no')
            for p in ps],
        headers=['index', 'name', 'is playing?']))


@ui_main.command(help='search the music database')
@click.argument('term')
def search(term):
    reply = squeezebox_cli.database.search(sb_server, term)
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


@ui_main.group(help='view and control a player by name or index')
@click.argument('player-name')
def player(player_name):
    global player_id
    player_id = squeezebox_cli.player.id_from_index_or_name(
            sb_server, player_name)
    if not player_id:
        click.echo(f'ERROR: no such player: {player_name}')
        sys.exit(1)


@player.command(help='stop the specified player')
def stop():
    squeezebox_cli.player.stop(sb_server, player_id)


@player.command(help='query shuffle state on the specified player')
def shuffled():
    click.echo(
            squeezebox_cli.player.playlist_query_shuffle(sb_server, player_id))


SHUFFLE_BY_STRING = {
        'none': squeezebox_cli.player.Shuffle.NONE,
        'song': squeezebox_cli.player.Shuffle.SONG,
        'album': squeezebox_cli.player.Shuffle.ALBUM,
        }


@player.command(help='set the shuffle state on the specified player')
@click.argument('shuffle-type',
                type=click.Choice(['none', 'song', 'album']),
                required=False)
def shuffle(shuffle_type):
    try:
        squeezebox_cli.player.playlist_set_shuffle(
                sb_server, player_id, SHUFFLE_BY_STRING[shuffle_type])
    except KeyError:
        squeezebox_cli.player.playlist_toggle_shuffle(sb_server, player_id)


@player.command(help='query the repeat state of the specified player')
def repeating():
    click.echo(
            squeezebox_cli.player.playlist_query_repeat(sb_server, player_id))


REPEAT_BY_STRING = {
        'none': squeezebox_cli.player.Repeat.NONE,
        'song': squeezebox_cli.player.Repeat.SONG,
        'all': squeezebox_cli.player.Repeat.ALL,
        }


@player.command(help='set the repeat state on the specified player')
@click.argument('repeat-type',
                type=click.Choice(['none', 'song', 'all']),
                required=False)
def repeat(repeat_type):
    try:
        squeezebox_cli.player.playlist_set_repeat(
                sb_server, player_id, REPEAT_BY_STRING[repeat_type])
    except KeyError:
        squeezebox_cli.player.playlist_toggle_repeat(sb_server, player_id)


@player.group(help='play a track or album')
def play():
    pass


@play.command(name='track', help='play the specified track')
@click.argument('track_id', type=int)
def play_track(track_id):
    squeezebox_cli.player.play(sb_server, player_id, track_id=track_id)


@play.command(name='album', help='play the specified album')
@click.argument('album_id', type=int)
def play_album(album_id):
    squeezebox_cli.player.play(sb_server, player_id, album_id=album_id)


@player.command(help='pause/unpause the specified player')
def pause():
    squeezebox_cli.player.pause(sb_server, player_id)


@player.command(help='status of the specified player')
@click.option(
        '--long/--short', default=False,
        help='verbose output, playlist etc.')
@click.option(
        '--listen/--return', default=False,
        help='listen for and display notificataions')
@click.option('--max-tracks', type=int)
def status(long, listen, max_tracks):
    status = squeezebox_cli.player.status(sb_server, player_id)
    sys.stdout.write(f'\x1b]2;Squeezebox: {status["name"]}\x07')

    def show():
        click.echo(squeezebox_cli.display.format_status(status))
        if long:
            click.echo(squeezebox_cli.display.format_playlist(
                [squeezebox_cli.database.songinfo(sb_server, id)
                    if id > 0
                    else dict(title=t, album='[Radio]', artist=None)
                 for id, t in status['playlist']],
                status['playlist_cur_index'],
                max_tracks))
    show()
    if listen:
        for n in squeezebox_cli.player.listen(
                Telnet(sb_server.host, sb_server.port), status['playerid']):
            # click.echo(n)
            for handler in squeezebox_cli.player.notification_handlers:
                if handler(status, n, sb_server):
                    show()
                    break


@player.command(help='monitor the specified player')
def monitor():

    def do_tui(screen):
        curses.curs_set(0)
        squeezebox_cli.display.show(screen, sb_server, player_id)
        for n in squeezebox_cli.player.listen(
                Telnet(sb_server.host, sb_server.port), player_id):
            squeezebox_cli.display.show(screen, sb_server, player_id)

    curses.wrapper(do_tui)


@player.command(help='play the next track in the current playlist')
def next():
    squeezebox_cli.player.next(sb_server, player_id)


@player.command(help='play the previous track in the current playlist')
def previous():
    squeezebox_cli.player.previous(sb_server, player_id)


@player.group(help=('add a track or album to the end of the current playlist'))
def add():
    pass


@add.command(name='track',
             help='add a track to the end of the current playlist')
@click.argument('track_id')
def add_track(track_id):
    squeezebox_cli.player.playlist_add(sb_server, player_id, track_id=track_id)


@add.command(name='album',
             help='add an album to the end of the current playlist')
@click.argument('album_id')
def add_album(album_id):
    squeezebox_cli.player.playlist_add(sb_server, player_id, album_id=album_id)


@player.group(help='insert a track or album after the current track')
def insert():
    pass


@insert.command(name='track', help='insert a track after the current one')
@click.argument('track_id')
def insert_track(track_id):
    squeezebox_cli.player.playlist_insert(
            sb_server, player_id, track_id=track_id)


@insert.command(name='album', help='insert an album after the current track')
@click.argument('album_id')
def insert_album(album_id):
    squeezebox_cli.player.playlist_insert(
            sb_server, player_id, album_id=album_id)


@player.command(help='set or change the player volume N, +N or -- -N')
@click.argument('vol', type=str)
def volume(vol):
    squeezebox_cli.player.set_volume(sb_server, player_id, vol)


@player.command(help='remove a track from the current playlist by index')
@click.argument('index', type=int)
def remove(index):
    squeezebox_cli.player.playlist_remove(sb_server, player_id, index - 1)
