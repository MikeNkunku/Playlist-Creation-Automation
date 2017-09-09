import unittest
from playlist_writing import *


class PlaylistWritingTest(unittest.TestCase):

    TV_SERIES_FOLDER = 'C:\\Daredevil\\S02'


    def test_get_playlist_file_path(self):
        playlist_file_path = get_playlist_file_path(self.TV_SERIES_FOLDER)
        expected = 'C:\\Daredevil\\Daredevil S02' + PLAYLIST_NAME_SUFFIX + PLAYLIST_EXTENSION
        self.assertEqual(expected, playlist_file_path, 'Expected "{0}" to be equal to "{1}".'.format(playlist_file_path, expected))


    def test_get_file_absolute_path_from_playlist_element(self):
        file_protocol_element_path = get_file_absolute_path_from_playlist_element(self.TV_SERIES_FOLDER + '\\' + 'Daredevil S02E01.mkv')
        expected = 'file:///C:/Daredevil/S02/Daredevil%20S02E01.mkv'
        self.assertEqual(expected, file_protocol_element_path, 'Expected "{0}" to be equal to "{1}".'.format(file_protocol_element_path, expected))
    
if __name__ == "__main__":
    unittest.main()