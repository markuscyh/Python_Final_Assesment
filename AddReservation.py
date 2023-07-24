import random
import os
from datetime import datetime, timedelta

# Function to add the reservation details
def ADD_Reservation():
    with open('reservations_21100649.txt', 'a+') as ADD:
        ADD_Reservation_str = ("\n{0}|{1}|{2}|{3}|{4}|{5}".format(ADD_RSV_details[0],ADD_RSV_details[1],ADD_RSV_details[3],ADD_RSV_details[4],ADD_RSV_details[5]))
        ADD.write(ADD_Reservation_str)
        print("Reservation has been added sucessfully!")
        ADD_RSV_details.clear() #Removes all data from the ADD_RSV_list so that new reservation details can be added.
        ADD.close()

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
# This variable enables the main menu 
main_menu_loop = True

# This block of code will create the Display list for the Display function of the program
try:
    with open("reservation_21100649.txt", "r") as reservation_list:
        reservation_list_contents = reservation_list.readlines()
        reservation_list_contents.sort()
        display_list = tuple(reservation_list_contents)
except FileNotFoundError:
    main_menu_loop = False
    print("Reservation file not Found! Please contact management for assistance!")

# This block of code will create the list for the menu recommendation
try:
    with open("menuItems_21100649.txt", "r") as menu_list:
        menu_contents = menu_list.readlines()
