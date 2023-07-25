import random
import os
from datetime import datetime, timedelta

# Function to add the reservation details
def ADD_Reservation():
    with open('reservations_21100649.txt', 'a+') as ADD:
        ADD_Reservation_str = ("\n{0}|{1}|{2}|{3}|{4}|{5}".format(RSV_Date_input, RSV_Slot_input, FM2_RSV_Name_input, RSV_Email_input, RSV_PhoneNum_input, RSV_Size_input))
        ADD.write(ADD_Reservation_str)
        print("Reservation has been added sucessfully!")
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
        os.system('cls')
        
        #Initial assigning of user input.
        RSV_Date_input = ''
        RSV_Slot_input = ''
        FM2_RSV_Name_input = ''
        RSV_Email_input = ''
        RSV_PhoneNum_input = ''
        RSV_Size_input = ''

        ADD_RSV_loop = True #Starts the Sub Program
        while ADD_RSV_loop:

            #Its for RSV_Name to remove symbols.
            forbidden_symbols = ['`','~','!','@','#','#','%','^','&','*','(',')','-','_','=','+',',','<','.','>','/','?',';',':','"','[',']','{','}','|']

            '''
            IMPORTANT:
            RSV stands for reservation
            FM stands for formatted
            '''

            #Loops for each input
            ADD_RSV_selection_loop = True
            

            #Prompt and start of Submenu UI
            print("ADD RESERVATION SUBMENU\n")
            print("Reservation details\n{6}\nReservation Date: {0}\nReservation Session Slot: {1}\nCustomer Name: {2}\nCustomer Email: {3}\nCustomer Phone Number: {4}\nReservation Size: {5}\n{6}\n".format(RSV_Date_input, RSV_Slot_input, FM2_RSV_Name_input, RSV_Email_input, RSV_PhoneNum_input, RSV_Size_input,"------------------------------"))
            print("Please enter (or fix) the reservation details for:\n[1] Reservation Date\n[2] Reservation Session Slot\n[3] Customer Name\n[4] Customer Email\n[5] Customer Phone Number\n[6] Reservation Size\n\nOr would you like to:\n[7] Cancel the reservation process and return to main menu\n[8] Restart the reservation process\n[9] Add the reservation details and prepare another one\n[10] Add the reservation details and return to main menu\n")

            while ADD_RSV_selection_loop:
                RSV_Selection = input("Please enter your selection from 1-10 here: ")
                
                if RSV_Selection == '1':

                    os.system('cls')
                    
                    #Getting the date of the reservation
                    while True:
                        
                        today = datetime.now()
                        FM_today = datetime.strftime(today, "%Y-%m-%d")
                        Date_minimum = today + timedelta(days=4)
                        try:
                            print("RESERVATION DATE:")
                            RSV_Date_input = input("NOTICE:\nThe date of the reservation must be 5 days in advacned from today {0}\nThe escape code is today's date.\nPlease enter the date of the reservation in the format (YYYY-mm-dd): ".format(FM_today))
                            
                        except ValueError:
                            os.system('cls')
                            print("Error: Invalid date format!\nPlease enter the date of the reservation in (YYYY-mm-dd) format.\nPlease try again\n")
                            
                        else:
                            try:
                                FM_RSV_DATE_input = datetime.strptime(RSV_Date_input, "%Y-%m-%d")
                            except:
                                os.system('cls')
                                print("Error: Invalid seperator format!\nPlease enter the date of the reservation in (YYYY-MM-DD) format.\nTry again\n")

                            else:
                                if RSV_Date_input != FM_today:
                                
                                    if FM_RSV_DATE_input <= Date_minimum and RSV_Date_input != FM_today:
                                        os.system('cls')
                                        print("Error: Invalid date selected!\nYou can only apply for a reservation at least 5 days in advance from today\nPlease try again\n")
                                    
                                    else:
                                        with open('reservation_21100649.txt', 'r') as dt:
                                            RSV_Date_data = dt.read()
                                            Date_count = RSV_Date_data.count(RSV_Date_input)

                                            #Counts to see if the date is found in the list 32 times. If true, then it means the date is full
                                            if Date_count != 32:
                                                print("Reservation set on {0}\n".format(RSV_Date_input))
                                                ADD_RSV_selection_loop = False

                                                os.system('cls')
                                                print("Reservation date succesfully added")

                                                break
                                            else:
                                                print("Error: Selected date is full.\nThe selected date is full and has no more room for reservations.\nTry another date.\n")
                                                #print(Date_count) #test code
                                else: 
                                    ADD_RSV_selection_loop = False
                                    os.system('cls')
                                    break


                
                elif RSV_Selection == '2':
                    
                    RSV_Slot_input = "Slot 1"
                    #Getting the session slot of the reservation
                    # while RSV_Slot_loop:
                    #     print("RESERVATION SLOT:")
                    #     with open("reservations_21100649.txt", "r") as st:
                    #         RSV_Slot_data = st.read()
                    #         RSV_Slot_data_count = 

                        # #Counts the reservation slots in the date.
                        # with open("reservations_21100649.txt", 'r') as st:
                        #     RSV_Slot_data = st.read()
                        #     RSV_Slot_data_date_count = RSV_Slot_data.count(RSV_Date_input)
                            


                        # print("NOTICE:\nEach date supports a maximum of 8 reservations per slot.\nHere are the time slots for the reservation on {0}.\n[1] 12:00pm - 02:00pm (Status: {1}/8)\n[2] 02:00pm - 04:00pm (Status: {2}/8)\n[3] 06:00pm - 08:00pm (Status: {3}/8)\n[4] 08:00pm - 10:00pm (Status: {4}/8)".format(RSV_Date_input, RSV_date_slot1_count, RSV_date_slot2_count, RSV_date_slot3_count, RSV_date_slot4_count))
                        # try:
                        #     RSV_Slot_input = int(input("Please select the time slot for the reservation: "))
                        # except:
                        #     print("Error: Invalid input format!\nPlease enter the input for the time slot in integer form only.\nTry again")
                        # else:

                        #         print("This slot on this date has reached the maximum capacity.\nPlease select a different slot")
                        #     else:
                        #         ADD_RSV_details.append(RSV_Slot_input)
                        #         print("Reservation set for slot {0}".format(RSV_Slot_input))
                
                elif RSV_Selection == '3':
                        
                        os.system('cls')
                        while True:
                            
                            print("CUSTOMER NAME:")
                            print("NOTICE:\nOne customer name per reservation slot.\nEnsure that there are no symbols or numbers in the customer's name as they will automatically be removed.\nThe escape code is 'ESCAPE'")
                            
                            RSV_Name_input = input("Please enter the customer's name: ").upper()
                            if RSV_Name_input == 'ESCAPE':
                                os.system('cls')
                                ADD_RSV_selection_loop = False
                                break
                            
                            else:
                                FM_RSV_Name_input = ''.join((x for x in RSV_Name_input if not x.isdigit()))
                                
                                FM2_RSV_Name_input = ''.join(x for x in FM_RSV_Name_input if not x in forbidden_symbols)
                                
                                
                                ADD_RSV_selection_loop = False
                                os.system('cls')
                                print("Customer Name has been succesfully added")
                                break
                
                elif RSV_Selection == '4':

                    os.system('cls')
                    #Getting the customer's email
                    while True:
                        
                        print("CUSTOMER EMAIL:")
                        print("NOTICE:\nEmail must be in correct format (E.g ExampleEmail@gmail.com)\ngmail, hotmail and yahoo domains are supported.\nThe escape code is 'ESCAPE'")
                        
                        RSV_Email_input = input("Please enter the customer's email address: ")
                        
                        if RSV_Email_input != 'ESCAPE':
                            if RSV_Email_input.endswith("@gmail.com") or RSV_Email_input.endswith("@yahoo.com") or RSV_Email_input.endswith("@hotmail.com"):
                                ADD_RSV_selection_loop = False
                                os.system('cls')
                                print("Customer Email succesfully added")
                                break
                            
                            else:
                                os.system('cls')
                                print("Error: Invalid email. Email must either use gmail, yahoo, or hotmail domains.\nTry again.\n")
                        else:
                            os.system('cls')
                            ADD_RSV_selection_loop = False
                            break

                elif RSV_Selection == '5':
                    
                    os.system('cls')
                    #Getting the customer's contact number
                    while True:
                        print("CUSTOMER CONTACT NUMBER:")
                        print("NOTICE:\n1.Customer contact number MUST be 10 digits long.\n2.Must start with 01.\nThe escape code is '0'")
                        
                        RSV_PhoneNum_input = input("Please enter the customer's contact number: ")

                        if RSV_PhoneNum_input != '0':   
                            if len(RSV_PhoneNum_input) == 10:
                                if RSV_PhoneNum_input.isdigit():
                                    if RSV_PhoneNum_input.startswith("01"):
                                        ADD_RSV_selection_loop = False
                                        os.system('cls')
                                        print("Customer Phone Number succesfully added")
                                        break
                                    else: 
                                        os.system('cls')
                                        print("Error: Invalid customer phone number!\nCustomer phone numbers can only start with '01'\nTry again.\n")
                                else:
                                    os.system('cls')
                                    print("Error: Invalid customer phone number format!\nCustomer phone numbers can only be digits.\nTry again.\n")
                            else:
                                os.system('cls')
                                print("Error: Invalid customer phone number length!\nCustomer phone numbers can only be 10 digits long.\nTry again\n")
                        else:
                            ADD_RSV_selection_loop = False
                            os.system('cls')
                            break

                elif RSV_Selection == '6':
                    
                    os.system('cls')
                    
                    #Getting the reservation size.
                    while True:
                        print("RESERVATION SIZE:")
                        print("NOTICE:\nThe reservation size cannot be more than 4.\nThe escape code is '0'")
                        
                        try:
                            RSV_Size_input = int(input("Please enter the size of the reservation slot: "))
                        except: #If user enters non integer
                            print("Error: Invalid input format.\nThe system only accepts integer values for reservation size\nTry again.\n")
                        else: #Else, proceed.

                            if RSV_Size_input != 0:
                                #Checks if ResPax has at least 1 person or a maximum of 4 people, or anything in between.
                                if RSV_Size_input < 1:
                                    os.system('cls')
                                    print("Error: Invalid size input.\nReservation slots can never have 0 people.\nTry again\n")

                                elif RSV_Size_input > 4:
                                    os.system('cls')
                                    print("Error: Invalid size input.\nReservation slots support a maximum of 4 people per slot.\nTry again\n")

                                else:
                                    ADD_RSV_selection_loop = False
                                    os.system('cls')
                                    print("Reservation Size has been succesfully added/updated\n")
                                    break
                            else:
                                os.system('cls')
                                ADD_RSV_selection_loop = False
                                break

                elif RSV_Selection == '7': 
                    
                    while True:
                        os.system('cls')

                        print("Are you sure you wish to return to main menu?\nYour progress will not be saved, and therefore need to be entered again.\n[1] Return to Main Menu\n[2] No, remain in program")
                        RSV_ADD_Exit_Selection = input("Please enter your selection here: ")
                            
                        if RSV_ADD_Exit_Selection == '1':
                
                            ADD_RSV_loop = False
                            ADD_RSV_selection_loop = False

                            os.system('cls')
                            print("Successfully returned to main menu.\n")
                            break

                        elif RSV_ADD_Exit_Selection == '2':
                            os.system('cls')
                            
                            ADD_RSV_selection_loop = False
                            print("Succesfully returned to add reservation program")
                            break
                        
                        else:
                            os.system('cls')
                            print("Error: Invalid selection!\nPlease use one of the given options (1-2) as your selection\nTry again.")

                elif RSV_Selection == '8':
                    os.system('cls')
                    while True:
                        print("Are you sure you wish to restart your the program process?\n[1] Yes\n[2] No")
                        RSV_ADD_Reset_Selection = input("Please enter your selection here: ")
                            
                        if RSV_ADD_Reset_Selection == '1':

                            #Used to revert all progress into blank data.
                            RSV_Date_input = ''
                            RSV_Slot_input = ''
                            RSV_Name_input = ''
                            RSV_Email_input = ''
                            RSV_PhoneNum_input = ''
                            RSV_Size_input = ''

                            os.system('cls')
                            RSV_ADD_selection_loop = False
                            print("Program restarted sucessfully")
                            break
        
                        elif RSV_ADD_Reset_Selection == '2':
                            ADD_RSV_selection_loop = False
                            os.system('cls')
                            print("Aborted program restart succesfully")
                            break
                        
                        else:
                            os.system('cls')
                            print("Error: Invalid selection!\nPlease use one of the given options (1-2) as your selection\nTry again.")
                            
                elif RSV_Selection == '9' or RSV_Selection == '10':
                    
                    if RSV_Date_input == '' or RSV_Slot_input == '' or FM2_RSV_Name_input == '' or RSV_Email_input == '' or RSV_PhoneNum_input == '' or RSV_Size_input == '':
                        
                        os.system('cls')
                        ADD_RSV_selection_loop = False
                        print("Error: Incomplete reservation details.\nThe reservation details cannot be added onto the text file with blank data.\nTry Again\n")
                    
                    else: 
                        if RSV_Selection == '9': 
                            ADD_Reservation()
                            os.system('cls')
                            print("Succesfully added the reservation details onto the reservation's text file.")
                            print("Program restarted sucessfully")
                            break
                        
                        else:
                            ADD_Reservation()
                            os.system('cls')
                            ADD_RSV_loop = False
                            break

                else:
                    os.system('cls')
                    print("Error: Invalid selection!\nPlease use the given options (1-10) as your selection.\nTry Again.\n")    
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
