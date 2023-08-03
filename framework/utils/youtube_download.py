"""Youtube download utility."""

from abc import ABC
from pytube import YouTube


class YoutubeDownloader(ABC):
    def __init__(self, ):
        """
        Initializes a new YoutubeDownloader instance.
        """

        
    def download(self, link):
        """
        Downloads videos from Youtube link.

        :param link: Youtube video link.
        """

        youtube = YouTube(link)
        youtube = youtube.streams.get_highest_resolution()
        try:
            youtube.download()
        except:
            print("An error has occurred")
