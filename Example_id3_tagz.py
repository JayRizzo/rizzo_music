"""PlaceHolder."""
import re

from os import path as ospath

from eyed3 import id3

current_home = ospath.expanduser('~')
file_path = ospath.join(current_home,
                        'Music',
                        'iTunes',
                        'iTunes Media',
                        'Music',
                        'Aerosmith',
                        'Big Ones',
                        '01 Walk On Water.mp3',
                        )


def read_id3_artist(audio_file):
    """Module to read MP3 Meta Tags.

    Accepts Path like object only.
    """
    filename = audio_file
    tag = id3.Tag()
    tag.parse(filename)
    # =========================================================================
    # Set Variables
    # =========================================================================
    artist = tag.artist
    title = tag.title
    track_path = tag.file_info.name
    # =========================================================================
    # Check Variables Values & Encode Them and substitute back-ticks
    # =========================================================================
    if artist is not None:
        artist.encode()
        artistz = re.sub(u'`', u"'", artist)
    else:
        artistz = 'Not Listed'
    if title is not None:
        title.encode()
        titlez = re.sub(u'`', u"'", title)
    else:
        titlez = 'Not Listed'
    if track_path is not None:
        track_path.encode()
        track_pathz = re.sub(u'`', u"'", track_path)
    else:
        track_pathz = ('Not Listed, and you have an the worst luck, '
                       'because this is/should not possible.')
    # =========================================================================
    # print them out
    # =========================================================================
    try:
        if artist is not None and title is not None and track_path is not None:
            print('Artist: "{}"'.format(artistz))
            print('Track : "{}"'.format(titlez))
            print('Path  : "{}"'.format(track_pathz))
    except Exception as e:
        raise e


read_id3_artist(file_path)

# Show Case:
# Artist: "Aerosmith"
# Track : "Walk On Water"
# Path  : "/Users/MyUserName/Music/iTunes/iTunes Media/Music/Aerosmith/Big Ones/01 Walk On Water.mp3"  # noqa
