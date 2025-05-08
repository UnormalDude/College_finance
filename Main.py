import time
import os
import platform
import shutil

from fancy_text import text_edit
import menu

menu_list = ["Get Last Known Cost Of Attendance", "Calculate Wage Necessary for next payment", "Adjust Cost Of Attendance", "Exit"]

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear_terminal()

print("Made By John Cunnington \n5/4/25\nThis program is meant to help manage student funds and help me understand my finances better.\n\n" + text_edit("italic") + "This program is a current work in progress. ")


while True:
    time.sleep(3)
    clear_terminal()

    print( text_edit("title") + "What Would You Like To Do?" + text_edit("reset") )

    i = 1
    for choice in menu_list:
        time.sleep(0.5)
        print(str(i) + " --- " + choice)
        i += 1

    menu_choice = input("\n\t>")

    clear_terminal()
    if menu_choice == "1":
        menu.cost_of_attendance()

    elif menu_choice == "2":
        menu.calc_wage()

    elif menu_choice == "3":
        menu.change_coa()

    elif menu_choice == "4":
        print("Goodbye!")
        exit()

    else:
        print(text_edit("bold") + text_edit("red") + "\n\n\n\n\n\t\t| Incorrect input |\n\n" + text_edit("reset"))