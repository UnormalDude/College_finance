import os
import shutil
import time
from fancy_text import text_edit  # Custom module for formatting terminal text (e.g., colors, bold, italic)

# Function to read and display the cost of attendance (COA) from a file
def cost_of_attendance():
    with open("temp/coa", "r") as file:  # Open the COA file in read mode
        coa = file.readlines()  # Read all lines into a list
    if len(coa) < 4:  # Check if file has fewer than 4 lines (incomplete data)
        print("\n\t\t" + text_edit("red") + text_edit("bold") + "No COA to read. Exiting\n\n" + text_edit("reset"))
        time.sleep(1)  # Wait for 1 second before exiting
    else:
        # Print each COA category with formatting
        print(f"Tuition: ${coa[0]}")
        print(f"Room: ${coa[1]}")
        print(f"Food: ${coa[2]}")
        print(f"Fees: ${coa[3]}")
        print(f"Total: ${coa[4]}")

        # Prompt user to continue after reviewing the output
        input("\n\t" + text_edit("italic") + "Press Enter To Continue..." + text_edit("reset"))

# Function to help user calculate work hours or required wage to afford a portion of tuition
def calc_wage():
    print("This function will let you see how many hours you need at your current rate to afford a percentage fo the cost.")
    print("Or you can input how many hours you can work per week and it will tell you how much you would need to earn per hour.")

    # Ask for current financial contribution from the user
    current_funds = input("\n\nFirst please type how much money you can currently put towards tuition: ")
    
    # Ask the user for the percentage of tuition they want to cover
    percentage = input("\nplease type the percentage of the tuition you are looking to pay: \n\t>")
    
    # Ask user whether they want to input hourly rate or available work hours
    user_input = input("Would you rather input:\n1 - An Hourly Rate\n2 - Hours you can work a week")

    # Placeholder for future logic based on user choice
    # if user_input == "1":
        # Logic for calculating required hours based on hourly rate

# Function to allow user to update the COA values
def change_coa():
    # Introduction and instructions for input
    print("Here you will be asked to provide the costs of different categories. Tuition, Room and board, Food, and Fees.")
    print("\n" + text_edit("bold") + text_edit("red") + "If you do not know a cost, please just enter a zero\n\nOnly numbers, no commas are needed\n" + text_edit("reset"))

    # Get numerical input for each major COA component
    tuition = int(input("Tuition: $"))
    room = int(input("\nRoom and Board: $"))
    food = int(input("\nFood: $"))
    
    # Instruction for entering multiple fees
    print(text_edit("red") + text_edit("bold") + "Please input only numbers for fees. Each fee can be put in its own category. When done type \'done\'\n\n" + text_edit("reset"))
    
    fees = 0  # Initialize total fees to zero

    # Loop to allow multiple fee entries
    while True:
        fee = input("\nFee: $")
        if fee == "done":  # Exit loop when user types 'done'
            break
        else:
            fees += int(fee)  # Add fee to total

    total = tuition + room + food + fees  # Calculate total COA

    data = f"{tuition}\n{room}\n{food}\n{fees}\n{total}"  # Format data for file writing
    print("\n\nTotal: " + str(total))  # Display total to user

    # Write updated COA values to file
    with open("temp/coa", "w") as file:
        file.write(data)
