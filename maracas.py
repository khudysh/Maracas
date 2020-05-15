# -*- coding: utf-8 -*-
import YaMusLib

functions = [
            "Enter your username (link) and parse your own music (150 limit)",
            "Enter number of playlist (link), and I'll play it",
            "Enter number of artist (link)",
            "Enter your OWN playlist",
            "Exit"
            ]

print("Welcome to YandexMusic parser, choose mode: \n")
for i in range(len(functions)):
    print(" ",str(i+1)+")", functions[i])

#input("If you're have a Discord bot, enter your prefix, else leave blank: ")

YaMusLib.SwitchMode(input("\nCHOOSE YOUR DESTINY: "))
