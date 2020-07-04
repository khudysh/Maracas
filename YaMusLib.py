# -*- coding: utf-8 -*-
import pyautogui
import time
import pyperclip
import requests
from bs4 import BeautifulSoup
from random import shuffle
import json
import os
import sys
from colorama import init, Fore, Back, Style

init()


def disMusOp(songs, n):
    DISCORD_ICON = (551, 767)
    pyautogui.moveTo(DISCORD_ICON)
    time.sleep(1)
    pyautogui.click(DISCORD_ICON)
    time.sleep(3)
    for i in range(n):
        pyautogui.typewrite(songs[i])
        pyautogui.keyDown("enter")
        time.sleep(3)


def disMus(temp, n):
    print(Fore.GREEN+Style.BRIGHT+"Okey, went to the Discord, you're have 4s"+Style.RESET_ALL)
    time.sleep(4)
    for section, commands in temp.items():
        time.sleep(2)
        for i in range(n):
            pyperclip.copy(''.join(commands[i]))
            if os.name == 'nt':
                pyautogui.hotkey('ctrl', 'v')
            else: pyautogui.hotkey('command', 'v')
            pyautogui.keyDown("enter")
            time.sleep(3)


def mainWork(response, choice):
    response.encoding = 'utf-8'

    if response.status_code == 200:
        print(Fore.GREEN+Style.BRIGHT+'Success!'+Style.RESET_ALL)
    elif response.status_code == 404:
        print(Fore.YELLOW+Style.BRIGHT+'Not Found'+Style.RESET_ALL)
    else:
        print(Fore.RED+Style.BRIGHT+'An error has occurred.')
        print(response)

    content = BeautifulSoup(response.content, "html.parser")

    artists = []
    songs = []

    if choice == "3":
        artist_name = content.find_all(class_='page-artist__title')
        song_name = content.find_all(class_='d-track__title')

        for i in artist_name:
            artists.append(i.text)

        for j in song_name:
            songs.append(j.text)

        all = ["-p " + artists[0] + " - " + songs[k] for k in range(len(song_name))]
    else:
        artist_name = content.find_all(class_='d-track__artists')
        song_name = content.find_all(class_='d-track__title')

        for i in artist_name:
            artists.append(i.text)

        for j in song_name:
            songs.append(j.text)

        all = ["-p " + artists[k] + " - " + songs[k] for k in range(len(song_name))]

    shuffleA(all)

    to_json = {'musica': all}

    with open('userMusic.json', 'w', encoding='utf-8') as f:
        json.dump(to_json, f, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))

    with open('userMusic.json', encoding='utf-8') as f:
        file_content = f.read()
        temp = json.loads(file_content)

    print("Downloaded "+Fore.YELLOW+Style.BRIGHT+str(len(songs))+Style.RESET_ALL+" songs")
    n = int(input("Amount of songs: "))

    return temp, n


def playByUser(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/users/*username*/tracks"+Style.RESET_ALL)
    user = input("Username: ")
    response = requests.get("https://music.yandex.ru/users/"+user+"/tracks")

    temp, n = mainWork(response, choice)

    disMus(temp, n)


def playByPlaylist(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/users/music-blog/playlists/*number*"+Style.RESET_ALL)
    playlist = input("Playlist number: ")
    response = requests.get("https://music.yandex.ru/users/music-blog/playlists/"+playlist)

    temp, n = mainWork(response, choice)

    disMus(temp, n)

def PlayByAlbum(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/album/*number*"+Style.RESET_ALL)
    playlist = input("Album number: ")
    response = requests.get("https://music.yandex.ru/album/"+playlist)

    temp, n = mainWork(response, choice)

    disMus(temp, n)


def playByOwn(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/users/*username*/playlists/*number*"+Style.RESET_ALL)
    user = input("Username: ")
    playlist = input("Playlist number: ")
    response = requests.get("https://music.yandex.ru/users/"+user+"/playlists/"+playlist)

    temp, n = mainWork(response, choice)

    disMus(temp, n)


def playByArtist(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/artist/*number*/tracks"+Style.RESET_ALL)
    artist = input("Artist number: ")
    response = requests.get("https://music.yandex.ru/artist/"+artist+"/tracks")

    temp, n = mainWork(response, choice)

    disMus(temp, n)


def restart():
    t = input("restart? y/n: ")
    if (t == "y"):
        os.system('cls' if os.name == 'nt' else 'clear')
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        quit()

def shuffleA(all):
    t = input("shuffle all? y/n: ")
    if (t == "y"):
        shuffle(all)

def switchMode(choice):
    if choice == "1":
        playByUser(choice)
        restart()
    elif choice == "2":
        playByPlaylist(choice)
        restart()
    elif choice == "3":
        playByArtist(choice)
        restart()
    elif choice == "4":
        playByOwn(choice)
        restart()
    elif choice == "5":
        playByAlbum(choice)
        restart()
    elif choice == "6":
        quit()
    else:
        print(Fore.RED+Style.BRIGHT+"Wrong code"+Style.RESET_ALL)
        restart()

#Daily playlist: https://music.yandex.ru/users/yamusic-daily/playlists/63562191
