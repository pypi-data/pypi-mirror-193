from .commands import list_all, stop, play, status, id_from_index_or_name, \
        next, previous, pause, count, id, name, ip, signal_strength, \
        connected, synced_to, sync_to, sync_groups, get_volume, set_volume, \
        change_volume, mute, unmute, toggle_mute, get_mute, players, \
        listen, playlist_add, playlist_remove, playlist_insert, Shuffle, \
        playlist_query_shuffle, playlist_set_shuffle, Repeat, \
        playlist_query_repeat, playlist_set_repeat, playlist_toggle_repeat, \
        playlist_toggle_shuffle
from .notifications import pause_handler, volume_handler, newsong_handler, \
        playlistcontrol_handler, play_handler

__all__ = (
    'list_all',
    'stop',
    'play',
    'status',
    'id_from_index_or_name',
    'next',
    'previous',
    'pause',
    'count',
    'id',
    'name',
    'ip',
    'signal_strength',
    'connected',
    'synced_to',
    'sync_to',
    'sync_groups',
    'get_volume',
    'set_volume',
    'change_volume',
    'mute',
    'unmute',
    'toggle_mute',
    'get_mute',
    'players',
    'listen',
    'playlist_add',
    'playlist_remove',
    'playlist_insert',
    'Shuffle',
    'playlist_query_shuffle',
    'playlist_set_shuffle',
    'playlist_toggle_shuffle',
    'Repeat',
    'playlist_query_repeat',
    'playlist_set_repeat',
    'playlist_toggle_repeat',
    )

notification_handlers = [
        pause_handler, volume_handler, newsong_handler,
        playlistcontrol_handler, play_handler]
