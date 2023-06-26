import random
import datetime
import os

def main_menu():
    print("Welcome to Charming Thyme Trattoria. Please type the number that corresponds to the option you would like to select")

    # This loop contains exception handling to help ensure that the proper input is entered 
    loop = True
    while loop == True:
        print("[1] Add Reservation \n[2] Cancel Reservation \n[3] Edit Reservations \n[4] Generate Meal Recommendation \n[5] Exit")

        try:
            main_menu_input = int(input())
        except:
            print("Please enter a valid input. \n")
        else:
            if main_menu_input < 1 or main_menu_input > 5:
                print("Please type the number that corresponds to the option you would like to select. \n")
            else:
                loop = False
    



# From this point below is the code that will first be executed when running the program
main_menu()