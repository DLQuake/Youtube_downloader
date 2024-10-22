import os
import sys
import yt_dlp


def download_video(yt_url, path):
    ydl_opts = {
        'format': 'bestvideo[height<=1080][fps>=24][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][fps>=24][ext=mp4]',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])


def download_audio(yt_url, path):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

    # Rename to .mp3
    for file in os.listdir(path):
        if file.endswith(".m4a"):
            base = os.path.splitext(file)[0]
            new_file = os.path.join(path, base + '.mp3')
            os.rename(os.path.join(path, file), new_file)


def download_video_without_audio(yt_url, path):
    ydl_opts = {
        'format': 'bestvideo[height<=1080][fps>=24][ext=mp4]',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


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
            create_directory('./Files/Videos')
            download_video(link, './Files/Videos')
            print()
            print("Video has been downloaded successfully")
        elif option == "2":
            create_directory('./Files/Audios')
            download_audio(link, './Files/Audios')
            print()
            print("Audio has been downloaded successfully")
        elif option == "3":
            create_directory('./Files/Videos_without_audio')
            download_video_without_audio(link, './Files/Videos_without_audio')
            print()
            print("Video without audio has been downloaded successfully")
        elif option == "4":
            create_directory('./Files/Videos')
            create_directory('./Files/Audios')
            create_directory('./Files/Videos_without_audio')
            download_video(link, './Files/Videos')
            download_audio(link, './Files/Audios')
            download_video_without_audio(link, './Files/Videos_without_audio')
            print()
            print("Everything has been downloaded successfully")
        else:
            print("Invalid option")

    elif number == "2":
        sys.exit(0)
    else:
        print("Invalid option")

    input("Press enter to continue")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
