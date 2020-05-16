# -*- coding: utf-8 -*-
import YaMusLib
from colorama import init, Style, Fore

init()

functions = [
            "Enter your username (link) and parse your own music (150 limit)",
            "Enter number of playlist (link), and I'll play it",
            "Enter number of artist (link)",
            "Enter your OWN playlist",
            "Exit"
            ]

print(Fore.YELLOW+Style.BRIGHT+"\n\t\t\t\tWelcome to YandexMusic parser, choose mode: \n" + Style.RESET_ALL)
for i in range(len(functions)):
    print(Fore.CYAN+" ",str(i+1)+")", functions[i]+ Style.RESET_ALL)


#input("If you're have a Discord bot, enter your prefix, else leave blank: ")

YaMusLib.SwitchMode(input("\nCHOOSE YOUR DESTINY: "))

#не выдавать при ошибке кол-во песен
