from urllib.error import HTTPError
from pytube import YouTube
from termcolor import cprint
import logging.config
from logs.logging_config import log_config

logging.config.dictConfig(log_config)
stream_logger = logging.getLogger('stream_logger')
file_logger = logging.getLogger('file_logger')


class YoutubeDownloader:
    """
    Main class to setup and download a video from youtube
    """

    def __init__(self):
        self.link = None
        self.youtube = None
        self.youtube_stream = None

    def get_video_info(self):
        """
        get a common information about video
        @return: str
        """
        return (f"Title: {self.youtube.title}\n"
                f"Number of views: {self.youtube.views}"
                f"Length of video: {self.youtube.length} seconds"
                f"Description: {self.youtube.description}"
                f"Ratings: {self.youtube.rating}")

    def set_link(self, link):
        self.link = link
        self.youtube = YouTube(link)

    def set_stream_by_resolution(self, resolution='720p'):
        """
        set up resolution
        @param resolution: Video resolution i.e. "720p", "480p", "360p", "240p", "144p"
        @return: none
        """
        self.youtube_stream = self.youtube.streams.get_by_resolution(resolution=resolution)

    def set_stream_highest_resolution(self):
        """
        set up a stream with highest resolution
        @return: None
        """
        self.youtube_stream = self.youtube.streams.get_highest_resolution()

    def set_stream_only_audio(self):
        """
        set up a stream with just audio
        @return: None
        """
        self.youtube_stream = self.youtube.streams.get_audio_only()

    def download_video(self, output_path=None):
        """
        download video to output_path
        @param output_path:
        @return:
        """
        print(f'Downloading "{self.youtube.title}", link: {self.link}')
        try:
            self.youtube_stream.download(output_path=output_path)
            cprint(f"SUCCESS -- {self.youtube.title} {self.link}", color='green')
        except HTTPError:
            cprint(f"FAILED -- {self.youtube.title} {self.link}", color='red')
            file_logger.exception(f"An error occurred while downloading the file {self.youtube.title},"
                                  f" link {self.link}")
