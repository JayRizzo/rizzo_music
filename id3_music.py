#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module Has Been Built to read MP3 Meta Tags & Hidden Mac Attributes."""
# How to get extended MacOS attributes of a file using python?
# Research \/
# https://stackoverflow.com/a/33182025/1896134
# http://hints.macworld.com/article.php?story=20101206161739274
# https://stackoverflow.com/a/19550814/1896134
# =============================================================================
import csv
import re
from os import path
from os import walk

from time import strftime

import biplist

from eyed3 import id3
from eyed3 import log

import xattr
# Helpful if you want to ignore errors.
# https://stackoverflow.com/a/25614061/1896134
# https://stackoverflow.com/a/39316798/1896134
# log.setLevel("ERROR")
log.setLevel("INFO")

# from tinytag import TinyTag
# from tinytag import TinyTagException


def _now():
    """The Module Returns "Current Time" As A Formatted String."""
    ymd = str(strftime('%Y%m%d_%H%M%S'))
    return ymd


current_home = path.expanduser('~')
new_file = (current_home + '/Desktop/testin_' + _now() + '.csv')
includes_file_extensn = (".mp3", ".m4a", ".flac", ".alac", ".aif", ".aiff")
search_dir = path.join(current_home, 'Music')
# search_dir = path.join('/Volumes', 'Muisikk', 'iTunes', 'iTunes Media')
print(search_dir)
tracks = []


def locate_files():
    """THE MODULE HAS BEEN BUILD FOR Locating YOUR FILES."""
    filelocated = ''
    for dirpath, dirnames, filenames in walk(search_dir, topdown=False):
        for name in filenames:
            if name.lower().endswith(includes_file_extensn):
                filelocated = path.join(str(dirpath) + '/' +
                                        str(name))
                read_id3_artist(filelocated)
                # print("{a} Track Names Begin {a}".format(a='=' * 35))
                # tracks.append(name)
                # print("Track So Far: {}".format(tracks))
                # print("{a} Track Names END {a}".format(a='=' * 35))
                # print('Files found: ' + str(filelocated))
                # print("\n\n# {} Song ID3Tags Start {} \n {}"
                #       .format("=" * 30, "=" * 30,
                #               read_id3_artist(filelocated)))
                #               # read_id3_info(filelocated)))
                # print("\n\n# {} Song ID3Tags End {} \n"
                #       .format("=" * 30, "=" * 30))

                print("{} Song Meta Start {}".format('=' * 35, '=' * 35))

                try:
                    x = xattr.xattr(filelocated)
                    print("{}".format(x.items()))
                    y = biplist.readPlistFromString(
                        x.get('com.apple.metadata:kMDItemWhereFroms'))
                    print("com.apple.metadata:ItemWhereFroms: {}".format(y))
                except Exception as e:
                    print("Custom Error: {}".format(e))
                    # print("{}".format(e.errno))
                    # print("{}".format(e.filename))
                    # print("{}".format(e.strerror))
                else:
                    pass
                    # print("Failed To find attr: kMDItemWhereFroms")
                finally:
                    # print("Completed: {}".format(y))
                    pass
                print("{} Song Meta END {}".format('=' * 35, '=' * 35))
                print("\n\n\n\n\n\n\n\n")
                pass
            else:
                print("{} Ignored.".format(name))
                pass
    return filelocated


with open(new_file, 'w', newline='') as csvfile:
    fieldnames = ['Artist', 'Tracks', 'Path']
    stuff_to_write = csv.DictWriter(csvfile, fieldnames=fieldnames)
    stuff_to_write.writeheader()


def read_id3_artist(filename):
    """Module to read MP3 Meta Tags."""
    filename = filename
    filename.encode()
    tag = id3.Tag()
    tag.parse(filename)
    # print("Artist: \"{}\" Track: \"{}\"".format(tag.artist, tag.title))

    artist = tag.artist
    title = tag.title
    track_path = filename

    if artist is not None:
        artist.encode()
        artist = re.sub(u'`', u"'", artist)
    if title is not None:
        title.encode()
        title = re.sub(u'`', u"'", title)
    if track_path is not None:
        track_path.encode()
        track_path = re.sub(u'`', u"'", track_path)

    with open(new_file, 'a', newline='') as csvfile:
        stuff_to_write = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)
        stuff_to_write.writerow([artist, title, track_path])


