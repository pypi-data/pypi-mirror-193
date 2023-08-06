# TBGDL by Marko2155
# Please do not remove these comments, modify any code or reupload this to PyPI without crediting the owner first.

from colorama import *
import os
import playsound

red = Fore.RED
black = Fore.BLACK
blue = Fore.BLUE
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
default = Fore.WHITE
cyan = Fore.CYAN
green = Fore.GREEN


def tbgdl_print(text, color):
    print(color, text)

    
def tbgdl_quit():
    print(Fore.WHITE, " ")
    quit()

def tbgdl_clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def tbgdl_getinput():
    return input()

def tbgdl_new_scene(command1, command2, command3, command4, command5, command6, command7, command8, command9, command10):
    return command1, command2, command3, command4, command5, command6, command7, command8, command9, command10

def tbgdl_load_scene(scene):
    return scene
