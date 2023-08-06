from squeezebox_cli.core.protocol import send_receive, tagged_command, \
        parse_tags


def test_send_receive_quoting(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'text%3Acolon%3Fquery tag%3Avalue\n'
    assert (['text:colon?query', 'tag:value']
            == send_receive(tn, ['text:colon?query', 'tag:value']))
    tn.write.assert_called_once_with(b'text%3Acolon%3Fquery tag%3Avalue\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_send_receive_all_strings(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'p0 p1 p2 p3 p4\n'
    assert (['p0', 'p1', 'p2', 'p3', 'p4']
            == send_receive(tn, ['p0', 'p1', 'p2', 'p3', 'p4']))
    tn.write.assert_called_once_with(b'p0 p1 p2 p3 p4\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_send_receive_escape_mac_address(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'12%3A34%3A56 p1 p2 p3 p4\n'
    assert (['12:34:56', 'p1', 'p2', 'p3', 'p4']
            == send_receive(tn, ['12:34:56', 'p1', 'p2', 'p3', 'p4']))
    tn.write.assert_called_once_with(b'12%3A34%3A56 p1 p2 p3 p4\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_send_receive_escape_tagged_value(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'p0 p1 p2 name%3ASt.%20Martin%27s p4\n'
    assert (['p0', 'p1', 'p2', "name:St. Martin's", 'p4']
            == send_receive(tn, ['p0', 'p1', 'p2', "name:St. Martin's", 'p4']))
    tn.write.assert_called_once_with(b'p0 p1 p2 name%3ASt.%20Martin%27s p4\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_tagged_command_with_player_id():
    assert [
            '12:34:56',
            'cmd',
            '0',
            '20',
            't1:v1',
            't2:v2:v2a?',
            't3:',
            't4:v4',
            ] == tagged_command(['12:34:56', 'cmd', 0, 20],
                                [
                                    ('t1', 'v1'),
                                    ('t2', 'v2:v2a?'),
                                    ('t3', ''),
                                    ('t4', 'v4'),
                                    ])


def test_parse_tags_empty_list():
    assert [] == parse_tags([])


def test_parse_tags_no_tags():
    assert [] == parse_tags(['p0', 'p1', 'p2'])


def test_parse_tags_all_tags():
    assert [
            ('k1', 'v1'),
            ('k2', 'v2:v2a'),
            ('k3', 'v3'),
            ] == parse_tags(['k1:v1', 'k2:v2:v2a', 'k3:v3'])
