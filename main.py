from pytube import YouTube


def on_progress(video_stream, chunk, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_complete = round(bytes_downloaded / total_size * 100)
    # Progress Bar:
    print("\r" + "▌" * percent_complete + "-" * (100 - percent_complete) + " {}%".format(percent_complete), end='')


"""
User Inputs:
1. Set the Youtube link
2. Set the desired resolution, e.g.: '360p', '480p', '720p', '1080p', etc
3. Specify the destination folder
"""

link = ''
desired_resolution = '720p'
destination_folder = 'C:/Users/User/Downloads'

yt_object = YouTube(link, on_progress_callback=on_progress)
file_to_download = yt_object.streams.get_by_resolution(desired_resolution)

# Video information:
print('Title:', yt_object.title)
print('File Size:', file_to_download.filesize_mb, 'MB')

# Execute the line below if you want to download it:
file_to_download.download(destination_folder)
