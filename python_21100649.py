import random
import datetime
import os





# This function generates a meal recommendation
def meal_recommendation_generator():
    menu_list = open("menuItems_21100649.txt", "r")
    menu_contents = menu_list.readlines()
    recommendation = random.choice(menu_contents)
    return recommendation
    

# From this point below is the code that will first be executed when running the program
main_menu_loop = True
while main_menu_loop == True:
    print("Welcome to Charming Thyme Trattoria. Please type the number that corresponds to the option you would like to select")

    # This loop contains exception handling to help ensure that the proper input is entered 
    loop = True
    while loop == True:
        print("[1] Add Reservation \n[2] Cancel Reservation \n[3] Edit Reservations \n[4] Display Reservations \n[5] Generate Meal Recommendation \n[6] Exit")

        try:
            main_menu_input = int(input())
        except:
            print("Please enter a valid input. \n")
        else:
            if main_menu_input < 1 or main_menu_input > 6:
                print("Please type the number that corresponds to the option you would like to select. \n")
            else:
                loop = False
    
    if main_menu_input == 1:
        pass
        #function
    elif main_menu_input == 2:
        pass
        #function
    elif main_menu_input == 3:
        pass
        #function
    elif main_menu_input == 4:
        pass
        #function
    elif main_menu_input == 5:
        # The while loop will keep the user in this option until they decide to exit and go back to the main menu
        loop = True
        while loop == True:
            print(f"We recommend the {meal_recommendation_generator()}")
            

    elif main_menu_input == 6:
        main_menu_loop = False

print("\nThank you for using the program")