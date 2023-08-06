from datetime import timedelta

import squeezebox_cli.database as database


def test_rescan_action(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'rescan\n'
    database.rescan(tn)
    tn.write.assert_called_once_with(b'rescan\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_rescan_query_scanning_true(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'rescan 1\n'
    assert database.rescanning(tn)
    tn.write.assert_called_once_with(b'rescan %3F\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_rescan_query_scanning_false(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'rescan 0\n'
    assert not database.rescanning(tn)
    tn.write.assert_called_once_with(b'rescan %3F\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_rescan_playlists(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'rescan playlists\n'
    database.rescan_playlists(tn)
    tn.write.assert_called_once_with(b'rescan playlists\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_rescan_progress_in_progress(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'rescanprogress rescan%3A1 '
            b'totaltime%3A00%3A00%3A07 directory%3A100 playlist%3A100 '
            b'itunes%3A15\n')
    assert dict(
            totaltime=timedelta(seconds=7),
            importers=[
                ('directory', 100),
                ('playlist', 100),
                ('itunes', 15),
                ]) == database.rescan_progress(tn)
    tn.write.assert_called_once_with(b'rescanprogress\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_rescan_progress_not_in_progress(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'rescanprogress rescan%3A0'
    assert database.rescan_progress(tn) is None
    tn.write.assert_called_once_with(b'rescanprogress\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_totals_genres(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'info total genres 12\n'
    assert 12 == database.total_genres(tn)
    tn.write.assert_called_once_with(b'info total genres %3F\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_totals_artists(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'info total artists 123\n'
    assert 123 == database.total_artists(tn)
    tn.write.assert_called_once_with(b'info total artists %3F\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_totals_songs(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'info total songs 123\n'
    assert 123 == database.total_songs(tn)
    tn.write.assert_called_once_with(b'info total songs %3F\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_totals_albums(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'info total albums 123\n'
    assert 123 == database.total_albums(tn)
    tn.write.assert_called_once_with(b'info total albums %3F\n')
    tn.read_until.asser_called_once_with(b'\n')


def test_genres_get_all_multiple_chunks(mocker):
    tn = mocker.MagicMock()
    tn.read_until.side_effect = [
            (b'genres 0 50 '
             b'id%3A298 genre%3A255) id%3A272 genre%3AAcoustic '
             b'id%3A304 genre%3AAlt%20Rock id%3A276 genre%3AAlternative '
             b'id%3A303 genre%3AAlternative%2FIndie '
             b'id%3A288 genre%3AAlternative%20%26%20Punk '
             b'id%3A294 genre%3AAlternative%20Rock '
             b'id%3A265 genre%3AAlternRock id%3A309 genre%3AAmbient '
             b'id%3A291 genre%3ABlues id%3A301 genre%3ACabaret '
             b'id%3A312 genre%3AChillout id%3A306 genre%3AChristmas '
             b'id%3A287 genre%3AClassic%20Rock id%3A267 genre%3AClassical '
             b'id%3A266 genre%3ACountry id%3A310 genre%3ADance '
             b'id%3A269 genre%3AElectronic id%3A311 genre%3AFilm '
             b'id%3A279 genre%3AFolk id%3A307 genre%3AFolk%2C%20acoustic '
             b'id%3A297 genre%3AFunk%2FDance id%3A300 genre%3AHard%20Rock '
             b'id%3A283 genre%3AIndie id%3A284 genre%3AIndie%20Rock '
             b'id%3A296 genre%3AIndie%20Rock%20Pop '
             b'id%3A295 genre%3AInstrumental '
             b'id%3A308 genre%3AInternational id%3A285 genre%3AJazz '
             b'id%3A314 genre%3AKids id%3A305 genre%3ALatin '
             b'id%3A278 genre%3AMeditative id%3A292 genre%3AMetal '
             b'id%3A286 genre%3AMusical id%3A316 genre%3ANew%20Age '
             b'id%3A280 genre%3ANo%20Genre id%3A281 genre%3AOther '
             b'id%3A270 genre%3APop id%3A274 genre%3APop-Folk '
             b'id%3A282 genre%3APsychedelic id%3A290 genre%3APunk '
             b'id%3A289 genre%3AR%26B id%3A268 genre%3AReggae '
             b'id%3A302 genre%3ARetro id%3A275 genre%3ARock '
             b'id%3A273 genre%3ARock%2FFolk id%3A271 genre%3ARock%2FPop '
             b'id%3A293 genre%3ARock%20%26%20Roll id%3A313 genre%3ASoul '
             b'id%3A317 genre%3ATribal count%3A53\n'),
            (b'genres 50 50 '
             b'id%3A299 genre%3AUnknown id%3A277 genre%3AVocal '
             b'id%3A315 genre%3AWorld count%3A53\n')]
    assert {
            298: '255)',
            272: 'Acoustic',
            304: 'Alt Rock',
            276: 'Alternative',
            303: 'Alternative/Indie',
            288: 'Alternative & Punk',
            294: 'Alternative Rock',
            265: 'AlternRock',
            309: 'Ambient',
            291: 'Blues',
            301: 'Cabaret',
            312: 'Chillout',
            306: 'Christmas',
            287: 'Classic Rock',
            267: 'Classical',
            266: 'Country',
            310: 'Dance',
            269: 'Electronic',
            311: 'Film',
            279: 'Folk',
            307: 'Folk, acoustic',
            297: 'Funk/Dance',
            300: 'Hard Rock',
            283: 'Indie',
            284: 'Indie Rock',
            296: 'Indie Rock Pop',
            295: 'Instrumental',
            308: 'International',
            285: 'Jazz',
            314: 'Kids',
            305: 'Latin',
            278: 'Meditative',
            292: 'Metal',
            286: 'Musical',
            316: 'New Age',
            280: 'No Genre',
            281: 'Other',
            270: 'Pop',
            274: 'Pop-Folk',
            282: 'Psychedelic',
            290: 'Punk',
            289: 'R&B',
            268: 'Reggae',
            302: 'Retro',
            275: 'Rock',
            273: 'Rock/Folk',
            271: 'Rock/Pop',
            293: 'Rock & Roll',
            313: 'Soul',
            317: 'Tribal',
            299: 'Unknown',
            277: 'Vocal',
            315: 'World',
            } == database.genres(tn)
    tn.write.assert_has_calls(
            [mocker.call(b'genres 0 50\n'), mocker.call(b'genres 50 50\n')])
    tn.read_until.assert_has_calls([mocker.call(b'\n'), mocker.call(b'\n')])


def test_genres_search_found(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'genres 0 50 search%3AFolk '
            b'id%3A279 genre%3AFolk id%3A307 genre%3AFolk%2C%20acoustic '
            b'id%3A274 genre%3APop-Folk id%3A273 genre%3ARock%2FFolk '
            b'count%3A4\n')
    assert {
            279: 'Folk',
            307: 'Folk, acoustic',
            274: 'Pop-Folk',
            273: 'Rock/Folk',
            } == database.genres(tn, search='Folk')
    tn.write.assert_called_once_with(b'genres 0 50 search%3AFolk\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_artists_get_all(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'artists 0 500 '
            b'id%3A8696 artist%3A5%20Seconds%20of%20Summer '
            b'id%3A7682 artist%3A50%20Cent id%3A7573 artist%3A6%20Notes '
            b'id%3A8362 artist%3A702 id%3A8591 artist%3A98%20Degrees '
            b'id%3A7690 artist%3AA%20Boogie%20wit%20da%20Hoodie '
            b'id%3A8369 artist%3AAaliyah id%3A8297 artist%3AABBA '
            b'id%3A7834 artist%3AAbigail%20Washburn '
            b'id%3A8983 artist%3AColonel%20Abrams '
            b'id%3A7725 artist%3AAceface '
            b'id%3A9026 artist%3AOleta%20Adams id%3A7575 artist%3AAdele '
            b'id%3A7598 artist%3AAdolphe%20Adam%20trans.%20'
            b'Sietse%20van%20Gorkom '
            b'id%3A8854 artist%3AAfrojack%20feat.%20Chris%20Brown '
            b'id%3A8837 artist%3AAggro%20Santos id%3A8906 artist%3AAir '
            b'id%3A7579 artist%3AAirhead '
            b'id%3A7835 artist%3AAlasdair%20Roberts%20and%20Friends '
            b'id%3A8829 artist%3AAlbinoni '
            b'id%3A7837 artist%3AAlessi\'s%20Ark '
            b'id%3A8852 artist%3AAlex%20Metrick%20%26%20JLC '
            b'id%3A9075 artist%3AAli%20Hassan%20Kuban '
            b'id%3A8377 artist%3ATatyana%20Ali '
            b'id%3A8499 artist%3AAlice%20DeeJay '
            b'id%3A7582 artist%3AAll%20About%20Eve '
            b'id%3A7838 artist%3AAll%20Jigged%20Out '
            b'id%3A8325 artist%3AAll%20Saints '
            b'id%3A7839 artist%3AAllan%20Yn%20Y%20Fan '
            b'id%3A8635 artist%3ALily%20Allen id%3A8261 artist%3AAlt-J '
            b'id%3A9074 artist%3AAlyssa%20Reid '
            b'id%3A8055 artist%3AShola%20Ama '
            b'id%3A8149 artist%3AThe%20Andrews%20Sisters '
            b'id%3A8621 artist%3AAngel '
            b'id%3A8536 artist%3ASteve%20Angello '
            b'id%3A8664 artist%3AAnne-Marie '
            b'id%3A8586 artist%3AAnother%20Level '
            b'id%3A8291 artist%3ARay%20Anthony '
            b'id%3A7586 artist%3AAppleseed id%3A9021 artist%3AArban '
            b'id%3A8630 artist%3AArctic%20Monkeys '
            b'id%3A7840 artist%3AArdentjohn '
            b'id%3A8660 artist%3AAriana%20Grande%20feat.%20Nicki%20Minaj '
            b'id%3A8867 artist%3AArmand%20Van%20Helden%20'
            b'feat.%20Spank%20Rock '
            b'id%3A8863 artist%3AArmin%20Van%20Buuren '
            b'id%3A8945 artist%3ACraig%20Armstrong '
            b'id%3A8161 artist%3ALouis%20Armstrong '
            b'id%3A9066 artist%3ADesi%20Arnaz '
            b'id%3A8167 artist%3AEddy%20Arnold count%3A50\n')
    assert {
            8696: '5 Seconds of Summer',
            7682: '50 Cent',
            7573: '6 Notes',
            8362: '702',
            8591: '98 Degrees',
            7690: 'A Boogie wit da Hoodie',
            8369: 'Aaliyah',
            8297: 'ABBA',
            7834: 'Abigail Washburn',
            8983: 'Colonel Abrams',
            7725: 'Aceface',
            9026: 'Oleta Adams',
            7575: 'Adele',
            7598: 'Adolphe Adam trans. Sietse van Gorkom',
            8854: 'Afrojack feat. Chris Brown',
            8837: 'Aggro Santos',
            8906: 'Air',
            7579: 'Airhead',
            7835: 'Alasdair Roberts and Friends',
            8829: 'Albinoni',
            7837: 'Alessi\'s Ark',
            8852: 'Alex Metrick & JLC',
            9075: 'Ali Hassan Kuban',
            8377: 'Tatyana Ali',
            8499: 'Alice DeeJay',
            7582: 'All About Eve',
            7838: 'All Jigged Out',
            8325: 'All Saints',
            7839: 'Allan Yn Y Fan',
            8635: 'Lily Allen',
            8261: 'Alt-J',
            9074: 'Alyssa Reid',
            8055: 'Shola Ama',
            8149: 'The Andrews Sisters',
            8621: 'Angel',
            8536: 'Steve Angello',
            8664: 'Anne-Marie',
            8586: 'Another Level',
            8291: 'Ray Anthony',
            7586: 'Appleseed',
            9021: 'Arban',
            8630: 'Arctic Monkeys',
            7840: 'Ardentjohn',
            8660: 'Ariana Grande feat. Nicki Minaj',
            8867: 'Armand Van Helden feat. Spank Rock',
            8863: 'Armin Van Buuren',
            8945: 'Craig Armstrong',
            8161: 'Louis Armstrong',
            9066: 'Desi Arnaz',
            8167: 'Eddy Arnold',
    } == database.artists(tn)
    tn.write.assert_called_once_with(b'artists 0 100\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_artists_search(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'artists 0 50 search%3ABen '
            b'id%3A8448 artist%3ABent '
            b'id%3A7602 artist%3ABen%20Howard '
            b'id%3A8655 artist%3ABen%20Pearce '
            b'id%3A8988 artist%3ABen%20Webster '
            b'id%3A8171 artist%3ABrook%20Benton '
            b'id%3A8939 artist%3ABentley%20Rhythm%20Ace '
            b'id%3A7941 artist%3AJosienne%20Clarke%2C%20Ben%20Walker '
            b'id%3A8785 artist%3ABen%20Haenow%20feat.%20Kelly%20Clarkson '
            b'id%3A8163 artist%3ALouis%20Armstrong%20%26%20Benny%20'
            b'Carter%20and%20His%20Orchestra '
            b'count%3A9')
    assert {
            8448: 'Bent',
            7602: 'Ben Howard',
            8655: 'Ben Pearce',
            8988: 'Ben Webster',
            8171: 'Brook Benton',
            8939: 'Bentley Rhythm Ace',
            7941: 'Josienne Clarke, Ben Walker',
            8785: 'Ben Haenow feat. Kelly Clarkson',
            8163: 'Louis Armstrong & Benny Carter and His Orchestra',
            } == database.artists(tn, search='Ben')
    tn.write.assert_called_once_with(b'artists 0 100 search%3ABen\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_albums_basic(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'albums 0 100 '
            b'id%3A3164 album%3A%2B '
            b'id%3A3163 album%3Adivide '
            b'id%3A3238 album%3A100%20Broken%20Windows '
            b'id%3A3585 album%3A100%20Hits%3A%20Christmas%20Legends '
            b'id%3A3586 album%3A100%20Popular%20Classics '
            b'count%3A5')
    assert {
            3164: '+',
            3163: 'divide',
            3238: '100 Broken Windows',
            3585: '100 Hits: Christmas Legends',
            3586: '100 Popular Classics',
        } == database.albums(tn)
    tn.read_until.assert_called_once_with(b'\n')
    tn.write.assert_called_once_with(b'albums 0 100\n')


def test_albums_extended(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'albums 0 100 tags%3AywaSsXl '
            b'id%3A3164 year%3A2011 compilation%3A0 album%3A%2B '
            b'album_replay_gain%3A-5.78 artist_id%3A7671 '
            b'artist%3AEd%20Sheeran textkey%3A%2B '
            b'id%3A3163 year%3A0 compilation%3A0 album%3Adivide '
            b'album_replay_gain%3A-9.66 artist_id%3A7671 '
            b'artist%3AEd%20Sheeran textkey%3Ad '
            b'id%3A3238 year%3A2000 compilation%3A0 '
            b'album%3A100%20Broken%20Windows '
            b'album_replay_gain%3A-9.12 artist_id%3A7919 '
            b'artist%3AIdlewild textkey%3A1 '
            b'id%3A3585 year%3A0 compilation%3A1 '
            b'album%3A100%20Hits%3A%20Christmas%20Legends '
            b'album_replay_gain%3A-8.52 artist_id%3A7574 '
            b'artist%3AVarious%20Artists textkey%3A1 '
            b'id%3A3586 year%3A2005 compilation%3A1 '
            b'album%3A100%20Popular%20Classics '
            b'album_replay_gain%3A-2.86 artist_id%3A7574 '
            b'artist%3AVarious%20Artists textkey%3A1 '
            b'count%3A5\n')
    assert [
            dict(id=3164, year=2011, compilation=False,
                 album_replay_gain=-5.78, artist_id=7671,
                 artist='Ed Sheeran', textkey='+', album='+'),
            dict(id=3163, year=None, compilation=False, album='divide',
                 album_replay_gain=-9.66, artist_id=7671,
                 artist='Ed Sheeran', textkey='d'),
            dict(id=3238, year=2000, compilation=False,
                 album_replay_gain=-9.12, artist_id=7919,
                 artist='Idlewild', textkey='1',
                 album='100 Broken Windows'),
            dict(id=3585, year=None, compilation=True,
                 album_replay_gain=-8.52, artist_id=7574,
                 artist='Various Artists', textkey='1',
                 album='100 Hits: Christmas Legends'),
            dict(id=3586, year=2005, compilation=True,
                 album_replay_gain=-2.86, artist_id=7574,
                 artist='Various Artists', textkey='1',
                 album='100 Popular Classics'),
        ] == database.albums(tn, extended=True)
    tn.write.assert_called_once_with(b'albums 0 100 tags%3AywaSsXl\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_albums_extended_search(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'albums 0 5 tags%3AywaSsXl search%3Abob '
            b'id%3A3101 '
            b'album%3ALegend%3A%20The%20Best%20of%20Bob%20Marley%20and'
            b'%20The%20Wailers year%3A2002 compilation%3A0 '
            b'album_replay_gain%3A-6.47 artist_id%3A7614 '
            b'artist%3ABob%20Marley%20%26%20The%20Wailers '
            b'id%3A3281 album%3AOnly%20Whispering year%3A2006 '
            b'compilation%3A0 album_replay_gain%3A-8.77 artist_id%3A7939 '
            b'artist%3AJosh%20Woodward '
            b'id%3A3036 album%3A19 year%3A2008 compilation%3A0 '
            b'album_replay_gain%3A-8.5 artist_id%3A7575 artist%3AAdele '
            b'id%3A3201 album%3AFrukie year%3A0 compilation%3A1 '
            b'album_replay_gain%3A1.84 artist_id%3A7574 '
            b'artist%3AVarious%20Artists '
            b'id%3A3618 album%3ASunday%20Morning%20Songs year%3A2006 '
            b'compilation%3A1 album_replay_gain%3A-7.02 artist_id%3A7574 '
            b'artist%3AVarious%20Artists count%3A3\n')
    assert [
            dict(id=3101,
                 album='Legend: The Best of Bob Marley and The Wailers',
                 year=2002,
                 compilation=False,
                 album_replay_gain=-6.47,
                 artist_id=7614,
                 artist='Bob Marley & The Wailers'),
            dict(id=3281,
                 album='Only Whispering',
                 year=2006,
                 compilation=False,
                 album_replay_gain=-8.77,
                 artist_id=7939,
                 artist='Josh Woodward'),
            dict(id=3036,
                 album='19',
                 year=2008,
                 compilation=False,
                 album_replay_gain=-8.5,
                 artist_id=7575,
                 artist='Adele'),
            dict(id=3201,
                 album='Frukie',
                 year=None,
                 compilation=True,
                 album_replay_gain=1.84,
                 artist_id=7574,
                 artist='Various Artists'),
            dict(id=3618,
                 album='Sunday Morning Songs',
                 year=2006,
                 compilation=True,
                 album_replay_gain=-7.02,
                 artist_id=7574,
                 artist='Various Artists')
            ] == database.albums(tn, extended=True, search='bob')
    tn.write.assert_called_once_with(
            b'albums 0 100 tags%3AywaSsXl search%3Abob\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_years_no_rescan(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'years 0 100 '
            b'year%3A2020 year%3A2019 year%3A2018 year%3A2017 year%3A2016 '
            b'count%3A5\n')
    assert [2020, 2019, 2018, 2017, 2016] == database.years(tn)
    tn.write.assert_called_once_with(b'years 0 100\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_years_rescan_in_progress(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'years 0 100 rescan%3A1 '
            b'year%3A2020 year%3A2019 year%3A2018 year%3A2017 year%3A2016 '
            b'count%3A5\n')
    assert [2020, 2019, 2018, 2017, 2016] == database.years(tn)
    tn.write.assert_called_once_with(b'years 0 100\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_song_info_default_tags(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'songinfo 0 100 track_id%3A50325 tags%3AaCdegilpqstuy '
            b'id%3A50325 title%3A0.34 artist%3ATexas compilation%3A0 '
            b'duration%3A34.666 album_id%3A3532 genre%3ARock%2FPop '
            b'album%3AWhite%20on%20Blonde genre_id%3A271 artist_id%3A8091 '
            b'tracknum%3A1 url%3Afile%3A%2F%2F%2Fmedia%2Fusb0%2Fmusic%2F'
            b'Texas%2FWhite%2520on%2520Blonde%2F1%2520-%25200.34.flac '
            b'year%3A1997\n')
    assert dict(id=50325,
                title='0.34',
                artist='Texas',
                compilation=False,
                duration=34.666,
                album_id=3532,
                genre='Rock/Pop',
                album='White on Blonde',
                genre_id=271,
                artist_id=8091,
                tracknum=1,
                url='file:///media/usb0/music/Texas/White%20on%20Blonde/'
                    '1%20-%200.34.flac',
                year=1997) == database.songinfo(tn, 50325)
    tn.write.assert_called_once_with(
            b'songinfo 0 100 track_id%3A50325 tags%3AaCdegilpqstuy\n')
    tn.read_until(b'\n')


def test_tracks_default(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'tracks 0 100 '
            b'id%3A49769 title%3A- genre%3ARock%2FPop '
            b'artist%3ASnow%20Patrol album%3AEyes%20Open '
            b'duration%3A235.373 '
            b'id%3A48705 title%3A%3F genre%3APunk '
            b'artist%3APlaster%20Caster album%3A%22Promo%202007%22 '
            b'duration%3A182.36 '
            b'id%3A50327 title%3A0.28 genre%3ARock%2FPop '
            b'artist%3ATexas album%3AWhite%20on%20Blonde '
            b'duration%3A28.466 '
            b'id%3A50325 title%3A0.34 genre%3ARock%2FPop '
            b'artist%3ATexas album%3AWhite%20on%20Blonde '
            b'duration%3A34.666 '
            b'id%3A50272 title%3A036 genre%3ARock%2FPop '
            b'artist%3ATexas album%3ARed%20Book duration%3A36.213 '
            b'count%3A5\n')
    assert [
            dict(id=49769,
                 title='-',
                 genre='Rock/Pop',
                 artist='Snow Patrol',
                 album='Eyes Open',
                 duration=235.373),
            dict(id=48705,
                 title='?',
                 genre='Punk',
                 artist='Plaster Caster',
                 album='"Promo 2007"',
                 duration=182.36),
            dict(id=50327,
                 title='0.28',
                 genre='Rock/Pop',
                 artist='Texas',
                 album='White on Blonde',
                 duration=28.466),
            dict(id=50325,
                 title='0.34',
                 genre='Rock/Pop',
                 artist='Texas',
                 album='White on Blonde',
                 duration=34.666),
            dict(id=50272,
                 title='036',
                 genre='Rock/Pop',
                 artist='Texas',
                 album='Red Book',
                 duration=36.213),
            ] == database.tracks(tn)
    tn.write.assert_called_once_with(b'tracks 0 100\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_tracks_default_search(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'tracks 0 100 search%3Awide '
            b'id%3A44333 title%3ADeep%20%26%20Wide%20%26%20Tall '
            b'genre%3APop artist%3AAztec%20Camera album%3ALove '
            b'duration%3A247.266 '
            b'id%3A44352 title%3ADeep%20%26%20Wide%20%26%20Tall '
            b'genre%3APop artist%3AAztec%20Camera '
            b'album%3AThe%20Best%20of%20Aztec%20Camera duration%3A245.106 '
            b'id%3A46763 title%3AEyes%20Wide%20Open genre%3ARock%2FFolk '
            b'artist%3AHothouse%20Flowers album%3AHome duration%3A195.306 '
            b'id%3A51650 title%3AEyes%20Wide%20Open genre%3ANo%20Genre '
            b'artist%3ARadio%204 '
            b'album%3ANY-LON%20A%20Transatlantic%20Romance '
            b'duration%3A224.133 '
            b'id%3A51685 title%3AWide%20Awake genre%3APop '
            b'artist%3AKaty%20Perry '
            b'album%3ANow%20That\'s%20What%20I%20Call%20Music!%2083 '
            b'duration%3A219.893 '
            b'id%3A49610 title%3AWidecombe%20Fair genre%3AFolk '
            b'artist%3AShow%20of%20Hands '
            b'album%3ARoots%3A%20The%20Best%20of%20Show%20of%20Hands '
            b'duration%3A206.866 '
            b'id%3A46766 title%3AWidescreen genre%3APop '
            b'artist%3AHue%20%26%20Cry '
            b'album%3ALabours%20of%20Love%2C%20'
            b'The%20Best%20of%20Hue%20and%20Cry '
            b'duration%3A227.826 '
            b'id%3A52102 title%3AChip%20Funk%20(Original%20Mix) '
            b'genre%3ADance artist%3AWide%20Boys '
            b'album%3ARunning%20Trax%202014%3A%20High%20Energy '
            b'duration%3A223.2 '
            b'id%3A52119 title%3APreacher%20(Radio%20Edit) genre%3ADance '
            b'artist%3AVarious%20Artists '
            b'album%3ARunning%20Trax%202014%3A%20Warm%20Up '
            b'duration%3A232.546 '
            b'id%3A51581 title%3AThe%20Word genre%3APop '
            b'artist%3AThe%20Wideboys '
            b'album%3AMinistry%20of%20Sound%3A%20The%20Annual%202013 '
            b'duration%3A208.133 '
            b'id%3A44193 title%3AImmersed genre%3AAcoustic '
            b'artist%3AAllison%20Crowe album%3ASecrets%20(originals) '
            b'duration%3A258.373 '
            b'id%3A44178 title%3AImmersed%20(live) genre%3AAcoustic '
            b'artist%3AAllison%20Crowe '
            b'album%3ALive%20at%20Wood%20Hall%20(originals) '
            b'duration%3A244.253 '
            b'count%3A12\n')
    assert [
            dict(id=44333,
                 title='Deep & Wide & Tall',
                 genre='Pop',
                 artist='Aztec Camera',
                 album='Love',
                 duration=247.266),
            dict(id=44352,
                 title='Deep & Wide & Tall',
                 genre='Pop',
                 artist='Aztec Camera',
                 album='The Best of Aztec Camera',
                 duration=245.106),
            dict(id=46763,
                 title='Eyes Wide Open',
                 genre='Rock/Folk',
                 artist='Hothouse Flowers',
                 album='Home',
                 duration=195.306),
            dict(id=51650,
                 title='Eyes Wide Open',
                 genre='No Genre',
                 artist='Radio 4',
                 album='NY-LON A Transatlantic Romance',
                 duration=224.133),
            dict(id=51685,
                 title='Wide Awake',
                 genre='Pop',
                 artist='Katy Perry',
                 album='Now That\'s What I Call Music! 83',
                 duration=219.893),
            dict(id=49610,
                 title='Widecombe Fair',
                 genre='Folk',
                 artist='Show of Hands',
                 album='Roots: The Best of Show of Hands',
                 duration=206.866),
            dict(id=46766,
                 title='Widescreen',
                 genre='Pop',
                 artist='Hue & Cry',
                 album='Labours of Love, The Best of Hue and Cry',
                 duration=227.826),
            dict(id=52102,
                 title='Chip Funk (Original Mix)',
                 genre='Dance',
                 artist='Wide Boys',
                 album='Running Trax 2014: High Energy',
                 duration=223.2),
            dict(id=52119,
                 title='Preacher (Radio Edit)',
                 genre='Dance',
                 artist='Various Artists',
                 album='Running Trax 2014: Warm Up',
                 duration=232.546),
            dict(id=51581,
                 title='The Word',
                 genre='Pop',
                 artist='The Wideboys',
                 album='Ministry of Sound: The Annual 2013',
                 duration=208.133),
            dict(id=44193,
                 title='Immersed',
                 genre='Acoustic',
                 artist='Allison Crowe',
                 album='Secrets (originals)',
                 duration=258.373),
            dict(id=44178, title='Immersed (live)',
                 genre='Acoustic',
                 artist='Allison Crowe',
                 album='Live at Wood Hall (originals)',
                 duration=244.253),
            ] == database.tracks(tn, search='wide')
    tn.write.assert_called_once_with(b'tracks 0 100 search%3Awide\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_tracks_default_artist(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'tracks 0 5 artist_id%3A8696 sort%3Aalbumtrack '
            b'id%3A51823 title%3AAmnesia genre%3APop '
            b'artist%3A5%20Seconds%20of%20Summer '
            b'album%3ANow%20That\'s%20What%20I%20Call%20Music%2089 '
            b'duration%3A217.653 '
            b'id%3A51917 title%3AShe%E2%80%99s%20Kinda%20Hot '
            b'genre%3ANo%20Genre artist%3A5%20Seconds%20of%20Summer '
            b'album%3A'
            b'Now%20That%E2%80%99s%20What%20I%20Call%20Music!%2092 '
            b'duration%3A194.773 '
            b'count%3A2\n')
    assert [dict(id=51823,
                 title='Amnesia',
                 genre='Pop',
                 artist='5 Seconds of Summer',
                 album='Now That\'s What I Call Music 89',
                 duration=217.653),
            dict(id=51917,
                 title='She’s Kinda Hot',
                 genre='No Genre',
                 artist='5 Seconds of Summer',
                 album='Now That’s What I Call Music! 92',
                 duration=194.773),
            ] == database.tracks(tn, artist_id=8696)
    tn.write.assert_called_once_with(
            b'tracks 0 100 artist_id%3A8696 sort%3Aalbumtrack\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_tracks_default_album(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'tracks 0 100 album_id%3A3238 sort%3Aalbumtrack '
            b'id%3A46832 title%3ALittle%20Discourage genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A188.866 tracknum%3A1 '
            b'id%3A46836 title%3AI%20Don\'t%20Have%20the%20Map '
            b'genre%3ARock artist%3AIdlewild '
            b'album%3A100%20Broken%20Windows duration%3A134.626 '
            b'tracknum%3A2 '
            b'id%3A46837 title%3AThese%20Wooden%20Ideas genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A232.84 tracknum%3A3 '
            b'id%3A46838 title%3ARoseability genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A218.96 tracknum%3A4 '
            b'id%3A46839 title%3AIdea%20Track genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A193.04 tracknum%3A5 '
            b'id%3A46840 '
            b'title%3ALet%20Me%20Sleep%20(Next%20to%20the%20Mirror) '
            b'genre%3ARock artist%3AIdlewild '
            b'album%3A100%20Broken%20Windows duration%3A200.426 '
            b'tracknum%3A6 '
            b'id%3A46841 title%3AListen%20to%20What%20You\'ve%20Got '
            b'genre%3ARock artist%3AIdlewild '
            b'album%3A100%20Broken%20Windows duration%3A152.866 '
            b'tracknum%3A7 '
            b'id%3A46842 '
            b'title%3AActually%20It\'s%20Darkness genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A159.866 tracknum%3A8 '
            b'id%3A46843 title%3ARusty genre%3ARock artist%3AIdlewild '
            b'album%3A100%20Broken%20Windows duration%3A257.866 '
            b'tracknum%3A9 '
            b'id%3A46833 title%3AMistake%20Pageant genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A169.973 tracknum%3A10 '
            b'id%3A46834 title%3AQuiet%20Crown genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A201.226 tracknum%3A11 '
            b'id%3A46835 title%3AThe%20Bronze%20Medal genre%3ARock '
            b'artist%3AIdlewild album%3A100%20Broken%20Windows '
            b'duration%3A215.44 tracknum%3A12 '
            b'count%3A12\n')

    assert [
            dict(id=46832,
                 title='Little Discourage',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 tracknum=1,
                 duration=188.866),
            dict(id=46836,
                 title='I Don\'t Have the Map',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 tracknum=2,
                 duration=134.626),
            dict(id=46837,
                 title='These Wooden Ideas',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 tracknum=3,
                 duration=232.84),
            dict(id=46838,
                 title='Roseability',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 tracknum=4,
                 duration=218.96),
            dict(id=46839,
                 title='Idea Track',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 tracknum=5,
                 duration=193.04),
            dict(id=46840,
                 title='Let Me Sleep (Next to the Mirror)',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 duration=200.426,
                 tracknum=6),
            dict(id=46841,
                 title='Listen to What You\'ve Got',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 duration=152.866,
                 tracknum=7),
            dict(id=46842,
                 title='Actually It\'s Darkness',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 duration=159.866,
                 tracknum=8),
            dict(id=46843,
                 title='Rusty',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 duration=257.866,
                 tracknum=9),
            dict(id=46833,
                 title='Mistake Pageant',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 duration=169.973,
                 tracknum=10),
            dict(id=46834,
                 title='Quiet Crown',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 duration=201.226,
                 tracknum=11),
            dict(id=46835,
                 title='The Bronze Medal',
                 genre='Rock',
                 artist='Idlewild',
                 album='100 Broken Windows',
                 duration=215.44,
                 tracknum=12),
            ] == database.tracks(tn, album_id=3238)
    tn.write.assert_called_once_with(
            b'tracks 0 100 album_id%3A3238 sort%3Aalbumtrack\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_tracks_extended_track(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'tracks 0 100 track_id%3A46842 tags%3AytsplgedCa '
            b'id%3A46842 title%3AActually%20It\'s%20Darkness year%3A2000 '
            b'tracknum%3A8 artist_id%3A7919 genre_id%3A275 '
            b'album%3A100%20Broken%20Windows genre%3ARock '
            b'album_id%3A3238 duration%3A159.866 compilation%3A0 '
            b'artist%3AIdlewild '
            b'count%3A1\n')
    assert [
            dict(id=46842,
                 title='Actually It\'s Darkness',
                 year=2000,
                 tracknum=8,
                 artist_id=7919,
                 genre_id=275,
                 album='100 Broken Windows',
                 genre='Rock',
                 album_id=3238,
                 duration=159.866,
                 compilation=0,
                 artist='Idlewild'),
            ] == database.tracks(tn, track_id=46842, extended=True)
    tn.write.called_once_with(
            b'tracks 0 100 track_id%3A46842 tags%3AytsplgedCa\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_search_no_match(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = b'search 0 5 term%3Azzzzz count%3A0\n'
    assert (dict(albums={}, artists={}, tracks={})
            == database.search(tn, 'zzzzz'))
    tn.write.assert_called_once_with(b'search 0 5 term%3Azzzzz\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_search_matches_single_chunk(mocker):
    tn = mocker.MagicMock()
    tn.read_until.return_value = (
            b'search 0 5 term%3Awide '
            b'contributors_count%3A2 '
            b'contributor_id%3A8526 contributor%3AThe%20Wideboys '
            b'contributor_id%3A8873 contributor%3AWide%20Boys '
            b'albums_count%3A5 '
            b'album_id%3A3599 '
            b'album%3AMinistry%20of%20Sound%3A%20The%20Annual%202013 '
            b'album_id%3A3615 '
            b'album%3ARunning%20Trax%202014%3A%20High%20Energy '
            b'album_id%3A3616 '
            b'album%3ARunning%20Trax%202014%3A%20Warm%20Up '
            b'album_id%3A3047 '
            b'album%3ALive%20at%20Wood%20Hall%20(originals) '
            b'album_id%3A3048 album%3ASecrets%20(originals) '
            b'tracks_count%3A5 '
            b'track_id%3A44333 track%3ADeep%20%26%20Wide%20%26%20Tall '
            b'track_id%3A44352 track%3ADeep%20%26%20Wide%20%26%20Tall '
            b'track_id%3A46763 track%3AEyes%20Wide%20Open '
            b'track_id%3A46766 track%3AWidescreen '
            b'track_id%3A49610 track%3AWidecombe%20Fair '
            b'count%3A12\n')
    assert dict(
            artists={8526: 'The Wideboys', 8873: 'Wide Boys'},
            albums={
                3599: 'Ministry of Sound: The Annual 2013',
                3615: 'Running Trax 2014: High Energy',
                3616: 'Running Trax 2014: Warm Up',
                3047: 'Live at Wood Hall (originals)',
                3048: 'Secrets (originals)',
                },
            tracks={
                44333: 'Deep & Wide & Tall',
                44352: 'Deep & Wide & Tall',
                46763: 'Eyes Wide Open',
                46766: 'Widescreen',
                49610: 'Widecombe Fair',
                }
            ) == database.search(tn, 'wide')
    tn.write.assert_called_once_with(b'search 0 5 term%3Awide\n')
    tn.read_until.assert_called_once_with(b'\n')


def test_search_matches_multiple_chunks(mocker):
    tn = mocker.MagicMock()
    tn.read_until.side_effect = [
        (b' search 0 5 term%3Awide '
         b'contributors_count%3A2 '
         b'contributor_id%3A8526 contributor%3AThe%20Wideboys '
         b'contributor_id%3A8873 contributor%3AWide%20Boys '
         b'albums_count%3A12 '
         b'album_id%3A3599 '
         b'album%3AMinistry%20of%20Sound%3A%20The%20Annual%202013 '
         b'album_id%3A3615 '
         b'album%3ARunning%20Trax%202014%3A%20High%20Energy '
         b'album_id%3A3616 album%3ARunning%20Trax%202014%3A%20Warm%20Up '
         b'album_id%3A3047 album%3ALive%20at%20Wood%20Hall%20(originals) '
         b'album_id%3A3048 album%3ASecrets%20(originals) '
         b'tracks_count%3A12 '
         b'track_id%3A44333 track%3ADeep%20%26%20Wide%20%26%20Tall '
         b'track_id%3A44352 track%3ADeep%20%26%20Wide%20%26%20Tall '
         b'track_id%3A46763 track%3AEyes%20Wide%20Open '
         b'track_id%3A46766 track%3AWidescreen '
         b'track_id%3A49610 track%3AWidecombe%20Fair '
         b'count%3A26\n'),
        (b'search 5 5 term%3Awide '
         b'albums_count%3A12 '
         b'album_id%3A3065 album%3ALove '
         b'album_id%3A3067 album%3AThe%20Best%20of%20Aztec%20Camera '
         b'album_id%3A3232 album%3AHome '
         b'album_id%3A3233 '
         b'album%3A'
         b'Labours%20of%20Love%2C%20The%20Best%20of%20Hue%20and%20Cry '
         b'album_id%3A3477 '
         b'album%3ARoots%3A%20The%20Best%20of%20Show%20of%20Hands '
         b'tracks_count%3A12 '
         b'track_id%3A51650 track%3AEyes%20Wide%20Open '
         b'track_id%3A51685 track%3AWide%20Awake '
         b'track_id%3A51581 track%3AThe%20Word '
         b'track_id%3A52102 track%3AChip%20Funk%20(Original%20Mix) '
         b'track_id%3A52119 track%3APreacher%20(Radio%20Edit) '
         b'count%3A26\n'),
        (b'search 10 5 term%3Awide '
         b'albums_count%3A12 '
         b'album_id%3A3600 album%3ANY-LON%20A%20Transatlantic%20Romance '
         b'album_id%3A3603 '
         b'album%3ANow%20That\'s%20What%20I%20Call%20Music!%2083 '
         b'tracks_count%3A12 '
         b'track_id%3A44178 track%3AImmersed%20(live) '
         b'track_id%3A44193 track%3AImmersed '
         b'count%3A26\n'),
        ]
    assert dict(
        artists={
            8526: 'The Wideboys',
            8873: 'Wide Boys',
            },
        albums={
            3599: 'Ministry of Sound: The Annual 2013',
            3615: 'Running Trax 2014: High Energy',
            3616: 'Running Trax 2014: Warm Up',
            3047: 'Live at Wood Hall (originals)',
            3048: 'Secrets (originals)',
            3065: 'Love',
            3067: 'The Best of Aztec Camera',
            3232: 'Home',
            3233: 'Labours of Love, The Best of Hue and Cry',
            3477: 'Roots: The Best of Show of Hands',
            3600: 'NY-LON A Transatlantic Romance',
            3603: 'Now That\'s What I Call Music! 83',
            },
        tracks={
            44333: 'Deep & Wide & Tall',
            44352: 'Deep & Wide & Tall',
            46763: 'Eyes Wide Open',
            46766: 'Widescreen',
            49610: 'Widecombe Fair',
            51650: 'Eyes Wide Open',
            51685: 'Wide Awake',
            51581: 'The Word',
            52102: 'Chip Funk (Original Mix)',
            52119: 'Preacher (Radio Edit)',
            44178: 'Immersed (live)',
            44193: 'Immersed',
            }
        ) == database.search(tn, 'wide')
    tn.write.assert_has_calls([
            mocker.call(b'search 0 5 term%3Awide\n'),
            mocker.call(b'search 5 5 term%3Awide\n'),
            mocker.call(b'search 10 5 term%3Awide\n'),
        ])
    tn.read_until.assert_has_calls([mocker.call(b'\n'), mocker.call(b'\n')])
