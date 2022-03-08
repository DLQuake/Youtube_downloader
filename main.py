from pytube import YouTube
import os
import sys
import time

while True:
    print("|-----------------------------|")
    print("|      YOUTUBE DOWNLOADER     |")
    print("|        MENU  PROGRAMU       |")
    print("|  1. Pobierz film z youtube  |")
    print("|  2. Zamknij program         |")
    print("|-----------------------------|")

    print()
    number = input("Wybierz numer z menu (1-2): ")
    print()

    if number == "1":
        link = input("Wprowadź link filmu z Youtube: ")
        yt = YouTube(link)

        print()
        print("|-------------------------------|")
        print("|  Co chcesz uzyskać z filmu?   |")
        print("|  1. Film                      |")
        print("|  2. Tylko audio               |")
        print("|  3. Film bez audio            |")
        print("|  4. Wszystkie powyższe opcje  |")
        print("|-------------------------------|")
        print()
        rodzaj = input("Wpisz numer opcji (1-4): ")

        if rodzaj == "1":
            video = yt.streams.get_highest_resolution()
            video.download('./Filmy')

            print()
            print("Film został pobrany pomyślnie")
        elif rodzaj == "2":
            audio = yt.streams.filter(only_audio=True).first()
            out_file = audio.download('./Audio')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            print()
            print("Audio zostało pobrane pomyślnie")
        elif rodzaj == "3":
            video_without_audio = yt.streams.filter(subtype='mp4', adaptive=True).first()
            video_without_audio.download('./Filmy_bez_audio')

            print()
            print("Film bez dźwięk został pobrany pomyślnie")
        elif rodzaj == "4":
            video = yt.streams.get_highest_resolution()
            video.download('./Filmy')

            audio = yt.streams.filter(only_audio=True).first()
            out_file = audio.download('./Audio')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            video_without_audio = yt.streams.filter(subtype='mp4', adaptive=True).first()
            video_without_audio.download('./Filmy_bez_audio')

            print()
            print("Wszytko zostało pobrane pomyślnie")
        else:
            print()
            print("Nie ma takiej opcji")

    elif number == "2":
        sys.exit(0)
    else:
        print("Nie ma takiej opcji")

    print()
    print("Wciśnij enter by kontynuować")
    number = sys.stdin.read(1)
    os.system('cls')
