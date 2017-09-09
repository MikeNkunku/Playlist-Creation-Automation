from string import join, rsplit
from urlparse import urljoin
from urllib import pathname2url


# Global variables
PLAYLIST_EXTENSION = '.xspf'
PLAYLIST_NAME_SUFFIX = ' (follow-up)'


def get_playlist_file_path(i_folder_absolute_path):
    '''
    Returns the playlist file name.
    i_folder_absolute_path : The absolute path of the folder in which the elements of the playlist are contained.
    '''
    folders = i_folder_absolute_path.split('\\')
    playlist_file_name_components = folders[-2:]
    playlist_file_name = join(playlist_file_name_components, " ") + PLAYLIST_NAME_SUFFIX + PLAYLIST_EXTENSION
    return rsplit(i_folder_absolute_path, '\\', 1)[0] + '\\' + playlist_file_name


def get_file_absolute_path_from_playlist_element(i_element_absolute_file_path):
    '''
    Returns the absolute path of the element which can be understood by the FILE protocol.
    i_element_absolute_file_path : The absolute path of the playlist element.
    '''
    return urljoin('file:', pathname2url(i_element_absolute_file_path))


def write_playlist_start(i_playlist_file_descriptor):
    '''
    Writes the beginning of the XSPF file.
    i_playlist_file_descriptor : The file descriptor on the absolute path of the XSPF playlist file. 
    '''
    with i_playlist_file_descriptor as f :
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">\n')
        title = i_playlist_file_descriptor.name.split('\\')[-1].replace(PLAYLIST_EXTENSION, '')
        f.write('\t<title>{0}</title>\n'.format(title))
        f.write('\t\t<trackList>\n')


def write_playlist_element(i_playlist_file_path, i_idx, i_element_absolute_path):
    '''
    Adds the element in the XSPF playlist file.
    i_playlist_file_path : The absolute path of the XSPF playlist file.
    i_idx : The position of the element.
    i_element_absolute_path : The absolute path of the element.
    '''
    pass


def write_playlist_end(i_playlist_file_path):
    '''
    Writes the end of the XSPF file.
    i_playlist_file_path : The absolute path of the XSPF playlist file.
    '''
    pass