from urllib.parse import urljoin
from urllib.request import pathname2url


# Global variables
PLAYLIST_EXTENSION = ".xspf"
PLAYLIST_NAME_SUFFIX = " (follow-up)"


def write_playlist(i_folder_absolute_path: str):
    """
        Creates the playlist containing all the elements which are in the provided folder.

        Args:
            i_folder_absolute_path : The absolute path of the folder.
    """

    pass


def get_playlist_file_path(i_folder_absolute_path: str) -> str:
    """
        Returns the playlist file name.

        Args:
            i_folder_absolute_path : The absolute path of the folder in which the elements of the playlist
                                    are contained.
    """

    folders = i_folder_absolute_path.split('\\')
    playlist_file_name_components = folders[-2:]
    playlist_file_name = ' '.join(playlist_file_name_components) + PLAYLIST_NAME_SUFFIX + PLAYLIST_EXTENSION
    return i_folder_absolute_path.rsplit('\\', 1)[0] + '\\' + playlist_file_name


def get_file_absolute_path_from_playlist_element(i_element_absolute_file_path: str) -> str:
    """
        Returns the absolute path of the element which can be understood by the FILE protocol.

        Args:
            i_element_absolute_file_path : The absolute path of the playlist element.
    """

    return urljoin('file:', pathname2url(i_element_absolute_file_path))


def write_playlist_start(i_playlist_file_descriptor: object):
    """
        Writes the beginning of the XSPF file.

        Args:
            i_playlist_file_descriptor : The file descriptor on the absolute path of the XSPF playlist file.
    """

    with i_playlist_file_descriptor as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/"' +
                ' version="1">\n')
        title = i_playlist_file_descriptor.name.split('\\')[-1].replace(PLAYLIST_EXTENSION, '')
        f.write("\t<title>{0}</title>\n".format(title))
        f.write("\t<trackList>\n")


def write_playlist_element(i_playlist_file_descriptor: object, i_idx: int, i_element_absolute_path: str):
    """
        Adds the element in the XSPF playlist file.

        Args:
            i_playlist_file_descriptor  : The file descriptor on the absolute path of the XSPF playlist file.
            i_idx                       : The position of the element.
            i_element_absolute_path     : The absolute path of the element.
    """

    with i_playlist_file_descriptor as f:
        f.write("\t\t<track>\n")
        f.write("\t\t\t<location>{0}</location>".format(
            get_file_absolute_path_from_playlist_element(i_element_absolute_path))
        )
        f.write("\t\t\t<title>{0}</title>".format(
            # get title from file
        ))
        f.write("\t\t\t<duration>{0}</duration>".format(
            # get file duration
        ))
        f.write('\t\t\t<extension application="http://www.videolan.org/vlc/playlist/0">')
        f.write("\t\t\t\t<vlc:id>{0}</vlc:id>".format(i_idx))
        f.write('\t\t\t</extension>')
        f.write("\t\t</track>\n")


def write_playlist_end(i_playlist_file_descriptor: object, i_nb_elts: int):
    """
        Writes the end of the XSPF file.

        Args:
            i_playlist_file_descriptor  : The file descriptor on the absolute path of the XSPF playlist file.
            i_nb_elts                   : The number of elements which have been reported in the playlist.
    """

    with i_playlist_file_descriptor as f:
        f.write('\t<extension application="http://www.videolan.org/vlc/playlist/0">\n')
        for i in range(i_nb_elts):
            f.write('\t\t<vlc:item tid="' + i + '"/>\n')
        f.write("\t</extension>\n")
        f.write("</playlist>\n")