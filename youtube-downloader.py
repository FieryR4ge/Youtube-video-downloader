from base.youtube import YoutubeDownloader


if __name__ == '__main__':
    link = input("Enter the link: ")
    youtube_downloader = YoutubeDownloader()
    youtube_downloader.set_link(link=link)
    youtube_downloader.set_stream_highest_resolution()
    youtube_downloader.download_video()
