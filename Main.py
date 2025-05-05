import time
import os
import platform
import shutil
from fancy_text import text_edit

menu = ["Get Last Known Cost Of Attendance", "Calculate Wage Necessary for next payment", "Adjust Cost Of Attendance", "Exit"]

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear_terminal()

print("Made By John Cunnington \n5/4/25\nThis program is meant to help manage student funds and help me understand my finances better.\n\n" + text_edit("italic") + "This program is a current work in progress. ")


time.sleep(3)
clear_terminal()

print(text_edit("title") + "What Would You Like To Do?")

i = 1
for choice in menu:
    print(str(i) + " --- " + choice)
    i += 1