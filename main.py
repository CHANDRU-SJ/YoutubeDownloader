"""
    module for youtube video download
"""

import os
from pytube import YouTube
from datetime import timedelta


def convertTimestamp(seconds: int) -> timedelta:
    """
        convert seconds into timestamp
        :param seconds: int
        :return timedelta
    """
    return timedelta(seconds= seconds)

def downloadVideo(link: str) -> None:
    """
        download video using url
        :param link: str
    """

    # define a path to store the downloaded video
    curr_dir = os.getcwd()
    savePath = os.path.join(curr_dir, "download")

    try:
        youtubeObj = YouTube(link)

        streams = youtubeObj.streams.filter(progressive='True', file_extension='mp4', res='360p')
        
        # asking the video number want to be download
        for number, stream in enumerate(streams, start=1):
            print(f" {number} for {stream.filesize_mb} MB")

        user_option = int(input("Enter the Number for your video to download: "))

        stream = streams[user_option - 1]

        print("Download Starting...")
        stream.download(output_path=savePath)

    # handling index error and not converted to int error
    except (IndexError, ValueError): 
        print("Enter correct number..")
    except Exception as err:
        print("Connection Error..", err)

    else:
        print(f"""Downloaded Successfully..
            Video Size: {stream.filesize_mb} MB
            Video Length:  {convertTimestamp(seconds = youtubeObj.length)}
        """)

# link = 'https://www.youtube.com/watch?v=CG12hJ3s6KI'
link = input("Enter a link you want to download: ")

downloadVideo(link=link)