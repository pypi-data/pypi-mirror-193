import pytest

import squeezebox_cli.player


def test_list_players(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'players 0 2 count%3A2 playerindex%3A0 '
            b'playerid%3A00%3A0f%3A00%3A64%3A6d%3Ada uuid%3A '
            b'ip%3A192.168.1.92%3A33862 name%3AKitchen seq_no%3A0 '
            b'model%3Asqueezelite modelname%3ASqueezeLite power%3A1 '
            b'isplaying%3A0 displaytype%3Anone isplayer%3A1 '
            b'canpoweroff%3A1 connected%3A1 firmware%3Av1.8.7-1052 '
            b'playerindex%3A1 playerid%3A00%3A04%3A20%3A23%3A30%3A7f '
            b'uuid%3Ab0ff501bdcff1d6a18e0965b23844c94 '
            b'ip%3A192.168.1.116%3A41415 name%3ALounge seq_no%3A12 '
            b'model%3Afab4 modelname%3ASqueezebox%20Touch power%3A1 '
            b'isplaying%3A1 displaytype%3Anone isplayer%3A1 '
            b'canpoweroff%3A1 connected%3A1 firmware%3A7.8.0-r16754')
    assert [
            dict(playerindex=0,
                 playerid='00:0f:00:64:6d:da',
                 name='Kitchen',
                 isplaying=False),
            dict(playerindex=1,
                 playerid='00:04:20:23:30:7f',
                 name='Lounge',
                 isplaying=True),
            ] == squeezebox_cli.player.list_all(tn)
    tn.write.assert_called_once_with(b'players 0 100\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playerid_from_index_or_name_plsfrom_index(mocker):
    list_all = mocker.patch('squeezebox_cli.player.commands.list_all')
    tn = mocker.MagicMock()
    list_all.return_value = [
            dict(playerindex=0,
                 playerid='00:0f:00:64:6d:da',
                 name='Kitchen',
                 isplaying=False),
            dict(playerindex=1,
                 playerid='00:04:20:23:30:7f',
                 name='Lounge',
                 isplaying=True),
            ]
    assert ('00:04:20:23:30:7f'
            == squeezebox_cli.player.id_from_index_or_name(tn, 1))
    list_all.assert_called_once_with(tn)


def test_playerid_from_index_or_name_plsfrom_name(mocker):
    list_all = mocker.patch('squeezebox_cli.player.commands.list_all')
    tn = mocker.MagicMock()
    list_all.return_value = [
            dict(playerindex=0,
                 playerid='00:0f:00:64:6d:da',
                 name='Kitchen',
                 isplaying=False),
            dict(playerindex=1,
                 playerid='00:04:20:23:30:7f',
                 name='Lounge',
                 isplaying=True),
            ]
    assert ('00:04:20:23:30:7f'
            == squeezebox_cli.player.id_from_index_or_name(tn, 'Lounge'))
    list_all.assert_called_once_with(tn)


def test_playerid_from_index_or_name_plsbad_index(mocker):
    list_all = mocker.patch('squeezebox_cli.player.commands.list_all')
    tn = mocker.MagicMock()
    list_all.return_value = [
            dict(playerindex=0,
                 playerid='00:0f:00:64:6d:da',
                 name='Kitchen',
                 isplaying=False),
            dict(playerindex=1,
                 playerid='00:04:20:23:30:7f',
                 name='Lounge',
                 isplaying=True),
            ]
    assert squeezebox_cli.player.id_from_index_or_name(tn, 5) is None
    list_all.assert_called_once_with(tn)


def test_playerid_from_index_or_name_plsbad_name(mocker):
    list_all = mocker.patch('squeezebox_cli.player.commands.list_all')
    tn = mocker.MagicMock()
    list_all.return_value = [
        dict(playerindex=0, playerid='00:0f:00:64:6d:da', name='Kitchen',
             isplaying=False),
        dict(playerindex=1, playerid='00:04:20:23:30:7f', name='Lounge',
             isplaying=True),
        ]
    assert squeezebox_cli.player.id_from_index_or_name(tn, 'Bob') is None
    list_all.assert_called_once_with(tn)


def test_stop_player(mocker):
    ss = mocker.MagicMock()
    squeezebox_cli.player.stop(ss, 'Garden')
    ss.write.assert_called_once_with(b'Garden stop\n')


def test_player_status_radio_playing(mocker):
    ss = mocker.MagicMock()
    ss.read_until.return_value = (
            b'00%3A0f%3A00%3A64%3A6d%3Ada status 0 100'
            b' player_name%3AKitchen player_connected%3A1'
            b' player_ip%3A192.168.1.89%3A52682 power%3A1'
            b' signalstrength%3A0 mode%3Astop remote%3A1'
            b' current_title%3ARadio%20X%20London time%3A0 rate%3A1'
            b' mixer%20volume%3A49 playlist%20repeat%3A0'
            b' playlist%20shuffle%3A0 playlist%20mode%3Aoff'
            b' seq_no%3A0 playlist_cur_index%3A0'
            b' playlist_timestamp%3A1605606321.24679'
            b' playlist_tracks%3A1 digital_volume_control%3A1'
            b' remoteMeta%3AHASH(0x5bd7b78) playlist%20index%3A0'
            b' id%3A-88879072 title%3ARadio%20X%20London\n')
    assert (dict(playerid='00:0f:00:64:6d:da',
                 name='Kitchen',
                 mode='stop',
                 volume=49,
                 shuffle=squeezebox_cli.player.Shuffle.NONE,
                 repeat=squeezebox_cli.player.Repeat.NONE,
                 playlist_cur_index=0,
                 playlist=[(-88879072, 'Radio X London')])
            == squeezebox_cli.player.status(ss, '00:0f:00:64:6d:da'))
    ss.write.assert_called_once_with(
            b'00%3A0f%3A00%3A64%3A6d%3Ada status 0 100\n')
    ss.read_until.assert_called_once_with(b'\n')


def test_player_status_with_playlist_by_player_id(mocker):
    ss = mocker.MagicMock()
    ss.read_until.return_value = (
            b'00%3A04%3A20%3A23%3A30%3A7f status 0 100 '
            b'player_name%3ALounge player_connected%3A1 '
            b'player_ip%3A192.168.1.116%3A44203 power%3A1 '
            b'signalstrength%3A100 mode%3Astop time%3A0 rate%3A1 '
            b'duration%3A237.48 can_seek%3A1 mixer%20volume%3A50 '
            b'playlist%20repeat%3A0 playlist%20shuffle%3A0 '
            b'playlist%20mode%3Aoff seq_no%3A12 playlist_cur_index%3A24 '
            b'playlist_timestamp%3A1602466299.16138 playlist_tracks%3A28 '
            b'digital_volume_control%3A1 playlist%20index%3A0 id%3A52734 '
            b'title%3ACity%20of%20Love playlist%20index%3A1 id%3A52807 '
            b'title%3Athe%201 playlist%20index%3A2 id%3A52816 '
            b'title%3Acardigan playlist%20index%3A3 id%3A52817 '
            b'title%3Athe%20last%20great%20american%20dynasty '
            b'playlist%20index%3A4 id%3A52818 title%3Aexile '
            b'playlist%20index%3A5 id%3A52819 '
            b'title%3Amy%20tears%20ricochet%20 playlist%20index%3A6 '
            b'id%3A52820 title%3Amirrorball playlist%20index%3A7 '
            b'id%3A52821 title%3Aseven%20 playlist%20index%3A8 id%3A52822 '
            b'title%3Aaugust%20 playlist%20index%3A9 id%3A52823 '
            b'title%3Athis%20is%20me%20trying%20 playlist%20index%3A10 '
            b'id%3A52808 title%3Aillicit%20affairs%20 '
            b'playlist%20index%3A11 id%3A52809 '
            b'title%3Ainvisible%20string%20 playlist%20index%3A12 '
            b'id%3A52810 title%3Amad%20woman%20 playlist%20index%3A13 '
            b'id%3A52811 title%3Aepiphany%20 playlist%20index%3A14 '
            b'id%3A52812 title%3Abetty%20 playlist%20index%3A15 '
            b'id%3A52813 title%3Apeace playlist%20index%3A16 id%3A52814 '
            b'title%3Ahoax%20 playlist%20index%3A17 id%3A52815 '
            b'title%3Athe%20lakes playlist%20index%3A18 id%3A52736 '
            b'title%3AWeight%20of%20the%20World playlist%20index%3A19 '
            b'id%3A52737 title%3ATake%20Me playlist%20index%3A20 '
            b'id%3A52735 title%3AHit%20Me%20Where%20It%20Hurts '
            b'playlist%20index%3A21 id%3A52738 title%3AIn%20Our%20Room '
            b'playlist%20index%3A22 id%3A52739 title%3AIntervals '
            b'playlist%20index%3A23 id%3A52740 '
            b'title%3AKeeping%20My%20Faith%20Alive playlist%20index%3A24 '
            b'id%3A52741 title%3AA%20Walk%20in%20the%20Woods '
            b'playlist%20index%3A25 id%3A52742 title%3ACome%20on%20In '
            b'playlist%20index%3A26 id%3A52743 title%3AWonderful '
            b'playlist%20index%3A27 id%3A52744 title%3AOn%20Love\n')
    assert (dict(playerid='00:04:20:23:30:7f',
                 name='Lounge',
                 mode='stop',
                 volume=50,
                 shuffle=squeezebox_cli.player.Shuffle.NONE,
                 repeat=squeezebox_cli.player.Repeat.NONE,
                 duration=237.48,
                 playlist_cur_index=24,
                 playlist=[
                     (52734, 'City of Love'),
                     (52807, 'the 1'),
                     (52816, 'cardigan'),
                     (52817, 'the last great american dynasty'),
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
                     (52736, 'Weight of the World'),
                     (52737, 'Take Me'),
                     (52735, 'Hit Me Where It Hurts'),
                     (52738, 'In Our Room'),
                     (52739, 'Intervals'),
                     (52740, 'Keeping My Faith Alive'),
                     (52741, 'A Walk in the Woods'),
                     (52742, 'Come on In'),
                     (52743, 'Wonderful'),
                     (52744, 'On Love'),
                     ])
            == squeezebox_cli.player.status(ss, '00:04:20:23:30:7f'))
    ss.write.assert_called_once_with(
            b'00%3A04%3A20%3A23%3A30%3A7f status 0 100\n')


def test_count(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'player count 5\n'
    assert 5 == squeezebox_cli.player.count(tn)
    tn.write.assert_called_once_with(b'player count %3F\n')


def test_id_valid_index(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'player id 2 00%3A04%3A20%3A23%3A30%3A7f\n')
    assert '00:04:20:23:30:7f' == squeezebox_cli.player.id(tn, 2)
    tn.write.assert_called_once_with(b'player id 2 %3F\n')


def test_name_valid_index(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'player name 1 Lounge\n'
    assert 'Lounge' == squeezebox_cli.player.name(tn, 1)
    tn.write.assert_called_once_with(b'player name 1 %3F\n')


def test_name_invalid_index(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'player name 5\n'
    with pytest.raises(IndexError):
        squeezebox_cli.player.name(tn, 5)
    tn.write.assert_called_once_with(b'player name 5 %3F\n')


def test_name_valid_id(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'player name 01%3A23%3A45%3A67%3A89%3A01 Dad\'s%20Phone\n')
    assert ("Dad's Phone"
            == squeezebox_cli.player.name(tn, '01:23:45:67:89:01'))
    tn.write.assert_called_once_with(
            b'player name 01%3A23%3A45%3A67%3A89%3A01 %3F\n')


def test_ip_valid_index(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'player ip 5 123.456.789.123%3A12345\n'
    assert '123.456.789.123:12345' == squeezebox_cli.player.ip(tn, 5)
    tn.write.assert_called_once_with(b'player ip 5 %3F\n')


def test_signal_strength_valid_id(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'01%3A23%3A45%3A67%3A89%3A01 signalstrength 13\n')
    assert 13 == squeezebox_cli.player.signal_strength(tn,
                                                       '01:23:45:67:89:01')
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 signalstrength %3F\n')


def test_connected_valid_id_connected(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'01%3A23%3A45%3A67%3A89%3A01 connected 1\n')
    assert squeezebox_cli.player.connected(tn, '01:23:45:67:89:01')
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 connected %3F\n')


def test_connected_valid_id_not_connected(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'01%3A23%3A45%3A67%3A89%3A01 connected 0\n')
    assert not squeezebox_cli.player.connected(tn, '01:23:45:67:89:01')
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 connected %3F\n')


def test_sync_to_none(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'01%3A23%3A45%3A67%3A89%3A01 sync -\n')
    assert [] == squeezebox_cli.player.synced_to(tn, '01:23:45:67:89:01')
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 sync %3F\n')


def test_synced_to_one(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
        b'01%3A23%3A45%3A67%3A89%3A01 sync 22%3A22%3A22%3A22%3A22%3A22\n')
    assert (['22:22:22:22:22:22']
            == squeezebox_cli.player.synced_to(tn, '01:23:45:67:89:01'))
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 sync %3F\n')


def test_synced_to_multiple(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'01%3A23%3A45%3A67%3A89%3A01 sync '
            b'22:22:22:22:22:22,33:33:33:33:33:33\n')
    assert (['22:22:22:22:22:22', '33:33:33:33:33:33']
            == squeezebox_cli.player.synced_to(tn, '01:23:45:67:89:01'))
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 sync %3F\n')


def test_sync_to_id(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
        b'01%3A23%3A45%3A67%3A89%3A01 sync 22%3A22%3A22%3A22%3A22%3A22\n')
    squeezebox_cli.player.sync_to(
            tn, '01:23:45:67:89:01', '22:22:22:22:22:22')
    tn.write.assert_called_once_with(
        b'01%3A23%3A45%3A67%3A89%3A01 sync 22%3A22%3A22%3A22%3A22%3A22\n')


def test_sync_to_index(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
        b'01%3A23%3A45%3A67%3A89%3A01 sync 5\n')
    squeezebox_cli.player.sync_to(tn, '01:23:45:67:89:01', 5)
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 sync 5\n')


def test_sync_to_unsync(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'01%3A23%3A45%3A67%3A89%3A01 sync -\n')
    assert [] == squeezebox_cli.player.synced_to(tn, '01:23:45:67:89:01')
    tn.write.assert_called_once_with(
            b'01%3A23%3A45%3A67%3A89%3A01 sync %3F\n')


def test_none(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'syncgroups\n'
    assert [] == squeezebox_cli.player.sync_groups(tn)
    tn.write.assert_called_once_with(b'syncgroups %3F\n')


def test_one(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
         b'syncgroups sync_members%3A04%3A20%3A00%3A12%3A23%3A45,'
         b'04%3A20%3A00%3A12%3A34%3A56 '
         b'sync_member_names%3ALiving%20Room,Kitchen')
    assert [
            ('04:20:00:12:23:45', 'Living Room'),
            ('04:20:00:12:34:56', 'Kitchen'),
            ] == squeezebox_cli.player.sync_groups(tn)
    tn.write.assert_called_once_with(b'syncgroups %3F\n')


def test_get_volume(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume 57\n')
    assert 57 == squeezebox_cli.player.get_volume(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume %3F\n')


def test_set_volume(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume 75\n')
    squeezebox_cli.player.set_volume(tn, '12:34:56:78:90:12', 75)
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume 75\n')


def test_inc_volume(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume %2b7\n')
    squeezebox_cli.player.change_volume(tn, '12:34:56:78:90:12', 7)
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume %2B7\n')


def test_dec_volume(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume -7\n')
    squeezebox_cli.player.change_volume(tn, '12:34:56:78:90:12', 7, False)
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer volume -7\n')


def test_mute(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting 1\n')
    squeezebox_cli.player.mute(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting 1\n')


def test_unmute(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting 0\n')
    squeezebox_cli.player.unmute(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting 0\n')


def test_toggle_mute(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting\n')
    squeezebox_cli.player.toggle_mute(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting\n')


def test_get_mute_true(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting 1\n')
    assert squeezebox_cli.player.get_mute(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting %3F\n')


def test_get_mute_false(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting 0\n')
    assert not squeezebox_cli.player.get_mute(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 mixer muting %3F\n')


def test_single_chunk(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'players 0 5 count%3A2 playerindex%3A0 '
            b'playerid%3Aa5%3A41%3Ad2%3Acd%3Acd%3A05 '
            b'ip%3A127.0.0.1%3A60488 name%3A127.0.0.1 '
            b'model%3Asoftsqueeze displaytype%3Agraphic-280x16 '
            b'connected%3A1 playerindex%3A1 '
            b'playerid%3A00%3A04%3A20%3A02%3A00%3Ac8 '
            b'ip%3A192.168.1.22%3A3483 name%3AMovy model%3Aslimp3 '
            b'displaytype%3Anoritake-katakana connected%3A1\n')
    assert [
            dict(index=0,
                 id='a5:41:d2:cd:cd:05',
                 ip='127.0.0.1:60488',
                 name='127.0.0.1',
                 model='softsqueeze',
                 displaytype='graphic-280x16',
                 connected=True),
            dict(index=1,
                 id='00:04:20:02:00:c8',
                 ip='192.168.1.22:3483',
                 name='Movy',
                 model='slimp3',
                 displaytype='noritake-katakana',
                 connected=True),
            ] == squeezebox_cli.player.players(tn)
    tn.write.assert_called_once_with(b'players 0 5\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_two_chunks(mocker):
    tn = mocker.MagicMock()
    tn.read_until.side_effect = [
            (b'players 0 5 count%3A7 '
             b'playerindex%3A0 playerid%3Aid0 ip%3Aip0 name%3Aname0 '
             b'model%3Amodel0 displaytype%3Adisplay0 connected%3A1 '
             b'playerindex%3A1 playerid%3Aid1 ip%3Aip1 name%3Aname1 '
             b'model%3Amodel1 displaytype%3Adisplay1 connected%3A1 '
             b'playerindex%3A2 playerid%3Aid2 ip%3Aip2 name%3Aname2 '
             b'model%3Amodel2 displaytype%3Adisplay2 connected%3A1 '
             b'playerindex%3A3 playerid%3Aid3 ip%3Aip3 name%3Aname3 '
             b'model%3Amodel3 displaytype%3Adisplay3 connected%3A1 '
             b'playerindex%3A4 playerid%3Aid4 ip%3Aip4 name%3Aname4 '
             b'model%3Amodel4 displaytype%3Adisplay4 connected%3A1\n'),
            (b'players 5 5 count%3A7 '
             b'playerindex%3A5 playerid%3Aid5 ip%3Aip5 name%3Aname5 '
             b'model%3Amodel5 displaytype%3Adisplay5 connected%3A1 '
             b'playerindex%3A6 playerid%3Aid6 ip%3Aip6 name%3Aname6 '
             b'model%3Amodel6 displaytype%3Adisplay6 connected%3A1\n')
        ]
    assert [
            dict(index=0,
                 id='id0',
                 ip='ip0',
                 name='name0',
                 model='model0',
                 displaytype='display0',
                 connected=True),
            dict(index=1,
                 id='id1',
                 ip='ip1',
                 name='name1',
                 model='model1',
                 displaytype='display1',
                 connected=True),
            dict(index=2,
                 id='id2',
                 ip='ip2',
                 name='name2',
                 model='model2',
                 displaytype='display2',
                 connected=True),
            dict(index=3,
                 id='id3',
                 ip='ip3',
                 name='name3',
                 model='model3',
                 displaytype='display3',
                 connected=True),
            dict(index=4,
                 id='id4',
                 ip='ip4',
                 name='name4',
                 model='model4',
                 displaytype='display4',
                 connected=True),
            dict(index=5,
                 id='id5',
                 ip='ip5',
                 name='name5',
                 model='model5',
                 displaytype='display5',
                 connected=True),
            dict(index=6,
                 id='id6',
                 ip='ip6',
                 name='name6',
                 model='model6',
                 displaytype='display6',
                 connected=True),
            ] == squeezebox_cli.player.players(tn)
    tn.write.assert_has_calls(
            [mocker.call(b'players 0 5\n'), mocker.call(b'players 5 5\n')])
    tn.read_until.assert_has_calls([mocker.call(b'\n'), mocker.call(b'\n')])


def test_playlist_add_track(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Aadd '
            b'track_id%3A44333 count%3A1\n')
    squeezebox_cli.player.playlist_add(
            tn, 'b1:e0:21:43:36:3b', track_id=44333)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Aadd '
            b'track_id%3A44333\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_add_album(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Aadd '
            b'album_id%3A3232 count%3A14\n')
    squeezebox_cli.player.playlist_add(
            tn, 'b1:e0:21:43:36:3b', album_id=3232)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Aadd '
            b'album_id%3A3232\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_insert_track(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Ainsert '
            b'track_id%3A44333 count%3A1\n')
    squeezebox_cli.player.playlist_insert(
            tn, 'b1:e0:21:43:36:3b', track_id=44333)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Ainsert '
            b'track_id%3A44333\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_insert_album(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Ainsert '
            b'album_id%3A3232 count%3A14\n')
    squeezebox_cli.player.playlist_insert(
            tn, 'b1:e0:21:43:36:3b', album_id=3232)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlistcontrol cmd%3Ainsert '
            b'album_id%3A3232\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_remove(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist delete 4\n')
    squeezebox_cli.player.playlist_remove(tn, 'b1:e0:21:43:36:3b', 4)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist delete 4\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_play_play_current(mocker):
    tn = mocker.MagicMock()
    squeezebox_cli.player.play(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(b'12%3A34%3A56%3A78%3A90%3A12 play\n')


def test_play_play_track(mocker):
    tn = mocker.MagicMock()
    squeezebox_cli.player.play(tn, '12:34:56:78:90:12', track_id=1234)
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 playlistcontrol'
            b' cmd%3Aload track_id%3A1234\n')


def test_play_play_album(mocker):
    tn = mocker.MagicMock()
    squeezebox_cli.player.play(tn, '12:34:56:78:90:12', album_id=1234)
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 playlistcontrol'
            b' cmd%3Aload album_id%3A1234\n')


def test_pause(mocker):
    tn = mocker.MagicMock()
    squeezebox_cli.player.pause(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 pause\n')


def test_next(mocker):
    tn = mocker.MagicMock()
    squeezebox_cli.player.next(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 playlist index %2B1\n')


def test_previous(mocker):
    tn = mocker.MagicMock()
    squeezebox_cli.player.previous(tn, '12:34:56:78:90:12')
    tn.write.assert_called_once_with(
            b'12%3A34%3A56%3A78%3A90%3A12 playlist index -1\n')


def test_listen(mocker):
    tn = mocker.MagicMock()
    tn.side_effect = [b'listen 1\n', b'stop']
    for msg in squeezebox_cli.player.listen(tn):
        break
    tn.write.assert_called_once_with(b'listen 1\n')


def test_playlist_suffle_query_none(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle 0\n')
    assert (squeezebox_cli.player.Shuffle.NONE
            == squeezebox_cli.player.playlist_query_shuffle(
                tn, 'b1:e0:21:43:36:3b'))
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle %3F\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_suffle_query_song(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle 1\n')
    assert (squeezebox_cli.player.Shuffle.SONG
            == squeezebox_cli.player.playlist_query_shuffle(
                tn, 'b1:e0:21:43:36:3b'))
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle %3F\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_suffle_query_album(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle 2\n')
    assert (squeezebox_cli.player.Shuffle.ALBUM
            == squeezebox_cli.player.playlist_query_shuffle(
                tn, 'b1:e0:21:43:36:3b'))
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle %3F\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_shuffle_set_song(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle 1\n')
    squeezebox_cli.player.playlist_set_shuffle(
            tn, 'b1:e0:21:43:36:3b', squeezebox_cli.player.Shuffle.SONG)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle 1\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_shuffle_toggle(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle\n')
    squeezebox_cli.player.playlist_toggle_shuffle(tn, 'b1:e0:21:43:36:3b')
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist shuffle\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_repeat_query_none(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat 0\n')
    assert (squeezebox_cli.player.Repeat.NONE
            == squeezebox_cli.player.playlist_query_repeat(
                tn, 'b1:e0:21:43:36:3b'))
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat %3F\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_repeat_set_song(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat 1\n')
    squeezebox_cli.player.playlist_set_repeat(
            tn, 'b1:e0:21:43:36:3b', squeezebox_cli.player.Repeat.SONG)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat 1\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_repeat_set_all(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat 2\n')
    squeezebox_cli.player.playlist_set_repeat(
            tn, 'b1:e0:21:43:36:3b', squeezebox_cli.player.Repeat.ALL)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat 2\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_repeat_set_none(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat 0\n')
    squeezebox_cli.player.playlist_set_repeat(
            tn, 'b1:e0:21:43:36:3b', squeezebox_cli.player.Repeat.NONE)
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat 0\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_playlist_repeat_toggke(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat\n')
    squeezebox_cli.player.playlist_toggle_repeat(tn, 'b1:e0:21:43:36:3b')
    tn.write.assert_called_once_with(
            b'b1%3Ae0%3A21%3A43%3A36%3A3b playlist repeat\n')
    tn.read_until.assert_called_once_with(b'\n')

# TODO: multi-reply tests
