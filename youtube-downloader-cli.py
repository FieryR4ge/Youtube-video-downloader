#!/usr/bin/python3

import argparse
from base.youtube import YoutubeDownloader

parser = argparse.ArgumentParser(description='Youtube cli downloader')
parser.add_argument('--link', help='Youtube link to video')
parser.add_argument('--file', help='Download from all links in the file. Specify a path to file')
parser.add_argument('--audio', action='store_true', help='Download only audio track "True" or "False"')


if __name__ == '__main__':
    args = parser.parse_args()
    link = args.link
    path_to_file = args.file
    only_audio = args.audio
    youtube_downloader = YoutubeDownloader()
    if link:
        youtube_downloader.set_link(link=link)
        if only_audio:
            youtube_downloader.set_stream_only_audio()
        else:
            youtube_downloader.set_stream_highest_resolution()
        youtube_downloader.download_video()
    elif path_to_file:
        with open(path_to_file, 'r', encoding='utf-8') as links_file:
            for link in links_file:
                youtube_downloader.set_link(link)
                if only_audio:
                    youtube_downloader.set_stream_only_audio()
                else:
                    youtube_downloader.set_stream_highest_resolution()
                youtube_downloader.download_video()
    else:
        exit('Required arguments undefined. Please run the script with --help to get more information')

