from base.youtube import YoutubeDownloader

link = input("Enter the link: ")
youtube_downloader = YoutubeDownloader(link=link)
youtube_downloader.set_stream_highest_resolution()
info = youtube_downloader.get_video_info()
print(info)
youtube_downloader.download_video()