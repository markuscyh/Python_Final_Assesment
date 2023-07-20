import random
import os
from datetime import datetime, timedelta


# Function to update the reservation
def update_reservation(reservation_list, index, change) :
    rsv_info = data[reservation_list].strip().split('|')
    rsv_info[index] = change
    data[reservation_list] = '|'.join(rsv_info) + '\n'  # Add new line character

    with open('reservation_21100649.txt', 'w') as f :
        for line in data :
            f.write(line)


# Function to count reservations for each date and slot
def count_reservations() :
    count_date_slot = {}
    for reservation in data :
        rsv_data = reservation.strip().split('|')
        if len(rsv_data) >= 2 :
            date = rsv_data[0]
            slot = rsv_data[1]
            new_date_slot = (date, slot)
            count_date_slot[new_date_slot] = count_date_slot.get(new_date_slot, 0) + 1
    return count_date_slot


# This function generates a meal recommendation
def meal_recommendation_generator(menu_contents, min, max, previous_recommendation):
    # This for loop helps ensure that recommendations of the same type are selected
    menu_recommendation = []
    for i in range(len(menu_contents)):
        if i >= min and i <= max:
            menu_recommendation.append(menu_contents[i])
    recommendation = random.choice(menu_recommendation)
    # This ensures that the same recommendation won't be selected twice in a row
    while recommendation == previous_recommendation:
        recommendation = random.choice(menu_recommendation)
    previous_recommendation = recommendation
    return recommendation, previous_recommendation


# This function will determine if the user continues with their process or return to the main menu
def menu_exit(question):
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
# This block of code will create the Display list for the Display function of the program
reservation_list = open("reservation_21100649.txt", "r")
reservation_list_contents = reservation_list.readlines()
reservation_list_contents.sort()
display_list = tuple(reservation_list_contents)

# This block of code will create the list for the menu recommendation
menu_list = open("menuItems_21100649.txt", "r")
menu_contents = menu_list.readlines()
menu_list.close()

