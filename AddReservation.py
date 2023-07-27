import random
import os
from datetime import datetime, timedelta

# This is the function to add the reservation onto the text file.
def ADD_Reservation():
    #Opens the text file in append mode.
    with open('reservation_21100649.txt', 'a') as ADD:
        #Prepares the reservation line.
        ADD_Reservation_str = ("{0}|{1}|{2}|{3}|{4}|{5}\n".format(FM_RSV_Date_input_final, RSV_Slot_input, FM2_RSV_Name_input, RSV_Email_input_final, RSV_PhoneNum_input_final, RSV_Size_input_final))
        #Appends the reservation line onto the text file
        ADD.write(ADD_Reservation_str)
        #Close file
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
except FileNotFoundError:
    main_menu_loop = False
    print("Reservation file not Found! Please contact management for assistance!")

# This block of code will create the list for the menu recommendation
try:
    with open("menuItems_21100649.txt", "r") as menu_list:
        menu_contents = menu_list.readlines()
except FileNotFoundError:
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
        os.system('cls')
        #Initial assigning of input variables.
        
        FM_RSV_Date_input_final = ''
        RSV_Slot_input = ''
        FM2_RSV_Name_input = ''
        RSV_Email_input_final = ''
        RSV_PhoneNum_input_final = ''
        RSV_Size_input_final = ''
        FM_RSV_DATE_input = ''

        RSV_Slot1_status = ''
        RSV_Slot2_status = ''
        RSV_Slot3_status = ''
        RSV_Slot4_status = ''

        Slot1_availble = 0
        Slot2_available = 0
        Slot3_available = 0
        Slot4_available = 0

        Slot1_count = 0
        Slot2_count = 0
        Slot3_count = 0
        Slot4_count = 0

        ADD_RSV_loop = True #The parent loop
        while ADD_RSV_loop:

            # It's for RSV_Name to remove symbols.
            forbidden_symbols = ['`','~','!','@','#','#','%','^','&','*','(',')','-','_','=','+',',','<','.','>','/','?',';',':','"','[',']','{','}','|']

            # IMPORTANT:
            # RSV stands for reservation
            # FM stands for formatted

            #Loop for the selection input section
            ADD_RSV_selection_loop = True
            
            #Submenu UI
            #Name of Submenu
            print("ADD RESERVATION SUBMENU\n") 

            #Display of Submenu UI
            print("Reservation details\n{6}\nReservation Date: {0}\n\nReservation Session Slot: {1}\n\nCustomer Name: {2}\n\nCustomer Email: {3}\n\nCustomer Phone Number: {4}\n\nReservation Size: {5}\n{6}\n".format(FM_RSV_Date_input_final, RSV_Slot_input, FM2_RSV_Name_input, RSV_Email_input_final, RSV_PhoneNum_input_final, RSV_Size_input_final,"------------------------------"))
            
            #Input options found on Submenu UI
            print("Please enter (or fix) the reservation details for:\n[1] Reservation Date\n[2] Reservation Session Slot (Done only after Reservation Date)\n[3] Customer Name\n[4] Customer Email\n[5] Customer Phone Number\n[6] Reservation Size\n\nOr would you like to:\n[7] Cancel the reservation process and return to main menu\n[8] Restart the reservation process\n[9] Add the reservation details and prepare another one\n[10] Add the reservation details and return to main menu\n")

            #Inner Loop 1
            while ADD_RSV_selection_loop:

                #User selects one of the options
                RSV_Selection = input("Please enter your selection from 1-10 here: ")
                
                #Reservation date has been chosen to be added.
                if RSV_Selection == '1':
                    
                    os.system('cls')
                    
                    #Getting the date of the reservation
                    while True:
                        #Get's today's date
                        today = datetime.now()

                        #Formats it to required format (YYYY-MM-DD)
                        FM_today = datetime.strftime(today, "%Y-%m-%d") 

                        #Used to see if entered date is 5 days in advance from today.
                        Date_minimum = today + timedelta(days=5)
                        
                        print("SELECTED RESERVATION DATE") #Subsection name
                        print("NOTICE!\nThe date of the reservation must be 5 days in advacned from today {0}\nThe escape code is today's date.\n".format(FM_today)) #otice
                        #Used to catch Value Error exception
                        
                        try:
                            #Subsection input
                            RSV_Date_input_initial = input("Please enter the date of the reservation in the format (YYYY-mm-dd): ")

                        #Catchses exception, allows program to keep functioning
                        except ValueError:
                            os.system('cls')
                            print("Error: Invalid date format!\nPlease enter the date of the reservation in (YYYY-mm-dd) format.\nTry Again\n")
                            
                        #No exceptions, then proceeding to add.
                        else:
                            try: #Tries to catch invalid input formats.
                                #Formats user input for logic comparison
                                FM_RSV_Date_input = datetime.strptime(RSV_Date_input_initial, "%Y-%m-%d")
                                FM_RSV_Date_input_1 = datetime.strptime(RSV_Date_input_initial, "%Y-%m-%d").date()
                                FM_RSV_Date_input_2 = datetime.strftime(FM_RSV_Date_input_1,"%Y-%m-%d")

                            except ValueError:
                                os.system('cls')
                                print("Error: Invalid date format!\nPlease enter the date of the reservation in the format (YYYY-MM-DD)\nTry Again\n")

                            else:
                                #If date input is not escape code, it will continue. Else, it will return to submenu.
                                if FM_RSV_Date_input_2 != FM_today:
                                    
                                    #Comparison. Forces user to choose a different date if true.
                                    if FM_RSV_Date_input < Date_minimum:
                                        os.system('cls')
                                        print("Error: Invalid date selected!\nYou can only apply for a reservation at least 5 days in advance from today\nPlease try again\n")
                                    
                                    #The date is 5 days or more ahead.
                                    else:
                                        #Formats input to presentable form
                                        RSV_Date_input_final = RSV_Date_input_initial
                                        FM2_RSV_Date_input = datetime.strptime(RSV_Date_input_final, "%Y-%m-%d").date()
                                        FM_RSV_Date_input_final = datetime.strftime(FM2_RSV_Date_input,"%Y-%m-%d")
                                        
                                        with open('reservation_21100649.txt', 'r') as dt:

                                            #Used to count how times does the inputted date occur.
                                            RSV_Date_data = dt.read()
                                            Date_count = RSV_Date_data.count(FM_RSV_Date_input_final)

                                            #Logic operation. If the inputted date appears 32 times, then the date is invalid as it is full of reservations.
                                            if Date_count != 32:
                                                ADD_RSV_selection_loop = False
                                                os.system('cls')
                                                print("Reservation date succesfully added")

                                                #In the case that the user resellects the date to edit it. This will automatically redefine the slot back to blank space, IF the selected slot on that date is full.
                                                if RSV_Slot_input == 'Slot 1' or RSV_Slot_input == 'Slot 2' or RSV_Slot_input == 'Slot 3' or RSV_Slot_input == 'Slot 4':
                                                        
                                                        with open('reservation_21100649.txt', 'r') as Slot:
                                                            slot_data = Slot.readlines()
                                                            for i in range(len(slot_data)):
                                                                slot_data2 = slot_data[i].strip().split('|')
                                                            
                                                                #Only concenrs the lines where the selected date occurs in the text file
                                                                if slot_data2[0] == FM_RSV_Date_input_final:

                                                                    #If specified slot appears, add 1 to the count.
                                                                    if slot_data2[1] == 'Slot 1':
                                                                        Slot1_count += 1

                                                                    elif slot_data2[1] == 'Slot 2':
                                                                        Slot2_count += 1
                                                                        
                                                                    elif slot_data2[1] == 'Slot 3':
                                                                        Slot3_count += 1

                                                                    elif slot_data2[1] == 'Slot 4':
                                                                        Slot4_count += 1

                                                            if RSV_Slot1_status == 8 and RSV_Slot_input == 'Slot 1':
                                                                RSV_Slot_input = ''

                                                            elif RSV_Slot2_status == 8 and RSV_Slot_input == 'Slot 2':
                                                                RSV_Slot_input = ''

                                                            elif RSV_Slot3_status == 8 and RSV_Slot_input == 'Slot 3':
                                                                RSV_Slot_input = ''

                                                            elif RSV_Slot4_status == 8 and RSV_Slot_input == 'Slot 4':
                                                                RSV_Slot_input = ''
                                                break
                                            #The date was full. (Occurred 32 times)
                                            else:
                                                print("Error: Selected date is full.\nThe selected date is full and has no more room for reservations.\nTry another date.\n")

                                #Returning to submenu succesfully.
                                else:
                                    ADD_RSV_selection_loop = False
                                    os.system('cls')
                                    break

                #Reservation slot has been chosen.
                elif RSV_Selection == '2':
                    
                    #Prevents user from entering this subsection as date MUST be entered beforehand.
                    if FM_RSV_Date_input_final == '':
                        os.system('cls')
                        print("Error: Invalid order!\nComplete the details for Reservation Date.\nPlease select a different option\n")
                        break
                    
                    #The date is entered.
                    else:
                        #The loop process. Used defined loop to make the loop breakable.
                        RSV_Slot_loop = True
                        while RSV_Slot_loop:

                            #Another defined loop for easier break. This section provides user with another UI.
                            RSV_Slot_Selection_loop = True

                            #Opens up text file for user to read the occurence of reservation date and its respective slot.
                            with open('reservation_21100649.txt', 'r') as Slot:
                                slot_data = Slot.readlines()

                                #Reads through all lines of the text file
                                #Converts each line into an array of information. slot_data2[0] is the date, and slot_data2[1] is the slot.
                                for i in range(len(slot_data)):
                                    slot_data2 = slot_data[i].strip().split('|')
                                    
                                    #Only concenrs the lines where the selected date occurs in the text file
                                    if slot_data2[0] == FM_RSV_Date_input_final:

                                        #If specified slot appears, add 1 to the count.
                                        if slot_data2[1] == 'Slot 1':
                                            Slot1_count += 1

                                        elif slot_data2[1] == 'Slot 2':
                                            Slot2_count += 1
                                            
                                        elif slot_data2[1] == 'Slot 3':
                                            Slot3_count += 1

                                        elif slot_data2[1] == 'Slot 4':
                                            Slot4_count += 1
                                    
                                    #The inputted date does not occur at all. Hence all session slots statuses are redefined as "EMPTY SLOT"
                                    else:
                                        RSV_Slot1_status = "EMPTY SLOT"
                                        RSV_Slot2_status = "EMPTY SLOT"
                                        RSV_Slot3_status = "EMPTY SLOT"
                                        RSV_Slot4_status = "EMPTY SLOT"

                                Slot.close() #Closes the textfile.
                            
                            #Used to redefine session slot statusses.
                            while True: #For Slot 1
                                
                                if Slot1_count > 0 :
                                    if Slot1_count == 8:
                                        RSV_Slot1_status = "FULL SLOT"

                                    else:
                                        Slot1_availble = 8 - Slot1_count
                                        RSV_Slot1_status = "{0} SLOT'S AVAILABLE".format(Slot1_availble)
                                else:
                                    RSV_Slot1_status = "EMPTY SLOT"
                                break
                            
                            while True: #For Slot 2
                                if Slot2_count > 0 :
                                    if Slot2_count == 8:
                                        RSV_Slot2_status = "FULL SLOT"

                                    else:
                                        Slot2_availble = 8 - Slot2_count
                                        RSV_Slot2_status = "{0} SLOT'S AVAILABLE".format(Slot2_availble)
                                else:
                                    RSV_Slot2_status = "EMPTY SLOT"
                                break
                            
                            while True: #For Slot 3
                                if Slot3_count > 0 :
                                    if Slot3_count == 8:
                                        RSV_Slot3_status = "FULL SLOT"

                                    else:
                                        Slot3_availble = 8 - Slot3_count
                                        RSV_Slot3_status = "{0} SLOT'S AVAILABLE".format(Slot3_availble)
                                else:
                                    RSV_Slot3_status = "EMPTY SLOT"
                                break
                            
                            while True: #For Slot 4
                                if Slot3_count > 0 :
                                    if Slot3_count == 8:
                                        RSV_Slot3_status = "FULL SLOT"

                                    else:
                                        Slot3_availble = 8 - Slot3_count
                                        RSV_Slot3_status = "{0} SLOT'S AVAILABLE".format(Slot3_availble)
                                else:
                                    RSV_Slot3_status = "EMPTY SLOT"
                                break

                            #UI presented to user. Displays date of reservation, status of the slots and how many are still available.
                            os.system('cls')
                            print("SELECTED RESERVATION SLOT\nNOTICE!\nEach session can accomodate a maximum of 8 reservations\nIf you entered here on accident, press 5 to return to the add reservation submenu\n")
                            print("Details of the reservation slots on {0}\n[1] Session 1: 12:00pm - 02:00pm | Status: {1}\n[2] Session 2: 02:00pm - 04:00pm | Status: {2}\n[3] Session 3: 06:00pm - 08:00pm | Status: {3}\n[4] Session 4: 08:00pm - 10:00pm | Status: {4}\n[5] Return to add reservation submenu".format(FM_RSV_Date_input_final, RSV_Slot1_status, RSV_Slot2_status, RSV_Slot3_status, RSV_Slot4_status))
                            while RSV_Slot_Selection_loop:
                                RSV_Slot_Selection = input("Please enter your selection here: ")
                                
                                #User selected first slot for reservation.
                                if RSV_Slot_Selection == '1':
                                    
                                    #If the slot is not full, then the input is accepted.
                                    if RSV_Slot1_status != 'SLOT FULL':
                                        RSV_Slot_input = "Slot 1" #Accepted input
                                        
                                        #Breaks named loops
                                        RSV_Slot_Selection_loop = False
                                        ADD_RSV_selection_loop = False
                                        RSV_Slot_loop = False

                                        os.system('cls')
                                        print("Reservation Slot sucessfully added")
                                        break #while True (UI) loop is broken 

                                    #Otherwise, input is rejected and user is forced to choose another slot.
                                    else:
                                        print("Error: Selected slot is full!\nEach reservation session slot supports 8 reservations maximum\nPlease select a reservation that has less than 8 reservations assigned\nTry again")
                                
                                #Second slot is selected.
                                elif RSV_Slot_Selection == '2':

                                    #If 2nd slot is not full, input is accepted.
                                    if RSV_Slot2_status != 'SLOT FULL':
                                        RSV_Slot_input = "Slot 2" #Accepted input

                                        #Named loops broken
                                        RSV_Slot_Selection_loop = False
                                        ADD_RSV_selection_loop = False
                                        RSV_Slot_loop = False

                                        os.system('cls')
                                        print("Reservation Slot sucessfully added")
                                        break #while True (UI) loop is broken 
                                    
                                    #Input rejected as slot is full.
                                    else:
                                        print("Error: Selected slot is full!\nEach reservation session slot supports 8 reservations maximum\nPlease select a reservation that has less than 8 reservations assigned\nTry again")

                                #Slot 3 selected
                                elif RSV_Slot_Selection == '3':

                                    #Accepts input only if Slot 3 IS NOT Full.
                                    if RSV_Slot3_status != 'SLOT FULL':

                                        #Accepted input
                                        RSV_Slot_input = "Slot 3"

                                        #Named loops broken.
                                        RSV_Slot_Selection_loop = False
                                        ADD_RSV_selection_loop = False
                                        RSV_Slot_loop = False

                                        os.system('cls')
                                        print("Reservation Slot sucessfully added")
                                        break #while True (UI) loop is broken 

                                    #Rejected input, slot full.
                                    else:
                                        print("Error: Selected slot is full!\nEach reservation session slot supports 8 reservations maximum\nPlease select a reservation that has less than 8 reservations assigned\nTry again")

                                #Slot 4 is selected.
                                elif RSV_Slot_Selection == '4':
                                    
                                    #Only accepts input if Slot 4 IS NOT full.
                                    if RSV_Slot2_status != 'SLOT FULL':
                                        #Accepted input
                                        RSV_Slot_input = "Slot 4"

                                        #Named (defined) loops are broken
                                        RSV_Slot_Selection_loop = False
                                        ADD_RSV_selection_loop = False
                                        RSV_Slot_loop = False

                                        os.system('cls')
                                        print("Reservation Slot sucessfully added")
                                        break #while True (UI) loop is broken 

                                    #Rejected input, slot full.
                                    else:
                                        print("Error: Selected slot is full!\nEach reservation session slot supports 8 reservations maximum\nPlease select a reservation that has less than 8 reservations assigned\nTry again")

                                #Escape input entered.
                                elif RSV_Slot_Selection == '5':

                                    #Breaks named loops
                                    RSV_Slot_Selection_loop = False
                                    ADD_RSV_selection_loop = False
                                    RSV_Slot_loop = False

                                    os.system('cls')

                                    break #Breaks while True (UI) loop

                                #User's selection was invalid, therfore they need to re-enter it.
                                else:
                                    print("Error: Invalid selection!\nPlease use one of the given options (1-5) as your selection\nTry again")
                                    RSV_Slot_Selection_loop = False
                                    break
                
                #Customer name is selected
                elif RSV_Selection == '3':
                    os.system('cls')
                    while True: #Subsection loop

                        #Subsection name                   
                        print("SELECTED CUSTOMER NAME")

                        #Subsection prompts
                        print("NOTICE!\nOne customer name per reservation slot.\nEnsure that there are no symbols or numbers in the customer's name as they will automatically be removed.\nThe escape code is 'ESCAPE'\n")
                        
                        #Input
                        RSV_Name_input = input("Please enter the customer's name: ").upper()

                        #If escape input entered, returns to ADD submenu.
                        if RSV_Name_input == 'ESCAPE':
                            os.system('cls')
                            ADD_RSV_selection_loop = False
                            break
                            
                        #Else, it proceeds.
                        else:
                            #Formats customer name. Removes digits and symbols (forbidden_symbols) used.
                            FM_RSV_Name_input = ''.join((x for x in RSV_Name_input if not x.isdigit()))
                            
                            FM2_RSV_Name_input = ''.join(x for x in FM_RSV_Name_input if not x in forbidden_symbols)

                            #If name has at least 2 letters, it is valid.
                            if len(FM2_RSV_Name_input) >=2:

                                #Input accepted
                                ADD_RSV_selection_loop = False
                                os.system('cls')
                                print("Customer Name has been succesfully added")
                                break
                            
                            #Input is rejected. 
                            else: 
                                os.system('cls')
                                print("Error: No name entered!\nPlease enter a valid name!.\nTry again.\n")
        
                #Customer email is selected.
                elif RSV_Selection == '4':
                    os.system('cls')
                    #Getting the customer's email
                    while True:             

                        #Subsection name
                        print("SELECTED CUSTOMER EMAIL")

                        #Subsection prompt
                        print("NOTICE!\nEmail must be in correct format (E.g ExampleEmail@gmail.com)\ngmail, hotmail and yahoo domains are supported.\nThe escape code is 'ESCAPE'")
                        
                        #Input
                        RSV_Email_input_initial = input("Please enter the customer's email address: ")
                        
                        #If escape input is entered, the user returns to submenu.
                        if RSV_Email_input_initial != 'ESCAPE': #Escape input was not entered.
                            
                            #_final is used so that the input is presentable.
                            

                            #Input is only valid if the following domains are included. Other domains are rejected as well as a lack of domain.
                            if RSV_Email_input_initial.endswith("@gmail.com") or RSV_Email_input_initial.endswith("@yahoo.com") or RSV_Email_input_initial.endswith("@hotmail.com"):
                                
                                #Input is invalid if 2 or more email domains are found.
                                #If all 3
                                if "@gmail.com" in RSV_Email_input_initial and "@yahoo.com" in RSV_Email_input_initial and "@hotmail.com" in RSV_Email_input_initial:
                                    os.system('cls')
                                    print("Error: Invalid customer email.\nOnly 1 email domain can be supported in the email.\nTry again.\n")
                                
                                #If gmail and other (yahoo or hotmail)
                                elif "@gmail.com" in RSV_Email_input_initial and "@yahoo.com" in RSV_Email_input_initial or "@gmail.com" in RSV_Email_input_initial and "@hotmail.com" in RSV_Email_input_initial:
                                    os.system('cls')
                                    print("Error: Invalid customer email.\nOnly 1 email domain can be supported in the email.\nTry again.\n")

                                #If yahoo and hotmail
                                elif "@yahoo.com" in RSV_Email_input_initial and "@hotmail.com" in RSV_Email_input_initial:
                                    os.system('cls')
                                    print("Error: Invalid customer email.\nOnly 1 email domain can be supported in the email.\nTry again.\n")

                                #Invalid input if the email starts with the domains.
                                elif RSV_Email_input_initial.startswith("@gmail.com") or RSV_Email_input_initial.startswith("@yahoo.com") or RSV_Email_input_initial.startswith("@hotmail.com"):
                                    os.system('cls')
                                    print("Error: Invalid customer email.\nDomain name alone was enterred and it is not sufficient.\nTry again.\n")

                                else:
                                    #Input is valid.
                                    RSV_Email_input_final = RSV_Email_input_initial
                                    ADD_RSV_selection_loop = False
                                    os.system('cls')
                                    print("Customer Email succesfully added")
                                    break
                                
                            #Lacks email domain, therfore rejecting input and restart.
                            else:
                                os.system('cls')
                                print("Error: Invalid email. Email must either use gmail, yahoo, or hotmail domains.\nTry again.\n")

                        #Returning to submenu succesfully.
                        else:
                            ADD_RSV_selection_loop = False
                            os.system('cls')
                            break 

                elif RSV_Selection == '5':
                    os.system('cls')
                    #Getting the customer's contact number
                    while True:

                        #Subsection name
                        print("SELECTED CUSTOMER CONTACT NUMBER")

                        #Subsection prompt
                        print("NOTICE!\n1.Customer contact number MUST be 10 digits long.\n2.Must start with 01.\nThe escape code is '0'")
                        
                        #Input
                        RSV_PhoneNum_input_initial = input("Please enter the customer's contact number: ")

                        #If input is not escape entry, proceeds. Else returns to submenu.
                        if RSV_PhoneNum_input_initial != '0':   
                            
                            #It is only valid if the phone number is 10 characters long, is a digit, and starts with 01.
                            
                            #Must be 10 digits long
                            if len(RSV_PhoneNum_input_initial) == 10:
                                
                                #Must be digits
                                if RSV_PhoneNum_input_initial.isdigit():
                                    
                                    #Must start with 01
                                    if RSV_PhoneNum_input_initial.startswith("01"):
                                        
                                        #Input is valid
                                        ADD_RSV_selection_loop = False
                                        RSV_PhoneNum_input_final = RSV_PhoneNum_input_initial
                                        os.system('cls')
                                        print("Customer Phone Number succesfully added")
                                        break

                                    #Input rejected, invalid phone number start
                                    else: 
                                        os.system('cls')
                                        print("Error: Invalid customer phone number!\nCustomer phone numbers can only start with '01'\nTry again.\n")
                                
                                #Input rejected, phone number is not digit.
                                else:
                                    os.system('cls')
                                    print("Error: Invalid customer phone number format!\nCustomer phone numbers can only be digits.\nTry again.\n")
                            
                            #Input rejected, phone number lenght is not 10
                            else:
                                os.system('cls')
                                print("Error: Invalid customer phone number length!\nCustomer phone numbers can only be 10 digits long.\nTry again\n")
                        
                        #Returning to submenu succesfully.
                        else:
                            ADD_RSV_selection_loop = False
                            os.system('cls')
                            break

                elif RSV_Selection == '6':
                    os.system('cls')
                    
                    #Getting the reservation size.
                    while True:
                        #Subsection name
                        print("SELECTED RESERVATION SIZE")
                        #Subsection prompt
                        print("NOTICE!\nThe reservation size cannot be more than 4.\nThe escape code is '0'")
                        
                        #Because input is integer. Prepared to catch exception
                        try:
                            #Input
                            RSV_Size_input_initial = int(input("Please enter the size of the reservation slot: "))
                        
                        #Exception caught, program functions. User is to re-enter the input
                        except:
                            print("Error: Invalid input format.\nThe system only accepts integer values for reservation size\nTry again.\n")
                        
                        #No exception, proceed
                        else: 
                            
                            #If escape input is not entered, code proceeds.
                            if RSV_Size_input_initial != 0:

                                #Checks if ResPax has at least 1 person or a maximum of 4 people, or anything in between.
                                if RSV_Size_input_initial < 1:
                                    os.system('cls')
                                    print("Error: Invalid size input.\nReservation slots can never have 0 people.\nTry again\n")

                                elif RSV_Size_input_initial > 4:
                                    os.system('cls')
                                    print("Error: Invalid size input.\nReservation slots support a maximum of 4 people per slot.\nTry again\n")

                                #Input is accepted
                                else:
                                    RSV_Size_input_final = RSV_Size_input_initial
                                    ADD_RSV_selection_loop = False
                                    os.system('cls')
                                    print("Reservation Size has been succesfully added/updated\n")
                                    break

                            #Returns to submenu
                            else:
                                os.system('cls')
                                ADD_RSV_selection_loop = False
                                break
                
                #Return to Main menu selected
                elif RSV_Selection == '7': 
                    
                    #Used to double check, to ensure that data is not lost by accident.
                    while True:
                        os.system('cls')
                        print("SELECTED CANCEL ADD RESERVATION PROGRAM")
                        print("Are you sure you wish to cancel the add reservation process and return to main menu?\nYour progress will not be saved, and therefore need to be entered again.\n[1] Yes, return to Main Menu\n[2] No, remain in program\n")
                        RSV_ADD_Exit_Selection = input("Please enter your selection here: ")
                        
                        #User succesfully returns to main menu
                        if RSV_ADD_Exit_Selection == '1':
                
                            ADD_RSV_loop = False #Parent loop is broken
                            ADD_RSV_selection_loop = False

                            os.system('cls')
                            break
                        
                        #User does not return to main menu
                        elif RSV_ADD_Exit_Selection == '2':
                            os.system('cls')
                            
                            ADD_RSV_selection_loop = False
                            print("Succesfully returned to add reservation program")
                            break
                        
                        #Invalid selection
                        else:
                            os.system('cls')
                            print("Error: Invalid selection!\nPlease use one of the given options (1-2) as your selection\nTry again.\n")

                #User selects to reset the reservation details
                elif RSV_Selection == '8':
                    os.system('cls')

                    #Used to double check to ensure that data is not lost by accident.
                    while True:
                        print("SELECTED RESTART ADD RESERVATION PROGRESS")
                        print("Are you sure you wish to restart your process?\n[1] Yes\n[2] No\n")
                        RSV_ADD_Reset_Selection = input("Please enter your selection here: ")
                        
                        #Succesfully restarts
                        if RSV_ADD_Reset_Selection == '1':

                            #Used to revert all progress into blank data.
                            FM_RSV_Date_input_final = ''
                            FM2_RSV_Name_input = ''
                            RSV_Slot_input = ''
                            RSV_Email_input_final = ''
                            RSV_PhoneNum_input_final = ''
                            RSV_Size_input_final = ''

                            os.system('cls')
                            ADD_RSV_selection_loop = False
                            print("Progress restarted sucessfully")
                            break
                        
                        #Returns to submenu
                        elif RSV_ADD_Reset_Selection == '2':
                            ADD_RSV_selection_loop = False
                            os.system('cls')
                            print("Aborted progress restart succesfully")
                            break
                        
                        #Invalid selection
                        else:
                            os.system('cls')
                            print("Error: Invalid selection!\nPlease use one of the given options (1-2) as your selection\nTry again.\n")
                
                #User wishes to append the reservation onto the text file
                elif RSV_Selection == '9' or RSV_Selection == '10':
                    
                    #To append to text file, ALL DETAILS MUST NOT BE BLANK SPACE
                    if FM_RSV_Date_input_final == '' or RSV_Slot_input == '' or FM2_RSV_Name_input == '' or RSV_Email_input_final == '' or RSV_PhoneNum_input_final == '' or RSV_Size_input_final == '':
                        
                        os.system('cls')
                        ADD_RSV_selection_loop = False
                        print("Error: Incomplete reservation details.\nThe reservation details cannot be added onto the text file with blank data.\nTry Again\n")
                    
                    #All details enterred.
                    else: 
                        #User has selected 9
                        #User adds reservation and system prepares for another one by redefining all details to blank space
                        if RSV_Selection == '9': 
                            
                            ADD_Reservation() #To append to text file

                            #To revert all progress back into blank data.
                            RSV_Date_input_final = ''
                            RSV_Slot_input = ''
                            FM2_RSV_Name_input = ''
                            RSV_Email_input_final = ''
                            RSV_PhoneNum_input_final = ''
                            RSV_Size_input_final = ''

                            RSV_Slot1_status = ''
                            RSV_Slot2_status = ''
                            RSV_Slot3_status = ''
                            RSV_Slot4_status = ''

                            Slot1_availble = 0
                            Slot2_available = 0
                            Slot3_available = 0
                            Slot4_available = 0

                            Slot1_count = 0
                            Slot2_count = 0
                            Slot3_count = 0
                            Slot4_count = 0

                            #Feedback
                            os.system('cls')
                            print("Succesfully added the reservation details onto the reservation's text file.")
                            print("Program restarted sucessfully")
                            break
                        
                        #User selected 10.
                        #User adds reservation, and system returns user to the main menu.
                        else:
                            ADD_Reservation()
                            os.system('cls')
                            ADD_RSV_loop = False
                            break
                
                #Invalid selection
                else:
                    os.system('cls')
                    print("Error: Invalid selection!\nPlease use the given options (1-10) as your selection.\nTry Again.\n")    
                    break

        
    elif main_menu_input == 2:
        reservations = []
        
        data = ''
    
        with open('reservation_21100649.txt', 'r') as f :
                data = f.readlines()
    
        for i in range(len(data)) :
            reservations.append(data[i])
    
        if not reservations:
            print("No reservations to delete. Please add some reservations")
            break
        else:
            while True:
                try:
                    print("Reservations:")
                    reservations.sort()
                    for i, reservation in enumerate(reservations, 1):
                        data = reservation.split('|')
                        print("{} : Date - [{}] || Session - [{}] || Name - [{}]".format(i, data[0], data[1], data[2]))
                    cancel_choice = int(input("\nEnter the number of the reservation you want to cancel (or 0 to go back): "))
                    if cancel_choice == 0:
                        break
                    elif cancel_choice < 1 or cancel_choice > len(reservations):
                        print("Invalid input. Please enter a valid reservation number.")
                    else:
                        canceled_reservation = reservations.pop(cancel_choice - 1)
                        data = canceled_reservation.split('|')
                        print("Reservation for {} on {} at {} has been canceled.\n\n".format(data[2], data[0], data[1]))
                    
                        with open('reservation_21100649.txt', 'w') as f :
                            for line in reservations :
                                f.write(line)
                            
                except ValueError:
                    print("Invalid input. Please enter a valid reservation number.")

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
        loop = True
        while loop:
            continue_question = "Do you want to proceed? Please choose the corresponding number (1-2) of your option \n[1] Continue \n[2] Return to Main Menu \n>>> "
            loop = menu_exit(continue_question)
            
            if loop == False:
                os.system('cls')
                break
            
            if loop == True:
            # This block asks the user to enter the date of the reservations that they want to see
                display_list = []
                while True:
                    try:
                        date = input("\nEnter the date (yyyy-mm-dd) of the reservations you want to see (yyyy-mm-dd)\n>>> ")
                        chosen_date = datetime.strptime(date, "%Y-%m-%d").date()
                        date = datetime.strftime(chosen_date, "%Y-%m-%d")
                        date_exists = False
                        for i in range(len(reservation_list_contents)):
                            if date in reservation_list_contents[i]:
                                display_list.append(reservation_list_contents[i])
                                date_exists = True
                        if date_exists == True:
                            break
                        if date_exists == False:
                            print("\nThere is no reservation on that date")
                    except ValueError:
                        print("\nPlease enter a valid date \n")

                # This block displays the list of reservations
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
            break

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
