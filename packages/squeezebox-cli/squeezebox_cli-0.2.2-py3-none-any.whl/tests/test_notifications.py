from squeezebox_cli.player import pause_handler, volume_handler, \
    newsong_handler, playlistcontrol_handler, play_handler


def test_play_handler_no_match(mocker):
    status = dict()
    assert not play_handler(status,
                            [
                                '12:34:56:78:90:12',
                                'prefset',
                                'server',
                                'volume',
                                '52',
                                ],
                            mocker.MagicMock())
    assert dict() == status


def test_play_handler_play(mocker):
    status = dict()
    assert play_handler(status,
                        ['b1:e0:21:43:36:3b', 'play', ''],
                        mocker.MagicMock())
    assert 'play' == status['mode']


def test_pause_handler_no_match(mocker):
    status = dict()
    assert not pause_handler(status,
                             [
                                 '12:34:56:78:90:12',
                                 'prefset',
                                 'server',
                                 'volume',
                                 '52',
                                 ],
                             mocker.MagicMock())
    assert dict() == status


def test_pause_handler_pause(mocker):
    status = dict()
    assert pause_handler(
            status,
            ['12:34:56:78:90:12', 'playlist', 'pause', '1'],
            mocker.MagicMock())
    assert 'pause' == status['mode']


def test_pause_handler_play(mocker):
    status = dict()
    assert pause_handler(
            status,
            ['12:34:56:78:90:12', 'playlist', 'pause', '0'],
            mocker.MagicMock())
    assert 'play' == status['mode']


def test_volume_handler_no_match(mocker):
    status = dict()
    assert not volume_handler(
            status,
            ['12:34:56:78:90:12', 'playlist', 'pause', '1'],
            mocker.MagicMock())
    assert dict() == status


def test_volume_handler_volume_set(mocker):
    status = dict()
    assert volume_handler(
            status,
            ['12:34:56:78:90:12', 'prefset', 'server', 'volume', '52'],
            mocker.MagicMock())
    assert 52 == status['volume']


def test_new_song_handler_no_match(mocker):
    player_status = mocker.patch('squeezebox_cli.player.notifications.status')
    status = dict()
    assert not newsong_handler(
            status,
            ['12:34:56:78:90:12', 'playlist', 'pause', '1'],
            mocker.MagicMock())
    assert dict() == status
    player_status.assert_not_called()


def test_new_song_handler_newsong(mocker):
    player_status = mocker.patch('squeezebox_cli.player.notifications.status')
    player_status.return_value = dict(
            playlist_cur_index=2,
            playlist=[
                (1234, "Blah Blah"),
                (1234, "Blah Blah"),
                (5678, "When We Were Young"),
                (1234, "Blah Blah"),
                ])
    ss = mocker.MagicMock()
    status = dict()
    assert newsong_handler(
            status,
            [
                'b1:e0:21:43:36:3b',
                'playlist',
                'newsong',
                'When We Were Young',
                '2',
                ],
            ss)
    player_status.assert_called_once_with(ss, 'b1:e0:21:43:36:3b')
    assert player_status.return_value == status


def test_new_song_handler_no_index(mocker):
    player_status = mocker.patch('squeezebox_cli.player.notifications.status')
    player_status.return_value = dict(
            playlist_cur_index=0,
            playlist=[(-1, 'Royal Blood - Come On Over')],
            )
    ss = mocker.MagicMock()
    status = dict()
    assert newsong_handler(
            status,
            [
                'b1:e0:21:43:36:3b',
                'playlist',
                'newsong',
                'Royal Blood - Come On Over',
                ],
            ss)
    assert 0 == status['playlist_cur_index']
    assert [(-1, 'Royal Blood - Come On Over')] == status['playlist']


def test_playlist_control_handler_no_match(mocker):
    status = dict()
    assert not playlistcontrol_handler(
            status,
            ['12:34:56:78:90:12', 'playlist', 'pause', '1'],
            mocker.MagicMock())
    assert dict() == status


def test_playlist_control_handler_remove_current(mocker):
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home'),
                ],
            'playlist_cur_index': 5,
            }
    assert playlistcontrol_handler(
            status,
            [
                'b1:e0:21:43:36:3b',
                'playlist',
                'delete',
                '5',
                'useContextMenu:1',
                ],
            mocker.MagicMock())
    assert [
            (48584, 'Everything'),
            (48586, 'If You Go'),
            (48587, 'When We Were Young'),
            (48588, 'Anywhere'),
            (48589, 'Somebody’s Love'),
            (48591, 'Beautiful Birds'),
            (48592, 'The Long Road'),
            (48593, 'Fool’s Gold'),
            (48585, 'Home'),
            ] == status['playlist']
    assert 5 == status['playlist_cur_index']