main_menu_loop = True
while main_menu_loop:
    print("\nWelcome to Charming Thyme Trattoria. Please enter a number (1-6) that corresponds to the option you would like to select")

    # This loop contains exception handling to help ensure that the proper input is entered 
    while True:
        print("[1] Add Reservation")
        print("[2] Cancel Reservation")
        print("[3] Edit Reservations")
        print("[4] Display Reservations")
        print("[5] Generate Meal Recommendation")
        print("[6] Exit")

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
        os.system('cls')
        # Code for updating reservations
        while True :
            reservation_name = input("Enter Guest Name To Update The Reservation: ").upper()
            with open('reservation_21100649.txt', 'r') as f :
                data = f.readlines()
            matching_reservations = []

            for i in range(len(data)) :
                reservation_data = data[i].strip().split('|')
                if len(reservation_data) >= 3 and reservation_data[2].upper() == reservation_name :
                    matching_reservations.append(i)

            if not matching_reservations :
                print(f'{reservation_name} NOT FOUND\n')
                continue

            print(f"\nReservations found for {reservation_name}:")
            for i in range(len(matching_reservations)) :
                reservation_index = matching_reservations[i]
                reservation_info = data[reservation_index].strip().split('|')
                print(f"[{i + 1}] Reservation on {reservation_info[0]} at {reservation_info[1]}")

            while True :
                try :
                    choice = int(input("Enter the number of the reservation you want to update: "))
                    if 1 <= choice <= len(matching_reservations) :
                        break
                    else :
                        print("Invalid choice! Please enter a valid number.")
                except ValueError :
                    print("Invalid input! Please enter a number.")

            selected_reservation_index = matching_reservations[choice - 1]
            reservation_info = data[selected_reservation_index].strip().split('|')

            while True :
                # Ask the user for the field they want to update
                print("\nSelect Field To Update:")
                print("[1] Date\n[2] Slot\n[3] Name\n[4] Email\n[5] Contact\n[6] Number of People")

                valid_choices = ['1', '2', '3', '4', '5', '6']
                user_update = input("Please choose a number (1-6) or 'N' to stop updating this reservation: ")
                # Code for new date
                if user_update in valid_choices :
                    if user_update == '1' :
                        while True :
                            try:
                                date = input("\nEnter New Date (yyyy-mm-dd): ")
                                chosen_date = datetime.strptime(date, "%Y-%m-%d").date()
                                today = datetime.now().date()
                                min_reservation_date = today + timedelta(days=5)  # Minimum reservation date 5 days in advance
                                if chosen_date < min_reservation_date :
                                    print("Invalid Date! Reservation Should Be Made At Least 5 Days in Advance.")
                                    continue
                        # Check if the chosen slot on the chosen date has reached the maximum capacity (8 reservations)
                                date = datetime.strftime(chosen_date, "%Y-%m-%d")
                    # Check if the chosen slot on the chosen date has reached the maximum capacity (8 reservations)
                                date_slot = (date, reservation_info[1])
                                date_slot_count = count_reservations()
                                if date_slot in date_slot_count and date_slot_count[date_slot] >= 8 :
                                    print("This slot on this date has reached the maximum capacity.")
                                    continue

                                update_reservation(selected_reservation_index, 0, date)
                                print("Date updated successfully.")
                                break
                            except ValueError :
                                print("Invalid Date Format! Please Enter The Date in The Format yyyy-mm-dd.")
                    # Code for new slot
                    elif user_update == '2' :
                        while True :
                            slot = input("\nEnter New Slot from 1-4: ")
                            if slot in ['1', '2', '3', '4'] :
                                # Check if the chosen date and slot have reached the maximum capacity (8 reservations)
                                date_slot = (reservation_info[0], 'Slot ' + slot)
                                date_slot_count = count_reservations()
                                if date_slot in date_slot_count and date_slot_count[date_slot] >= 8 :
                                    print("This slot on this date has reached the maximum capacity.")
                                    continue

                                slot = 'Slot ' + slot
                                update_reservation(selected_reservation_index, 1, slot)
                                print("Slot updated successfully.")
                                break
                            else :
                                print("Invalid Slot! Please Choose Between 1-4.")
                    # Code for new name
                    elif user_update == '3' :
                        while True :
                            name_new = input("\nEnter New Name: ").strip().upper()
                            if name_new :
                                update_reservation(selected_reservation_index, 2, name_new)
                                print("Name updated successfully.")
                                break
                            else :
                                print("Name cannot be blank! Please enter a valid name.")
                    # Code for new email
                    
                    elif user_update == '4' :
                        while True :
                            email = input("\nEnter New Email: ").lower()
                            if " " in email:
                                print("Invalid Email! No spaces are allowed in an email.")
                            elif email.endswith('@gmail.com') or email.endswith('@yahoo.com') or email.endswith('@hotmail.com'):
                                update_reservation(selected_reservation_index, 3, email)
                                print("Email updated successfully.")
                                break
                            else :
                                print("Invalid Email! Only gmail, yahoo, and hotmail domains are accepted.")
                    # Code for new number
                    elif user_update == '5' :
                        while True :
                            contact = input("\nEnter New Contact Number: ")
                            if len(contact) == 10 and contact.isdigit() :
                                update_reservation(selected_reservation_index, 4, contact)
                                print("Contact Number updated successfully.")
                                break
                            else :
                                print("Invalid Number! Contact Should Be a 10-Digit Number.")
                    # Code for new number of people
                    elif user_update == '6' :
                        while True :
                            num_people = input("\nEnter New Number of People: ")
                            if num_people in ['1', '2', '3', '4'] :
                                update_reservation(selected_reservation_index, 5, num_people)
                                print("Number of People updated successfully.")
                                break
                            else :
                                print("Invalid Number of People! Maximum is 4.")
                elif user_update.upper() == 'N' :
                    break

            any_more_reservations = input("\nDo You Have Another Reservation To Update? (Y/N): ").upper()
            if any_more_reservations != 'Y' :
                os.system('cls')
                break
        


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
        # This loop allows the user to select the type of recommendation they want
        loop = True
        while loop:
            while True:
                print("Select the type of recommendation you would like from the numbers 1-5.")
                print("[1] Seafood")
                print("[2] Pork")
                print("[3] Chicken")
                print("[4] Beef")
                print("[5] Sides")
                user_recommendation = input(">>> ")
                if user_recommendation not in "12345":
                    print("\nPlease enter a number from 1-5 that corresponds with your selection.")
                else: 
                    break

            # These if statements help pick the type of reservations from the reservation list
            if user_recommendation == "1":
                min_recommendation, max_recommendation = 0, 7

            elif user_recommendation == "2":
                min_recommendation, max_recommendation = 8, 10

            elif user_recommendation == "3":
                min_recommendation, max_recommendation = 11, 13

            elif user_recommendation == "4":
                min_recommendation, max_recommendation = 14, 18

            elif user_recommendation == "5":
                min_recommendation, max_recommendation = 19, 21

            # The loop will ask the user to ask for a new recommendation or exit
            os.system('cls')
            recommendation_loop = True
            previous_recommendation = ""
            while recommendation_loop:
                print("\n--------------------------------------------------------------------------------\n")
                recommendation, previous_recommendation = meal_recommendation_generator(menu_contents, min_recommendation, max_recommendation, previous_recommendation)
                print(f"We recommend {recommendation}")
                recommendation_loop_question = "Would you like a new recommendation? Enter a number (1-2) to select your option \n[1] Another recommendation \n[2] Exit \n>>> "
                recommendation_loop = menu_exit(recommendation_loop_question)
            
            # This will ask the question of asking for a new recommendation type or to return to the main menu
            print("\n--------------------------------------------------------------------------------\n")
            loop_question = "Would you like to select a different type of recommendation or return to the main menu? Enter a number (1-2) to select your option \n[1] New recommendation type \n[2] Exit \n>>> "
            loop = menu_exit(loop_question)
            os.system('cls')
        os.system('cls')
        print("\n--------------------------------------------------------------------------------")



    elif main_menu_input == 6:
        main_menu_loop = False

print("--------------------------------------------------------------------------------")
print("Thank you for using the program")