def read_id3_info(filename):
    """Module to read MP3 Meta Tags."""
    tag = id3.Tag()
    tag.parse(filename)
    print("Tag Version: {}\n"
          "Artist: {}\n"
          "Album: {}\n"
          "Album Artist: {}\n"
          "Album Type: {}"
          .format(tag.version,
                  tag.artist,
                  tag.album,
                  tag.album_artist,
                  tag.album_type,
                  ))
    print("Version: {}".format(tag.version))
    print("Title: {}".format(tag.title))
    print("Track Num: {}".format(tag.track_num))
    print("Artist Origin: {}".format(tag.artist_origin))
    print("Artist Url: {}".format(tag.artist_url))
    print("Audio File Url: {}".format(tag.audio_file_url))
    print("Audio Source Url: {}".format(tag.audio_source_url))
    print("GetBestDate: {}".format(tag.getBestDate()))
    print("Bpm: {}".format(tag.bpm))
    print("Cd Id: {}".format(tag.cd_id))
    # print("Chapters: {}".format(tag.chapters))
    # print("Clear: {}".format(tag.clear))
    # print("Comments: {}".format(tag.comments))
    print("Commercial Url: {}".format(tag.commercial_url))
    print("Composer: {}".format(tag.composer))
    print("Copyright Url: {}".format(tag.copyright_url))
    print("Disc Num: {}".format(tag.disc_num))
    print("Encoding Date: {}".format(tag.encoding_date))
    # print("File Info: {}".format(tag.file_info))
    print("File Info Name: {}".format(tag.file_info.name))
    print("File Info Tag Padding Size: {}".format(tag.file_info.tag_padding_size))  # noqa
    print("File Info Tag Size: {}".format(tag.file_info.tag_size))

    # for key, value in sorted(tag.frame_set.items(), key=lambda x: x[1]):
    #     print("{} : {}".format(key, value))
    # print("Frameiter: {}".format(tag.frameiter))
    if tag.genre is not None and tag.genre.id is not None:
        if tag.genre.id is not None:
            print("Genre ID: {}".format(tag.genre.id))
        if tag.genre.name is not None:
            print("Genre: {}".format(tag.genre.name))

    if tag.getBestDate() is not None:
        print("GetBestDate: {}-{}-{} {}-{}-{}"
              .format(tag.getBestDate().year,
                      tag.getBestDate().month,
                      tag.getBestDate().day,
                      tag.getBestDate().hour,
                      tag.getBestDate().minute,
                      tag.getBestDate().second
                      )
              )

    print("GetTextFrame: {}".format(tag.getTextFrame))
    print("Header - Experimental: {}".format(tag.header.experimental))
    print("Header - extended: {}".format(tag.header.extended))
    print("Header - footer: {}".format(tag.header.footer))
    print("Header - version: {}".format(tag.header.version))
    print("Header - major_version: {}".format(tag.header.major_version))
    print("Header - minor_version: {}".format(tag.header.minor_version))
    print("Header - rev_version: {}".format(tag.header.rev_version))
    print("Header - render: {}".format(tag.header.render()))
    print("Header - tag_size: {}".format(tag.header.tag_size))
    print("Header - unsync: {}".format(tag.header.unsync))
    # print("Header - parse: {}".format(tag.header.parse()))
    # print("Header - clear: {}".format(tag.header.clear))

    # print("Images: {}".format(tag.images))
    print("Internet Radio Url: {}".format(tag.internet_radio_url))
    print("IsV1: {}".format(tag.isV1()))
    print("IsV2: {}".format(tag.isV2()))
    # print("Lyrics: {}".format(tag.lyrics))
    print("Non Std Genre: {}".format(tag.non_std_genre))
    # print("Objects: {}".format(tag.objects))
    print("Original Release Date: {}".format(tag.original_release_date))
    print("Parse: {}".format(tag.parse(tag.file_info.name)))
    print("Payment Url: {}".format(tag.payment_url))
    print("Play Count: {}".format(tag.play_count))
    # print("Popularities: {}".format(tag.popularities))
    # print("Privates: {}".format(tag.privates))
    print("Publisher: {}".format(tag.publisher))
    print("Publisher Url: {}".format(tag.publisher_url))
    print("Read Only: {}".format(tag.read_only))
    print("Recording Date: {}".format(tag.recording_date))
    print("Release Date: {}".format(tag.release_date))
    # print("Remove: {}".format(tag.remove))
    # print("Save: {}".format(tag.save))
    # print("SetTextFrame: {}".format(tag.setTextFrame))
    # print("Table Of Contents: {}".format(tag.table_of_contents))
    print("Tagging Date: {}".format(tag.tagging_date))
    print("Terms Of Use: {}".format(tag.terms_of_use))
    # print("Unique File Ids: {}".format(tag.unique_file_ids))
    # print("User Text Frames: {}".format(tag.user_text_frames))
    # print("User Url Frames: {}".format(tag.user_url_frames))
    print("{} Extended Header Start {}".format('=' * 35, '=' * 35))
    print("Extended Header CRC: {}".format(tag.extended_header.crc))
    print("Extended Header CRC Bit: {}".format(tag.extended_header.crc_bit))
    print("Extended Header image Enc Restriction: {}".format(tag.extended_header.image_enc_restriction))  # noqa
    print("Extended Header image Enc Restriction Description: {}".format(tag.extended_header.image_enc_restriction_description))  # noqa
    print("Extended Header image Size Restriction: {}".format(tag.extended_header.image_size_restriction))  # noqa
    print("Extended Header image Size Restriction Description: {}".format(tag.extended_header.image_size_restriction_description))  # noqa
    # print("Extended Header parse: {}".format(tag.extended_header.parse()))
    # # TypeError: parse() missing 2 required positional arguments: 'fp' and 'version'  # noqa
    # print("Extended Header render: {}".format(tag.extended_header.render))
    # # TypeError: render() missing 2 required positional arguments: 'version' and 'frame_data'  # noqa
    print("Extended Header restrictions Bit: {}".format(tag.extended_header.restrictions_bit))  # noqa
    print("Extended Header size: {}".format(tag.extended_header.size))  # noqa
    print("Extended Header tag Size Restriction: {}".format(tag.extended_header.tag_size_restriction))  # noqa
    print("Extended Header tag Size Restriction Description: {}".format(tag.extended_header.tag_size_restriction_description))  # noqa
    print("Extended Header text Enc Restriction: {}".format(tag.extended_header.text_enc_restriction))  # noqa
    print("Extended Header text Enc Restriction Description: {}".format(tag.extended_header.text_enc_restriction_description))  # noqa
    print("Extended Header text Length Restriction: {}".format(tag.extended_header.text_length_restriction))  # noqa
    print("Extended Header text Length Restriction Description: {}".format(tag.extended_header.text_length_restriction_description))  # noqa
    print("Extended Header update Bit: {}".format(tag.extended_header.update_bit))  # noqa
    print("{} Extended Header End {}".format('=' * 35, '=' * 35))
    print("")
    return


