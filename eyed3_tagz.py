"""The Module Has Been Built to read MP3 Meta Tags & Hidden Mac Attributes."""
import re
from os import path
from os import walk

from eyed3 import id3


def locate_files():
    """THE MODULE HAS BEEN BUILD FOR Locating YOUR FILES."""
    current_home = path.expanduser('~')
    includes_file_extensn = (".mp3", ".m4a", ".flac", ".alac", ".aiff")
    search_dir = path.join(current_home, 'Music')
    print("Searching Directory: {}".format(search_dir))
    for dirpath, dirnames, filenames in walk(search_dir, topdown=False):
        for name in filenames:
            if name.lower().endswith(includes_file_extensn):
                filelocated = path.join(str(dirpath) + '/' +
                                        str(name))
                print("# {} Song Meta Start {}".format('=' * 34, '=' * 34))
                read_id3_artist(filelocated)
                print("# {} Song Meta END {}".format('=' * 34, '=' * 34))


def read_id3_artist(filename):
    """Module to read MP3 Meta Tags."""
    filename = filename
    filename.encode()
    tag = id3.Tag()
    tag.parse(filename)
    artist = tag.artist
    if artist is not None:
        artist.encode()
        artist = re.sub(u'`', u"'", artist)
        print("Artist: {}".format(artist.encode()))
    title = tag.title
    if title is not None:
        title.encode()
        title = re.sub(u'`', u"'", title)
        print("title: {}".format(title.encode()))
    track_path = filename
    if track_path is not None:
        track_path.encode()
        track_path = re.sub(u'`', u"'", track_path)
        print("Track Path: {}".format(track_path.encode()))
    duration = tag.duration
    if duration is not None:
        duration.encode()
        duration = re.sub(u'`', u"'", duration)
        print("Duration: {}".format(duration.encode()))
    return


if __name__ == '__main__':
    locate_files()


filename = '~/Music/test/t154.mp3'
filename.encode()
tag = id3.Tag()
tag.parse(filename)
tag.isV1()
tag.isV2()

artist = tag.artist
if artist is not None:
    artist.encode()
    artist = re.sub(u'`', u"'", artist)
    print("Artist: {}".format(artist.encode()))
title = tag.title
if title is not None:
    title.encode()
    title = re.sub(u'`', u"'", title)
    print("title: {}".format(title.encode()))
track_path = filename
if track_path is not None:
    track_path.encode()
    track_path = re.sub(u'`', u"'", track_path)
    print("Track Path: {}".format(track_path.encode()))
duration = tag.duration
if duration is not None:
    duration.encode()
    duration = re.sub(u'`', u"'", duration)
    print("Duration: {}".format(duration.encode()))
