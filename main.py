from pytube import YouTube
import os
import sys

def download_video(yt, path):
    video = yt.streams.get_highest_resolution()
    video.download(path)

def download_audio(yt, path):
    audio = yt.streams.filter(only_audio=True).first()
    out_file = audio.download(path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def download_video_without_audio(yt, path):
    video_without_audio = yt.streams.filter(subtype='mp4', adaptive=True).first()
    video_without_audio.download(path)

while True:
    print("|-----------------------------|")
    print("|      YOUTUBE DOWNLOADER     |")
    print("|          PROGRAM MENU       |")
    print("|  1. Download video from YT  |")
    print("|  2. Exit program            |")
    print("|-----------------------------|")

    print()
    number = input("Select option (1-2): ")
    print()

    if number == "1":
        link = input("Enter YT video link: ")
        yt = YouTube(link)

        print()
        print("|-------------------------------|")
        print("|  What do you want to download?|")
        print("|  1. Video                     |")
        print("|  2. Audio only                |")
        print("|  3. Video without audio       |")
        print("|  4. All of the above          |")
        print("|-------------------------------|")
        print()
        option = input("Enter option number (1-4): ")

        if option == "1":
            download_video(yt, './Videos')
            print("Video has been downloaded successfully")
        elif option == "2":
            download_audio(yt, './Audios')
            print("Audio has been downloaded successfully")
        elif option == "3":
            download_video_without_audio(yt, './Videos_without_audio')
            print("Video without audio has been downloaded successfully")
        elif option == "4":
            download_video(yt, './Videos')
            download_audio(yt, './Audios')
            download_video_without_audio(yt, './Videos_without_audio')
            print("Everything has been downloaded successfully")
        else:
            print("Invalid option")

    elif number == "2":
        sys.exit(0)
    else:
        print("Invalid option")

    print()
    input("Press enter to continue")
    os.system('cls')
