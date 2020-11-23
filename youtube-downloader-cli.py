#!/usr/bin/python3

import argparse

from base.youtube import YoutubeDownloader

parser = argparse.ArgumentParser(description='Youtube cli downloader')
parser.add_argument('--link', dest='link', help='youtube link to video')


if __name__ == '__main__':
    args = parser.parse_args()
    link = args.link
    if link is None:
        exit('Required argument "link" is undefined. Please run the script with --help to get more information')
    youtube_downloader = YoutubeDownloader(link=link)
    video_info = youtube_downloader.get_video_info()
    print(video_info)
    youtube_downloader.set_stream_highest_resolution()
    youtube_downloader.download_video()
