import time                   # For adding delays between actions
import os                     # For interacting with the operating system (e.g., clearing terminal)
import platform               # To detect the operating system type
import shutil                 # For potential file operations (not used in this snippet)

from fancy_text import text_edit   # Custom module for text styling
import menu                        # Custom module containing menu-related functions

# List of options displayed to the user in the menu
menu_list = ["Get Last Known Cost Of Attendance", "Calculate Wage Necessary for next payment", "Adjust Cost Of Attendance", "Exit"]

# Function to clear the terminal screen depending on the user's OS
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Clear the terminal at program start
clear_terminal()

# Display introductory message with styled text
print("Made By John Cunnington \n5/4/25\nThis program is meant to help manage student funds and help me understand my finances better.\n\n" + text_edit("italic") + "This program is a current work in progress. ")

# Start of the main loop that keeps the program running
while True:
    time.sleep(3)            # Delay before clearing screen again
    clear_terminal()         # Clear the terminal for clean menu display

    # Print menu title with styled text
    print( text_edit("title") + "What Would You Like To Do?" + text_edit("reset") )

    # Print each menu item with a delay for better user experience
    i = 1
    for choice in menu_list:
        time.sleep(0.5)
        print(str(i) + " --- " + choice)
        i += 1

    # Get user input for menu selection
    menu_choice = input("\n\t>")

    clear_terminal()  # Clear screen before executing choice

    # Execute corresponding function based on user's input
    if menu_choice == "1":
        menu.cost_of_attendance()     # Call function to get cost of attendance

    elif menu_choice == "2":
        menu.calc_wage()              # Call function to calculate needed wage

    elif menu_choice == "3":
        menu.change_coa()             # Call function to adjust COA

    elif menu_choice == "4":
        print("Goodbye!")             # Exit message
        exit()                        # End program

    else:
        # Handle incorrect input with styled error message
        print(text_edit("bold") + text_edit("red") + "\n\n\n\n\n\t\t| Incorrect input |\n\n" + text_edit("reset"))
