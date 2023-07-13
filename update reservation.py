from datetime import datetime, timedelta


# Function to Edit/Update Reservation
def update_reservation(index, change) :
    for i in range(len(data)) :
        if reservation_name in data[i] :
            reservation_info = data[i].strip().split('|')
            reservation_info[index] = change
            data[i] = '|'.join(reservation_info)

    with open('reservation_22110670.txt', 'w') as f :
        for line in data :
            f.write(line)


# Main Menu
main_menu_loop = True
while main_menu_loop :
    print(
        "\nWelcome to Charming Thyme Trattoria. Please type the number that corresponds to the option you would like to select")

    # This loop contains exception handling to help ensure that the proper input is entered
    loop = True
    while loop :
        print(
            "[1] Add Reservation \n[2] Cancel Reservation \n[3] Edit Reservations \n[4] Display Reservations \n[5] Generate Meal Recommendation \n[6] Exit")

        try :
            main_menu_input = int(input())
        except :
            print("Please enter a valid input. \n")
            print("--------------------------------------------------------------------------------\n")
        else :
            if main_menu_input < 1 or main_menu_input > 6 :
                print("Please type the number that corresponds to the option you would like to select. \n")
                print("----------------------------------------------------------------------------\n")
            else :
                loop = False

    if main_menu_input == 1 :
        pass
        # function
    elif main_menu_input == 2 :
        pass
        # function
    elif main_menu_input == 3 :
        # Edit Reservation
        while True :
            reservation_name = input("Enter Guest Name To Update The Reservation:").upper()
            with open('reservation_22110670.txt', 'r') as f :
                data = f.readlines()
            names_in_file = []

            for name in data :
                name_parts = name.strip().split('|')
                if len(name_parts) >= 3 :
                    names_in_file.append(name_parts[2])

            while reservation_name not in names_in_file :
                print(f'{reservation_name} RESERVATION NOT FOUND!\n Please Enter The Correct Name:')
                reservation_name = input("Enter Guest Name To Update The Reservation!!!!!!!:").upper()

            any_changes = 'Y'  # Set any_changes to 'Y' initially to enter the loop

            while any_changes == 'Y' :
                # Ask the user for the field they want to change
                print("\nSelect Field To Update:")
                print("1) Date\n2) Slot\n3) Name\n4) Email\n5) Contact\n6) Number of People")

                valid_choice = ['1', '2', '3', '4', '5', '6']
                user_update = input("Please Choose A Number (1-6):")

            # Update or Edit Date
            if user_update == '1':
                while True:
                    try:
                        date = input("Enter New Date (yyyy-mm-dd):")
                        chosen_date = datetime.strptime(date, "%Y-%m-%d").date()
                        today = datetime.now().date()
                        min_reservation_date = today + timedelta(
                            days=5) #Minimum reservation date 5 days in advance
                        if chosen_date < min_reservation_date:
                            print("Invalid Date! Reservation Should Be Atleast 5 Days in Advance.")
                        else:
                            break
                    except ValueError:
                        print("Invalid Date Format! Please Enter The Date in The Format (yyyy-mm-dd).")

                update_reservation(0, data)

            # Update or Edit Slot
            if user_update == '2':
                slot = input("Enter New Slot (1-4):")
                while slot not in '1234':
                    print("Invalid Slot! Please Choose Between 1-4.")
                    slot = input("Enter New Slot (1-4):")
                slot = 'Slot' + slot
                update_reservation(1, slot)

            # Update or Edit Name
            if user_update == '3':
                new_name = input("Enter New Name:").upper()
                update_reservation(2, new_name)

            # Update or Edit Email
            if user_update == '4':
                new_email = input("Enter New Email:").lower()
                update_reservation(3, new_email)

            # Update or Edit Contact Number
            if user_update == '5':
                new_contact = input("Enter New Contact Number:")
                while len(new_contact) != 10 or not new_contact.isdigit():
                    print("Invalid Contact Number! Contact Should Be A 10-Digit Number.")
                    new_contact = input("Enter New Contact Number:")
                update_reservation(4, new_contact)

            # Update or Edit Number of People
            if user_update == '6':
                new_num_people = input("Enter New Number of People:")
                while new_num_people not in '1234':
                    print("Invalid Number of People! Maximum is 4 Per Reservation")
                    new_num_people = input("Enter New Number of People:")
                update_reservation(5, new_num_people)

            print()
            changes = input("Do You Have Any OTHER Changes To Be Made To Your Reservation? (Y/N):").upper()

            print("Reservation Updated Successfully!\n")

            more_changes = input("Do You Want To Update Another Reservation? (Y/N):").upper()
            if more_changes == 'N':
                break

    elif main_menu_input == 4 :
        pass

    elif main_menu_input == 5 :
        pass

    elif main_menu_input == 6 :
        main_menu_loop = False

print("--------------------------------------------------------------------------------")
print("Thank you for using the program")