def test_playlist_control_handler_remove_before_current(mocker):
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home'),
                ],
            'playlist_cur_index': 7,
            }
    assert playlistcontrol_handler(
            status,
            [
                'b1:e0:21:43:36:3b',
                'playlist',
                'delete',
                '5',
                'useContextMenu:1',
                ],
            mocker.MagicMock())
    assert [
            (48584, 'Everything'),
            (48586, 'If You Go'),
            (48587, 'When We Were Young'),
            (48588, 'Anywhere'),
            (48589, 'Somebody’s Love'),
            (48591, 'Beautiful Birds'),
            (48592, 'The Long Road'),
            (48593, 'Fool’s Gold'),
            (48585, 'Home'),
            ] == status['playlist']
    assert 6 == status['playlist_cur_index']


def test_playlist_control_handler_remove_after_current(mocker):
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home')
                ],
            'playlist_cur_index': 2,
            }
    assert playlistcontrol_handler(
                status,
                [
                    'b1:e0:21:43:36:3b',
                    'playlist',
                    'delete',
                    '5',
                    'useContextMenu:1',
                    ],
                mocker.MagicMock())
    assert [
            (48584, 'Everything'),
            (48586, 'If You Go'),
            (48587, 'When We Were Young'),
            (48588, 'Anywhere'),
            (48589, 'Somebody’s Love'),
            (48591, 'Beautiful Birds'),
            (48592, 'The Long Road'),
            (48593, 'Fool’s Gold'),
            (48585, 'Home'),
            ] == status['playlist']
    assert 2 == status['playlist_cur_index']


def test_playlist_control_handler_add_track_to_end(mocker):
    tn = mocker.MagicMock()
    tracks = mocker.patch('squeezebox_cli.player.notifications.tracks')
    tracks.return_value = [{
        'id': 48537,
        'title': 'Hell Or High Water (live from Santa Monica Beach, CA)',
        'genre': 'Folk', 'artist': 'Passenger', 'album': 'Runaway (Live)',
        'duration': 190.16,
        }]
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home')
                ],
            }
    assert playlistcontrol_handler(
                status,
                ['b1:e0:21:43:36:3b', 'playlistcontrol', 'cmd:add',
                    'useContextMenu:1', 'track_id:48537', 'count:1'],
                tn)
    tracks.assert_called_once_with(tn, track_id=48537)
    assert [
            (48584, 'Everything'),
            (48586, 'If You Go'),
            (48587, 'When We Were Young'),
            (48588, 'Anywhere'),
            (48589, 'Somebody’s Love'),
            (48590, 'Young as the Morning Old as the Sea'),
            (48591, 'Beautiful Birds'),
            (48592, 'The Long Road'),
            (48593, 'Fool’s Gold'),
            (48585, 'Home'),
            (48537,
             'Hell Or High Water (live from Santa Monica Beach, CA)'),
            ] == status['playlist']


def test_playlist_control_handler_add_album_to_end(mocker):
    tn = mocker.MagicMock()
    tracks = mocker.patch('squeezebox_cli.player.notifications.tracks')
    tracks.return_value = [
            {'id': 52807, 'title': 'the 1', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 210.24, 'tracknum': 1},
            {'id': 52816, 'title': 'cardigan', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 239.56, 'tracknum': 2},
            {'id': 52817, 'title': 'the last great american dynasty',
                'genre': 'Pop', 'artist': 'taylor swift',
                'album': 'folklore', 'duration': 231.0, 'tracknum': 3},
            {'id': 52818, 'title': 'exile', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 285.64, 'tracknum': 4},
            {'id': 52819, 'title': 'my tears ricochet', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 255.893, 'tracknum': 5},
            {'id': 52820, 'title': 'mirrorball', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 208.973, 'tracknum': 6},
            {'id': 52821, 'title': 'seven', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 208.906, 'tracknum': 7},
            {'id': 52822, 'title': 'august', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 261.92, 'tracknum': 8},
            {'id': 52823, 'title': 'this is me trying', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 195.106, 'tracknum': 9},
            {'id': 52808, 'title': 'illicit affairs', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 190.893, 'tracknum': 10},
            {'id': 52809, 'title': 'invisible string', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 252.88, 'tracknum': 11},
            {'id': 52810, 'title': 'mad woman', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 237.266, 'tracknum': 12},
            {'id': 52811, 'title': 'epiphany', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 289.746, 'tracknum': 13},
            {'id': 52812, 'title': 'betty', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 294.52, 'tracknum': 14},
            {'id': 52813, 'title': 'peace', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 234.0, 'tracknum': 15},
            {'id': 52814, 'title': 'hoax', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 220.04, 'tracknum': 16},
            {'id': 52815, 'title': 'the lakes', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 211.813, 'tracknum': 17}]

    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home'),
                ],
            }
    assert playlistcontrol_handler(
                status,
                ['b1:e0:21:43:36:3b', 'playlistcontrol', 'cmd:add',
                    'useContextMenu:1', 'album_id:3650', 'count:17'],
                tn)
    tracks.assert_called_once_with(tn, album_id=3650)
    assert [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home'),
                (52807, 'the 1'),
                (52816, 'cardigan'),
                (52817, 'the last great american dynasty',),
                (52818, 'exile'),
                (52819, 'my tears ricochet'),
                (52820, 'mirrorball'),
                (52821, 'seven'),
                (52822, 'august'),
                (52823, 'this is me trying'),
                (52808, 'illicit affairs'),
                (52809, 'invisible string'),
                (52810, 'mad woman'),
                (52811, 'epiphany'),
                (52812, 'betty'),
                (52813, 'peace'),
                (52814, 'hoax'),
                (52815, 'the lakes'),
                ] == status['playlist']


