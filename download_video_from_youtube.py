#!/usr/bin/python

import sys
from framework.utils.youtube_download import YoutubeDownloader


def setUp():
    global youtube_downloader

    youtube_downloader = YoutubeDownloader()

    global link
    link = str(sys.argv[1])


def download():
    youtube_downloader.download(link)


def main():
    setUp()
    download()


if __name__ == "__main__":
    main()
