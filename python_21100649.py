import random
import datetime
import os





# This function generates a meal recommendation
def meal_recommendation_generator():
    menu_list = open("menuItems_21100649.txt", "r")
    menu_contents = menu_list.readlines()
    recommendation = random.choice(menu_contents)
    return recommendation

# This function will determine if the user continues with their process or return to the main menu
def main_menu_exit(question):
    loop = True
    while loop == True:
        answer = input(f"{question}")
        if answer == "1" or answer == "2":
            loop = False
        else:
            loop = True
    if answer == "1":
        loop = True
        return loop
    elif answer == "2":
        loop = False
        return loop

# From this point below is the code that will first be executed when running the program
# This block of code will create the Reservation Display list for the Display function of the program
reservation_list = open("reservation_21100649.txt", "r")
reservation_list_contents = reservation_list.readlines()
reservation_list.close()

main_menu_loop = True
while main_menu_loop == True:
    print("\nWelcome to Charming Thyme Trattoria. Please type the number that corresponds to the option you would like to select")

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
            list_count = 0
            for i in range(len(reservation_list_contents)):
                print(reservation_list_contents[list_count])
                list_count += 1
            # This input will allow the user to view the display list before returning to the main menu
            display_exit = input("Enter any word, number or symbol to return to the main menu: ")
            os.system('cls')

        
    elif main_menu_input == 5:
        # The while loop will keep the user in this option until they decide to exit and go back to the main menu
        loop = True
        while loop:
            print(f"We recommend {meal_recommendation_generator()}")
            loop_question = "Would you like a new recommendation or return to the main menu? \n[1] Another recommendation \n[2] Exit \n"
            loop = main_menu_exit(loop_question)
        os.system('cls')

    elif main_menu_input == 6:
        main_menu_loop = False

print("\nThank you for using the program")