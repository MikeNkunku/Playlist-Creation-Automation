import unittest
from os import remove
from tempfile import gettempdir
from playlist_writing import *


class PlaylistWritingTest(unittest.TestCase):

    TV_SERIES_FOLDER = 'C:\\Daredevil\\S02'

    def assertFileContains(self, i_file_to_read_descriptor, i_string_to_look):
        """
            Returns whether the element was found.

            i_file_to_read_descriptor : File descriptor for the element to read
            i_string_to_look          : The String to look for
        """

        found = False
        with open(i_file_to_read_descriptor.name, mode='r') as fp:
            for line in fp.readlines():
                if line.find(i_string_to_look) != -1:
                    found = True
            fp.close()
            return found


    def test_get_playlist_file_path(self):
        playlist_file_path = get_playlist_file_path(self.TV_SERIES_FOLDER)
        expected = 'C:\\Daredevil\\Daredevil S02' + PLAYLIST_NAME_SUFFIX + PLAYLIST_EXTENSION
        self.assertEqual(expected, playlist_file_path, 'Expected "{0}" to be equal to "{1}".'.format(playlist_file_path, expected))


    def test_get_file_absolute_path_from_playlist_element(self):
        file_protocol_element_path = get_file_absolute_path_from_playlist_element(self.TV_SERIES_FOLDER + '\\' + 'Daredevil S02E01.mkv')
        expected = 'file:///C:/Daredevil/S02/Daredevil%20S02E01.mkv'
        self.assertEqual(expected, file_protocol_element_path, 'Expected "{0}" to be equal to "{1}".'.format(file_protocol_element_path, expected))


    def test_write_playlist_start(self):
        filePath = get_playlist_file_path(gettempdir())
        with open(filePath, mode='w+b') as f:
            write_playlist_start(f)
            for expected_elt in ['<?xml', '<playlist xmlns="', '<title>', '<trackList>']:
                self.assertTrue(self.assertFileContains(f, expected_elt))

        remove(filePath)


if __name__ == "__main__":
    unittest.main()