def test_playlist_control_handler_track_play_next(mocker):
    tn = mocker.MagicMock()
    tracks = mocker.patch('squeezebox_cli.player.notifications.tracks')
    tracks.return_value = [{
        'id': 48537,
        'title': 'Hell Or High Water (live from Santa Monica Beach, CA)',
        'genre': 'Folk', 'artist': 'Passenger', 'album': 'Runaway (Live)',
        'duration': 190.16}]
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home')
                ],
            'playlist_cur_index': 5,
            }
    assert playlistcontrol_handler(
                status,
                ['b1:e0:21:43:36:3b', 'playlistcontrol', 'cmd:insert',
                    'useContextMenu:1', 'track_id:48537', 'count:1'],
                tn)
    tracks.assert_called_once_with(tn, track_id=48537)
    assert [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48537,
                 'Hell Or High Water (live from Santa Monica Beach, CA)'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home'),
                ] == status['playlist']
    assert 5 == status['playlist_cur_index']


def test_playlist_control_handler_album_play_next(mocker):
    tn = mocker.MagicMock()
    tracks = mocker.patch('squeezebox_cli.player.notifications.tracks')
    tracks.return_value = [
            {'id': 52807, 'title': 'the 1', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 210.24, 'tracknum': 1},
            {'id': 52816, 'title': 'cardigan', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 239.56, 'tracknum': 2},
            {'id': 52817, 'title': 'the last great american dynasty',
                'genre': 'Pop', 'artist': 'taylor swift',
                'album': 'folklore', 'duration': 231.0, 'tracknum': 3},
            {'id': 52818, 'title': 'exile', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 285.64, 'tracknum': 4},
            {'id': 52819, 'title': 'my tears ricochet', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 255.893, 'tracknum': 5},
            {'id': 52820, 'title': 'mirrorball', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 208.973, 'tracknum': 6},
            {'id': 52821, 'title': 'seven', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 208.906, 'tracknum': 7},
            {'id': 52822, 'title': 'august', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 261.92, 'tracknum': 8},
            {'id': 52823, 'title': 'this is me trying', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 195.106, 'tracknum': 9},
            {'id': 52808, 'title': 'illicit affairs', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 190.893, 'tracknum': 10},
            {'id': 52809, 'title': 'invisible string', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 252.88, 'tracknum': 11},
            {'id': 52810, 'title': 'mad woman', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 237.266, 'tracknum': 12},
            {'id': 52811, 'title': 'epiphany', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 289.746, 'tracknum': 13},
            {'id': 52812, 'title': 'betty', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 294.52, 'tracknum': 14},
            {'id': 52813, 'title': 'peace', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 234.0, 'tracknum': 15},
            {'id': 52814, 'title': 'hoax', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 220.04, 'tracknum': 16},
            {'id': 52815, 'title': 'the lakes', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 211.813, 'tracknum': 17}]
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home')
                ],
            'playlist_cur_index': 5,
            }
    assert playlistcontrol_handler(
                status,
                ['b1:e0:21:43:36:3b', 'playlistcontrol', 'cmd:insert',
                    'useContextMenu:1', 'album_id:3650', 'count:1'],
                tn)
    tracks.assert_called_once_with(tn, album_id=3650)
    assert [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (52807, 'the 1'),
                (52816, 'cardigan'),
                (52817, 'the last great american dynasty',),
                (52818, 'exile'),
                (52819, 'my tears ricochet'),
                (52820, 'mirrorball'),
                (52821, 'seven'),
                (52822, 'august'),
                (52823, 'this is me trying'),
                (52808, 'illicit affairs'),
                (52809, 'invisible string'),
                (52810, 'mad woman'),
                (52811, 'epiphany'),
                (52812, 'betty'),
                (52813, 'peace'),
                (52814, 'hoax'),
                (52815, 'the lakes'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home'),
                ] == status['playlist']
    assert 5 == status['playlist_cur_index']


def test_playlist_control_handler_play_track(mocker):
    tn = mocker.MagicMock()
    tracks = mocker.patch('squeezebox_cli.player.notifications.tracks')
    tracks.return_value = [{
        'id': 48537,
        'title': 'Hell Or High Water (live from Santa Monica Beach, CA)',
        'genre': 'Folk', 'artist': 'Passenger', 'album': 'Runaway (Live)',
        'duration': 190.16}]
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home')
                ],
            }
    assert playlistcontrol_handler(
                status,
                ['b1:e0:21:43:36:3b', 'playlistcontrol', 'cmd:load',
                    'useContextMenu:1', 'track_id:48537', 'count:1'],
                tn)
    tracks.assert_called_once_with(tn, track_id=48537)
    assert [(48537,
             'Hell Or High Water (live from Santa Monica Beach, CA)'),
            ] == status['playlist']
    assert 0 == status['playlist_cur_index']
    assert 'play' == status['mode']


