import unittest
from playlist_writing import get_playlist_file_path, PLAYLIST_EXTENSION, PLAYLIST_NAME_SUFFIX


class PlaylistWritingTest(unittest.TestCase):

    def test_get_playlist_file_path(self):
        playlist_file_path = get_playlist_file_path('C:\\Daredevil\\S02')
        expected = 'C:\\Daredevil\\Daredevil S02 ' + PLAYLIST_NAME_SUFFIX + PLAYLIST_EXTENSION
        self.assertEqual(expected, playlist_file_path, 'Expected "{0}" to be equal to "{1}".'.format(playlist_file_path, expected))

if __name__ == "__main__":
    unittest.main()