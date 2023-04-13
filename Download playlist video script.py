import os
import pytube
import requests
import re
import pyfiglet
import time
import webbrowser
logo = pyfiglet.figlet_format("Download Videos By Ghalwash")
print(logo)
print("")


choice = input("What do you want to do?\n1) Open developer accounts\n2) Run script\n")


if choice == "1":
        webbrowser.open("http://t.me/mrfa0gh")
        webbrowser.open("https://www.instagram.com/mrfa0gh")
        webbrowser.open('https://twitter.com/mrfa0gh')
 
elif choice == "2":
        print("Script is running...")
else:
        print("Invalid choice.")

# Ask the user for the playlist link
playlist_link = input("Please enter the link to the YouTube playlist: ")

# Create a YouTube playlist object using the link
playlist = pytube.Playlist(playlist_link)

# Set initial counters
num_videos = len(playlist.video_urls)
downloaded_count = 0
not_downloaded_count = 0

# Loop through each video in the playlist and download the video
start_time = time.time()
for video in playlist.videos:
    try:
        # Get the highest quality video stream
        stream = video.streams.get_highest_resolution()
        print(f"Downloading {video.title}...")
        download_path = stream.download()
        downloaded_count += 1
        print(f"Downloaded {video.title} to {os.path.abspath(download_path)}")
    except:
        print(f"Couldn't download {video.title}")
        not_downloaded_count += 1

# Print summary of download
end_time = time.time()
total_time = end_time - start_time
print(f"\nDownload playlist Done")
print(f"Number of videos in playlist: {num_videos}")
print(f"Number of videos downloaded: {downloaded_count}")
print(f"Number of videos not downloaded: {not_downloaded_count}")
print(f"Total time taken: {total_time:.2f} seconds")
print(f"Playlist downloaded to: {os.path.dirname(os.path.abspath(download_path))}")
