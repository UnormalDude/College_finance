import os
import shutil
import time
from fancy_text import text_edit

def cost_of_attendance():
    with open("temp/coa", "r") as file:
        coa = file.readlines()
    if len(coa) < 4:
        print("\n\t\t" + text_edit("red") + text_edit("bold") + "No COA to read. Exiting\n\n")
        time.sleep(1)
        exit()

    print(f"Tuition: ${coa[0]}")
    print(f"Room: ${coa[1]}")
    print(f"Food: ${coa[2]}")
    print(f"Fees: ${coa[3]}")
    print(f"Total: ${coa[4]}")

    input("\n\t" + text_edit("italic") + "Press Enter To Continue..." + text_edit("reset"))

def calc_wage():
    print("This function will let you see how many hours you need at your current rate to afford a percentage fo the cost.")
    print("Or you can input how many hours you can work per week and it will tell you how much you would need to earn per hour.")

    current_funds = input("\n\nFirst please type how much money you can currently put towards tuition: ")
    percentage = input("\nplease type the percentage of the tuition you are looking to pay: \n\t>")
    user_input = input("Would you rather input:\n1 - An Hourly Rate\n2 - Hours you can work a week")

    #if user_input == "1":
        

def change_coa():
#This will allow the user to change the cost of attendance for the school they intend on attending
    print("Here you will be asked to provide the costs of different categories. Tuition, Room and board, Food, and Fees.")
    print("\n" + text_edit("bold") + text_edit("red") + "If you do not know a cost, please just enter a zero\n\nOnly numbers, no commas are needed\n" + text_edit("reset"))

    tuition = int(input("Tuition: $"))
    room = int(input("\nRoom and Board: $"))
    food = int(input("\nFood: $"))
    
    print(text_edit("red") + text_edit("bold") + "Please input only numbers for fees. Each fee can be put in its own category. When done type \'done\'\n\n" + text_edit("reset"))
    fees = 0
    while True:
        fee = input("\nFee: $")
        if fee == "done":
            break
        else:
            fees += int(fee)

    total = tuition + room + food + fees

    data = f"{tuition}\n{room}\n{food}\n{fees}\n{total}"
    print("\n\nTotal: " + str(total))

    with open("temp/coa", "w") as file:
        file.write(data)