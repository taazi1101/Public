import sys
import subprocess
import time

try:
    import pytube
except:
    subprocess.Popen([sys.executable, "-m", "pip", "install", "pytube"])
    import pytube


print("Video url or type:p to use a playlist")
video_url = input(":")
if video_url == "p":
    use_play = True
    print("Playlist url")
    playlist_url = input(":")
else:
    use_play = False

start = time.perf_counter()

if use_play:
    print("Opening playlist...")
    try:
        playlist = pytube.Playlist(playlist_url)
    except:
        print("Failed to open playlist. Maybe its private?")
        input()
        exit()
    print("Downloading videos from playlist...")
    for video_playurl in playlist.video_urls:
        try:
            print(f"Downloading {pytube.YouTube(video_playurl).title}")
            pytube.YouTube(video_playurl).streams.first().download("Youtube")
            print(f"Downloaded {pytube.YouTube(video_playurl).title}")
        except:
            print("Failed to download video. Maybe its private?")
            continue

else:
    try:
        print(f"Downloading {pytube.YouTube(video_url).title}")
        pytube.YouTube(video_url).streams.first().download("Youtube")
        print(f"Downloaded {pytube.YouTube(video_url).title}")
    except:
        print("Failed to download video. Maybe its private?")
        pass

input(f"Finished in {round(time.perf_counter()-start, 2)} second(s)")
