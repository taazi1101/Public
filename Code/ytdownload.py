import pytube, os, time

def downl(name):
    try:
        yt = pytube.YouTube(name)
        video = yt.streams.get_highest_resolution()
        title = str(video.title)
    except:
        print("Error opening video")
        return
    print("Downloading...")
    try:
        video.download("./", title.replace(" ", "_"))
    except:
        print("Error downloading.")
        return

def downl_playlist(name):
    try:
        plist = pytube.Playlist(name)
        pl_name = str(plist.title).replace(" ","_").replace(".","").replace("!","").replace("?","").replace("'","").replace('"',"").replace("(","").replace(")","").replace("[","").replace("]","")
    except:
        print("Error opening playlist")
        return
    try:
        if os.path.isdir(pl_name) == False:
            os.mkdir(pl_name)
        _, _, filenames = next(os.walk(pl_name))
    except:
        print("Error creating directory")
        return
    for yt_url in plist.video_urls:
        try:
            yt = pytube.YouTube(yt_url)
            video_tl = str(yt.title).replace(" ","_").replace(".","").replace("!","").replace("?","").replace("'","").replace('"',"").replace("(","").replace(")","").replace("[","").replace("]","")
            if video_tl + ".mp4" in filenames:
                print(f"{video_tl} Already exists")
                continue
            else:
                print(video_tl,end="")
                video = yt.streams.get_highest_resolution()
                video.download(f"{pl_name}/",video_tl)
                print(" ☑")
        except:
            print(" ☒")
            continue

start_time = time.perf_counter()
if "-p" == os.sys.argv[1]:
    downl_playlist(os.sys.argv[2])
else:
    downl(os.sys.argv[1])
print(f"Completed in {round(time.perf_counter()-start_time,1)}")