except:
    main_menu_loop = False
    print("Menu file not found! Please contact management for assistance!")

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
        #Code for adding reservations.
        print("Selected 'Add Reservations'. Do you wish to:\n[1] Proceed.\n[2] Return to Main Menu")
        RSV_ADD_parent_loop = True
        while RSV_ADD_parent_loop:
            ADD_RSV_selection_1 = input("(1 - 2) Please enter your selection here: ")
            if ADD_RSV_selection_1 == '1':
                RSV_ADD_selection = '1'
                break
            
            elif ADD_RSV_selection_1 == '2':
                print("Returning to Main Menu")
                os.system('cls')
                RSV_ADD_selection = '2'
                break
            
            else:
                print("Error: Invalid selection! Can only use 1 or 2 as your options of choice.\nTry again\n")

        print("Proceeding with selected function\n")
        while RSV_ADD_selection == '1' or RSV_ADD_selection == '3':

                    ADD_RSV_details = [] #Input list.

                    #Loops for each input
                    RSV_Date_loop = True
                    RSV_Slot_loop = True
                    RSV_Name_loop = True
                    RSV_Email_loop = True
                    RSV_PhoneNum_loop = True
                    RSV_Size_loop = True
                    ADD_RSV_loop = True
                    
                    #Getting the date of the reservation
                    while RSV_Date_loop:
                        #FM stands for formatted.
                        #RSV stands for Reservation.
                        today = datetime.now()
                        FM_today = datetime.strftime(today, "%Y-%m-%d")
                        Date_minimum = today + timedelta(days=4)
                        try:
                            print("RESERVATION DATE:")
                            RSV_Date_input = input("The date of the reservation must be 5 days in advacne from today {0}\nPlease enter the date of the reservation in the format (YYYY-mm-dd): ".format(FM_today))
                            
                        except ValueError:
                            print("Error: Invalid date format!\nPlease enter the date of the reservation in (YYYY-mm-dd) format.\nPlease try again\n")
                        else:
                            try:
                                FM_Date_input = datetime.strptime(RSV_Date_input, "%Y-%m-%d")
                            except:
                                print("Error: Invalid seperator format!\nPlease enter the date of the reservation in (YYYY-MM-DD) format.\nTry again\n")

                            else:
                                if FM_Date_input <= Date_minimum:
                                    print("Error: Invalid date selected!\nYou can only apply for a reservation at least 5 days in advance from today\nPlease try again\n")
                                else:

                                    with open('reservation_21100649.txt', 'r') as dt:
                                        RSV_Date_data = dt.read()
                                        Date_count = RSV_Date_data.count(RSV_Date_input)

                                        #Counts to see if the date is found in the list 32 times. If true, then it means the date is full
                                        if Date_count != 32:
                                            print("Reservation set on {0}\n".format(RSV_Date_input))
                                            ADD_RSV_details.append(RSV_Date_input) #Inputs date into list
                                            #print(Date_count) #Test code.
                                            break

                                        else:
                                            print("Error: Selected date is full.\nThe selected date is full and has no more room for reservations.\nTry another date.\n")
                                            #print(Date_count) #test code

                    #Getting the session slot of the reservation
                    while RSV_Slot_loop:
                        print("RESERVATION SLOT:")

                        #Counts the reservation slots in the date
                        RSV_slot1 = (reservation_info[0], 'Slot 1')
                        RSV_date_slot1_count = count_reservations()

                        RSV_slot2 = (reservation_info[0], 'Slot 2')
                        RSV_date_slot2_count = count_reservations()

                        RSV_slot3 = (reservation_info[0], 'Slot 3')
                        RSV_date_slot3_count = count_reservations()

                        RSV_slot4 = (reservation_info[0], 'Slot 4')
                        RSV_date_slot4_count = count_reservations()

                        print("NOTICE:\nEach date supports a maximum of 8 reservations per slot.\nHere are the time slots for the reservation on {0}.\n[1] 12:00pm - 02:00pm (Status: {1}/8)\n[2] 02:00pm - 04:00pm (Status: {2}/8)\n[3] 06:00pm - 08:00pm (Status: {3}/8)\n[4] 08:00pm - 10:00pm (Status: {4}/8)".format(RSV_Date_input, RSV_date_slot1_count, RSV_date_slot2_count, RSV_date_slot3_count, RSV_date_slot4_count))
                        try:
                            RSV_Slot_input = int(input("Please select the time slot for the reservation: "))
                        except:
                            print("Error: Invalid input format!\nPlease enter the input for the time slot in integer form only.\nTry again")
                        else:
                            RSV_date_slot = (reservation_info[0], 'Slot ' + RSV_Slot_input)
                            RSV_date_slot_count = count_reservations()
                            if RSV_date_slot in RSV_date_slot_count and RSV_date_slot_count[RSV_date_slot] >= 8 :
                                print("This slot on this date has reached the maximum capacity.\nPlease select a different slot")
                            else:
                                ADD_RSV_details.append(RSV_Slot_input)
                                print("Reservation set for slot {0}".format(RSV_Slot_input))
                    
                    #Getting the customer's name
                    while RSV_Name_loop:
                        print("CUSTOMER NAME:")
                        print("NOTICE:\nOne customer name per reservation slot.\nensure that there are no symbols or numbers in the customer's name.\n")

                        Rsv_Name_input = input("Please enter the customer's name: ").upper()
                        FM_RSV_Name_input = ''.join((x for x in Rsv_Name_input if not x.isdigit())) #Removes any digits from the name.
                        print("Reservation for {0}, has been set\n".format(FM_RSV_Name_input))
                        ADD_RSV_details.append(Rsv_Name_input)
                        break

                    #Getting the customer's email
                    while RSV_Email_loop:
                        print("CUSTOMER EMAIL:")
                        print("NOTICE:\nEmail must be in correct format (E.g ExampleEmail@gmail.com)\ngmail, hotmail and yahoo domains are supported.\n")
                        RSV_Email_input = input("Please enter the customer's email address: ")
                        if RSV_Email_input.endswith("@gmail.com") or RSV_Email_input.endswith("@yahoo.com") or RSV_Email_input.endswith("@hotmail.com"):
                            print("Customer email added into reservation details\n")
                            ADD_RSV_details.append(RSV_Email_input)
                            break
                        else:
                            print("Error: Invalid email. Email must either use gmail, yahoo, or hotmail domains.\nTry again.\n")
                    
                    #Getting the customer's contact number
                    while RSV_PhoneNum_loop:
                        print("CUSTOMER CONTACT NUMBER:")
                        print("NOTICE:\n1.Customer contact number MUST be 10 digits long.\n2.Must start with 01.\n")
                        try:
                            RSV_PhoneNum_input = input("Please enter the customer's contact number: ")
                        except:
                            print("Error: Invalid phone number format!\nPhone (Contact) numbers can only be in integer form.\nPlease try again.\n")
                        else:
                            if len(RSV_PhoneNum_input) == 10 and RSV_PhoneNum_input.isdigit():
                                print("The customer's contact number has been added to the reservation details\n.")
                                ADD_RSV_details.append(RSV_PhoneNum_input)
                                break
                            else:
                                print("Error: Invalid customer phone number!\nCustomer's phone numbers can only be 10 digit long entries.\nTry again\n")

                    #Getting the reservation size.
                    while RSV_Size_loop:
                        print("RESERVATION SIZE:")
                        print("NOTICE:\nThe reservation size cannot be more than 4.")
                        try:
                            RSV_Size_input = int(input("Please enter the size of the reservation slot: "))
                        except: #If user enters non integer
                            print("Error: Invalid input format.\nThe system only accepts integer values for reservation size\nTry again.\n")
                        else: #Else, proceed.
                            #Checks if ResPax has at least 1 person or a maximum of 4 people, or anything in between.
                            if RSV_Size_input < 1:
                                print("Error: Invalid size input.\nReservation slots can never have 0 people.\nTry again\n")
                            elif RSV_Size_input > 4:
                                print("Error: Invalid size input.\nReservation slots support a maximum of 4 people per slot.\nTry again\n")
                            else:
                                print("A table for {0} will be reserved.\nProceeding to finalization".format(RSV_Size_input))
                                ADD_RSV_details.append(RSV_Size_input)
                                break
                    
                    #Finalizing the inputs
                    while ADD_RSV_loop:
                        print("Reservation details to be added:\nDate: {0}\nSession slot: \nCustomer name: {1}\nCustomer email: {2}\nCustomer contact number: {3}\nReservation size: {4}".format(RSV_Date_input, Rsv_Name_input, RSV_Email_input, RSV_PhoneNum_input, RSV_Size_input))
                        print("\nWould you like to:\n[1] Add the reservation and then prepare another one\n[2] Add the reservation and return to main menu\n[3] (In case of errors) Redo the reservation process\n[4] Cancel the add reservation process")
                        ADD_RSV_selection = input("Please enter your selection here: ")

                        while True:
                            if ADD_RSV_selection == '1':
                                ADD_Reservation()
                                os.system('cls')
                                print("Adding new reservation.\n")
                                ADD_RSV_loop = False
                                break

                            elif ADD_RSV_selection == '2':
                                ADD_Reservation()
                                os.system('cls')
                                print("Reservation added succesfully.\nReturning to main menu.")
                                RSV_ADD_parent_loop = False
                                break
                            
                            elif ADD_RSV_selection == '3':
                                ADD_RSV_details.clear()
                                os.system('cls')
                                print("Redoing reservation\n")
                                ADD_RSV_loop = False
                                break

                            elif ADD_RSV_selection == '4':
                                ADD_RSV_details.clear()
                                os.system('cls')
                                print("Cancelled add reservation process.\nReturning to main menu.")
                                ADD_RSV_loop = False
                                RSV_ADD_parent_loop = False
                                break
                        
                    

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

            os.system('cls')
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
                    if 1 <= choice <= len(matching_reservations):
                        break
                    else:
                        print("\nInvalid choice! Please enter a valid number.")
                except ValueError:
                    print("\nInvalid input! Please enter a number.")

            selected_reservation_index = matching_reservations[choice - 1]
            reservation_info = data[selected_reservation_index].strip().split('|')
            os.system('cls')

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
                                    os.system('cls')
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
                                os.system('cls')
                                print("Date updated successfully.")
                                break
                            except ValueError :
                                print("Invalid Date Format! Please Enter The Date in The Format yyyy-mm-dd.")
                    # Code for new slot
                    elif user_update == '2':
                        while True :
                            slot = input("\nEnter New Slot from 1-4: ")
                            if slot in ['1', '2', '3', '4']:
                                # Check if the chosen date and slot have reached the maximum capacity (8 reservations)
                                date_slot = (reservation_info[0], 'Slot ' + slot)
                                date_slot_count = count_reservations()
                                if date_slot in date_slot_count and date_slot_count[date_slot] >= 8:
                                    print("This slot on this date has reached the maximum capacity.")
                                    continue

                                slot = 'Slot ' + slot
                                update_reservation(selected_reservation_index, 1, slot)
                                os.system('cls')
                                print("Slot updated successfully.")
                                break
                            else:
                                os.system('cls')
                                print("Invalid Slot! Please Choose Between 1-4.")
                    # Code for new name
                    elif user_update == '3':
                        while True:
                            name_new = input("\nEnter New Name: ").strip().upper()
                            if name_new:
                                update_reservation(selected_reservation_index, 2, name_new)
                                os.system('cls')
                                print("Name updated successfully.")
                                break
                            else:
                                os.system('cls')
                                print("Name cannot be blank! Please enter a valid name.")
                    # Code for new email
                    
                    elif user_update == '4':
                        while True:
                            email = input("\nEnter New Email: ")
                            if " " in email:
                                print("Invalid Email! No spaces are allowed in an email.")
                            elif email.endswith('@gmail.com') or email.endswith('@yahoo.com') or email.endswith('@hotmail.com'):
                                update_reservation(selected_reservation_index, 3, email)
                                os.system('cls')
                                print("Email updated successfully.")
                                break
                            else:
                                os.system('cls')
                                print("Invalid Email! Only gmail, yahoo, and hotmail domains are accepted.")
                    # Code for new number
                    elif user_update == '5':
                        while True:
                            contact = input("\nEnter New Contact Number: ")
                            if len(contact) == 10 and contact.isdigit():
                                update_reservation(selected_reservation_index, 4, contact)
                                os.system('cls')
                                print("Contact Number updated successfully.")
                                break
                            else:
                                os.system('cls')
                                print("Invalid Number! Contact Should Be a 10-Digit Number.")
                    # Code for new number of people
                    elif user_update == '6':
                        while True:
                            num_people = input("\nEnter New Number of People: ")
                            if num_people in ['1', '2', '3', '4']:
                                update_reservation(selected_reservation_index, 5, num_people)
                                os.system('cls')
                                print("Number of People updated successfully.")
                                break
                            else:
                                os.system('cls')
                                print("Invalid Number of People! Maximum is 4.")
                elif user_update.upper() == 'N':
                    break
            
            os.system('cls')
            any_more_reservations = input("\nDo You Have Another Reservation To Update? (Y/N): ").upper()
            if any_more_reservations != 'Y':
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
