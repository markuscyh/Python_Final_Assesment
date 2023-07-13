import random
import datetime
import os




# This function generates a meal recommendation
def meal_recommendation_generator(menu_contents):
    recommendation = random.choice(menu_contents)
    return recommendation

# This function will determine if the user continues with their process or return to the main menu
def main_menu_exit(question):
    loop = True
    while loop:
        answer = input(f"{question}")
        if answer in "12":
            loop = False
        else:
            print("Please enter the number (1-2) that corresponds with your selection.")
    if answer == "1":
        loop = True
        return loop
    elif answer == "2":
        loop = False
        return loop

#-----------------------------------------------------------------------------#
# This block of code will create the initial reservation_list and the Display list for the Display function of the program
reservation_list = open("reservation_21100649.txt", "r")
reservation_list_contents = reservation_list.readlines()
display_list = reservation_list_contents
display_list.sort()
display_list = tuple(display_list)

# This block of code will create the list for the menu recommendation
menu_list = open("menuItems_21100649.txt", "r")
menu_contents = menu_list.readlines()
menu_list.close()

main_menu_loop = True
while main_menu_loop:
    print("\nWelcome to Charming Thyme Trattoria. Please enter a number (1-6) that corresponds to the option you would like to select")

    # This loop contains exception handling to help ensure that the proper input is entered 
    while True:
        print("[1] Add Reservation \n[2] Cancel Reservation \n[3] Edit Reservations \n[4] Display Reservations \n[5] Generate Meal Recommendation \n[6] Exit")

        try:
            main_menu_input = int(input(">>> "))
            os.system('cls')
            if main_menu_input < 1 or main_menu_input > 6:
                os.system('cls')
                print("Please type a number (1-6) that corresponds to the option you would like to select. \n")
                print("--------------------------------------------------------------------------------\n")
            else:
                break
        except ValueError:
            os.system('cls')
            print("Please enter a valid number (1-6) \n")
            print("--------------------------------------------------------------------------------\n")
    
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
        print("\n--------------------------------------------------------------------------------\n")
        display_guide = "No. | {0:^10} | {1:^6} | {2:^15} | {3:^31} | {4:^10} | {5:^1} \n".format("Date","Slot","Name","Email","Phone Num","PAX")
        print(display_guide)

        list_count = 1
        for i in range(len(display_list)):
            if i % 10 == 0 and i != 0:
                display_continue = input("Enter any word, number or symbol to return to continue: ")
                os.system('cls')
                print(display_guide)
            display_list_contents = display_list[i]
            display_list_contents = display_list_contents.split("|")
            display_output = "{0:^3} | {1:^1} | {2:^1} | {3:^15} | {4:^31} | {5:^10} |  {6:^1}".format(list_count,display_list_contents[0], display_list_contents[1], display_list_contents[2], display_list_contents[3], display_list_contents[4], display_list_contents[5])
            print(display_output)
            list_count += 1

        # This input will allow the user to view the display list before returning to the main menu
        display_exit = input("Enter any word, number or symbol to return to the main menu: ")
        os.system('cls')
        print("\n--------------------------------------------------------------------------------")



    elif main_menu_input == 5:
        print("\n--------------------------------------------------------------------------------\n")
        # The while loop will allow the user to ask for a new recommendation or return to the main menu
        loop = True
        while loop:
            print(f"We recommend {meal_recommendation_generator(menu_contents)}")
            loop_question = "Would you like a new recommendation or return to the main menu? Enter a number (1-2) \n[1] Another recommendation \n[2] Exit \n>>> "
            loop = main_menu_exit(loop_question)
            os.system('cls')
        os.system('cls')
        print("\n--------------------------------------------------------------------------------")


    elif main_menu_input == 6:
        main_menu_loop = False



reservation_list.close()
print("--------------------------------------------------------------------------------")
print("Thank you for using the program")

