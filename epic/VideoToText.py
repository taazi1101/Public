from pytube import YouTube
import time
import os
import speech_recognition as sp
import ffmpeg

start_time = time.perf_counter()

def setlink(link):
    print("Downloading video from Youtube. This might take a while...")
    video = YouTube(link)
    video.streams.filter(only_audio=True).first().download("Convtotxt", filename="link")
    print("Done")
    return "Convtotxt/link.mp4"

print("Filename type:l to use a youtube link")
in_filename = input(":")
if in_filename == "l":
    print("Link")
    link = input(":")
    uselink = True
else:
    uselink = False
    link = ""

print("Lenght per file (Max: 250) Leave empty for DEFAULT")
try:
    lenght_per = int(input(":"))
except:
    lenght_per = 200
    pass

if lenght_per > 250:
    lenght_per = 250

if uselink:
    in_filename = setlink(link)

try:
    os.makedirs('Convtotxt')
except:
    pass

command2mp3 = f"ffmpeg -i {in_filename} Convtotxt/convert.mp3"
command2wav = "ffmpeg -i Convtotxt/convert.mp3 Convtotxt/convert.wav"
os.system(command2mp3)
os.system(command2wav)
commandsplit = f"ffmpeg -i Convtotxt/convert.wav -f segment -segment_time {str(lenght_per)} -c copy Convtotxt/use%0d.wav"
os.system(commandsplit)
os.remove('Convtotxt/convert.mp3')
os.remove('Convtotxt/convert.wav')

if os.path.exists("out.txt"):
    os.remove("out.txt")

def convert_to_text(filename, output_name):
    try:
        rec = sp.Recognizer()
        with sp.AudioFile(filename) as source:
            audiodata = rec.record(source, 200)
        outfile = open(output_name, 'a')
        rec_text = rec.recognize_google(audiodata)
        outfile.write(rec_text + "\n")
    except:
        print(f"Failed {filename}")
        return
    print(f"Converted {filename}")
    return

for num in range(os.sys.maxsize**100):
    filename = f"Convtotxt/use{num}.wav"
    if os.path.exists(filename) == False:
        break
    convert_to_text(filename, "out.txt")
    os.remove(filename)

try:
    os.remove("Convtotxt/link.mp4")
except:
    pass

os.rmdir('Convtotxt')
print(f"Finished in {round(time.perf_counter()-start_time, 2)} second(s)")
input()
