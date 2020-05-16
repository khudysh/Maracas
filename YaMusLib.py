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


def DisMusOp(songs, n):
    DISCORD_ICON = (551, 767)
    pyautogui.moveTo(DISCORD_ICON)
    time.sleep(1)
    pyautogui.click(DISCORD_ICON)
    time.sleep(3)
    for i in range(n):
        pyautogui.typewrite(songs[i])
        pyautogui.keyDown("enter")
        time.sleep(3)


def DisMus(temp, n):
    print(Fore.GREEN+Style.BRIGHT+"Okey, went to the Discord, you're have 4s"+Style.RESET_ALL)
    time.sleep(4)
    for section, commands in temp.items():
        time.sleep(2)
        for i in range(n):
            pyperclip.copy(''.join(commands[i]))
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.keyDown("enter")
            time.sleep(3)


def MainWork(response, choice):
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

    shuffle(all)

    to_json = {'musica': all}

    with open('userMusic.json', 'w', encoding='utf-8') as f:
        json.dump(to_json, f, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))

    with open('userMusic.json', encoding='utf-8') as f:
        file_content = f.read()
        temp = json.loads(file_content)

    print("Downloaded "+Fore.YELLOW+Style.BRIGHT+str(len(songs))+Style.RESET_ALL+" songs")
    n = int(input("Amount of songs: "))

    return temp, n


def PlayByUser(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/users/*username*/tracks"+Style.RESET_ALL)
    user = input("Username: ")
    response = requests.get("https://music.yandex.ru/users/"+user+"/tracks")

    temp, n = MainWork(response, choice)

    DisMus(temp, n)


def PlayByPlaylist(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/users/music-blog/playlists/*number*"+Style.RESET_ALL)
    playlist = input("Playlist number: ")
    response = requests.get("https://music.yandex.ru/users/music-blog/playlists/"+playlist)

    temp, n = MainWork(response, choice)

    DisMus(temp, n)


def PlayByOwn(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/users/*username*/playlists/*number*"+Style.RESET_ALL)
    user = input("Username: ")
    playlist = input("Playlist number: ")
    response = requests.get("https://music.yandex.ru/users/"+user+"/playlists/"+playlist)

    temp, n = MainWork(response, choice)

    DisMus(temp, n)


def PlayByArtist(choice):
    print(Fore.BLACK+Style.BRIGHT+"link like: https://music.yandex.ru/artist/*number*/tracks"+Style.RESET_ALL)
    artist = input("Artist number: ")
    response = requests.get("https://music.yandex.ru/artist/"+artist+"/tracks")

    temp, n = MainWork(response, choice)

    DisMus(temp, n)


def Restart():
    t = input("Restart? y/n: ")
    if (t == "y"):
        os.system('cls' if os.name == 'nt' else 'clear')
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        quit()


def SwitchMode(choice):
    if choice == "1":
        PlayByUser(choice)
        Restart()
    elif choice == "2":
        PlayByPlaylist(choice)
        Restart()
    elif choice == "3":
        PlayByArtist(choice)
        Restart()
    elif choice == "4":
        PlayByOwn(choice)
        Restart()
    elif choice == "5":
        quit()
    else:
        print(Fore.RED+Style.BRIGHT+"Wrong code"+Style.RESET_ALL)
        Restart()

#Daily playlist: https://music.yandex.ru/users/yamusic-daily/playlists/63562191