def test_playlist_control_handler_play_album(mocker):
    tn = mocker.MagicMock()
    tracks = mocker.patch('squeezebox_cli.player.notifications.tracks')
    tracks.return_value = [
            {'id': 52807, 'title': 'the 1', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 210.24, 'tracknum': 1},
            {'id': 52816, 'title': 'cardigan', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 239.56, 'tracknum': 2},
            {'id': 52817, 'title': 'the last great american dynasty',
                'genre': 'Pop', 'artist': 'taylor swift',
                'album': 'folklore', 'duration': 231.0, 'tracknum': 3},
            {'id': 52818, 'title': 'exile', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 285.64, 'tracknum': 4},
            {'id': 52819, 'title': 'my tears ricochet', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 255.893, 'tracknum': 5},
            {'id': 52820, 'title': 'mirrorball', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 208.973, 'tracknum': 6},
            {'id': 52821, 'title': 'seven', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 208.906, 'tracknum': 7},
            {'id': 52822, 'title': 'august', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 261.92, 'tracknum': 8},
            {'id': 52823, 'title': 'this is me trying', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 195.106, 'tracknum': 9},
            {'id': 52808, 'title': 'illicit affairs', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 190.893, 'tracknum': 10},
            {'id': 52809, 'title': 'invisible string', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 252.88, 'tracknum': 11},
            {'id': 52810, 'title': 'mad woman', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 237.266, 'tracknum': 12},
            {'id': 52811, 'title': 'epiphany', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 289.746, 'tracknum': 13},
            {'id': 52812, 'title': 'betty', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 294.52, 'tracknum': 14},
            {'id': 52813, 'title': 'peace', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 234.0, 'tracknum': 15},
            {'id': 52814, 'title': 'hoax', 'genre': 'Pop',
                'artist': 'Taylor Swift', 'album': 'folklore',
                'duration': 220.04, 'tracknum': 16},
            {'id': 52815, 'title': 'the lakes', 'genre': 'Pop',
                'artist': 'taylor swift', 'album': 'folklore',
                'duration': 211.813, 'tracknum': 17}]
    status = {
            'playlist': [
                (48584, 'Everything'),
                (48586, 'If You Go'),
                (48587, 'When We Were Young'),
                (48588, 'Anywhere'),
                (48589, 'Somebody’s Love'),
                (48590, 'Young as the Morning Old as the Sea'),
                (48591, 'Beautiful Birds'),
                (48592, 'The Long Road'),
                (48593, 'Fool’s Gold'),
                (48585, 'Home')
                ],
            'playlist_cur_index': 5,
            }
    assert playlistcontrol_handler(
                status,
                ['b1:e0:21:43:36:3b', 'playlistcontrol', 'cmd:load',
                    'useContextMenu:1', 'album_id:3650', 'count:1'],
                tn)
    tracks.assert_called_once_with(tn, album_id=3650)
    assert [
                (52807, 'the 1'),
                (52816, 'cardigan'),
                (52817, 'the last great american dynasty',),
                (52818, 'exile'),
                (52819, 'my tears ricochet'),
                (52820, 'mirrorball'),
                (52821, 'seven'),
                (52822, 'august'),
                (52823, 'this is me trying'),
                (52808, 'illicit affairs'),
                (52809, 'invisible string'),
                (52810, 'mad woman'),
                (52811, 'epiphany'),
                (52812, 'betty'),
                (52813, 'peace'),
                (52814, 'hoax'),
                (52815, 'the lakes'),
                ] == status['playlist']
    assert 0 == status['playlist_cur_index']
    assert 'play' == status['mode']
