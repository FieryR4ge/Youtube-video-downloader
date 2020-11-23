from pytube import YouTube


class YoutubeDownloader:
    """
    Main class to setup and download a video from youtube
    """
    def __init__(self, link):
        self.link = link
        self.youtube = YouTube(link)
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
        @return: none
        """
        self.youtube_stream = self.youtube.streams.get_highest_resolution()

    def download_video(self, output_path=None):
        """
        download video to output_path
        @param output_path:
        @return:
        """
        print("Downloading...")
        self.youtube_stream.download(output_path=output_path)
        print("Download completed.")