def checkthings(filename):
    """Module to Verify MP3 Meta Tags."""
    tag = id3.Tag()
    tag.parse(filename)
    test_version = ("Valid Tag Format: {}".format(id3.isValidVersion(tag.version)))  # noqa
    print(test_version)
    return id3.isValidVersion(tag.version)


def pushtocsv():
    """Module to Write MP3 Meta Info To CSV."""
    csv.register_dialect('pipes', delimiter='|')
    f = open(_now() + '_taglist.csv', 'w')

    writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    with f:
        writer = csv.writer(f, dialect="dapiper")
        writer.writerow(("pens", 4))
        writer.writerow(("plates", 2))
        writer.writerow(("bottles", 4))
        writer.writerow(("cups", 1))


def write_xattr_tags(file_path, tags):
    """THE MODULE HAS BEEN BUILD FOR writePlistToString."""
    bpl_tags = biplist.writePlistToString(tags)
    optional_tag = "com.apple.metadata:"
    map(lambda a: xattr.setxattr(file_path, optional_tag + a, bpl_tags),
        ["kMDItemFinderComment", "_kMDItemUserTags", "kMDItemOMUserTags"])
    return 'Updated xattr'


if __name__ == '__main__':
    locate_files()

    # read_id3_info(filename)
    # read_id3_info(filename2)

    # checkthings(filename)
    # checkthings(filename2)
