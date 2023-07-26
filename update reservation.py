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
            edit_date = rsv_data[0]
            edit_slot = rsv_data[1]
            new_date_slot = (edit_date, edit_slot)
            count_date_slot[new_date_slot] = count_date_slot.get(new_date_slot, 0) + 1
    return count_date_slot


# Function to check if a string contains only letters
def contains_only_letters(input_str) :
    return all(char.isalpha() for char in input_str)


# Main menu loop
main_menu_loop = True
while main_menu_loop :
    print(
        "\nWelcome to Charming Thyme Trattoria. Please enter the number that corresponds to the option you would like to select")

    # This loop contains exception handling to ensure proper input is entered
    while True :
        print(
            "[1] Add Reservation \n[2] Cancel Reservation \n[3] Edit Reservations \n[4] Display Reservations \n[5] Generate Meal Recommendation \n[6] Exit")
        try :
            main_menu_input = int(input(">>> "))
        except ValueError :
            print("Please enter a valid input.")
        else :
            if 1 <= main_menu_input <= 6 :
                break
            else :
                print("Please type the number that corresponds to the option you would like to select.")

    if main_menu_input == 1 :
        pass
        # Function to add reservation

    elif main_menu_input == 2 :
        pass
        # Function to cancel reservation

    elif main_menu_input == 3 :
        # Code for updating reservations
        while True :
            reservation_name = input(
                "Enter Guest Name To Update The Reservation (leave blank to go back to main menu): ").strip().upper()
            if not reservation_name :
                break
            # Code to read from text file
            with open('reservation_21100649.txt', 'r') as f :
                data = f.readlines()
            matching_reservations = []

            for i in range(len(data)) :
                reservation_data = data[i].strip().split('|')
                if len(reservation_data) >= 3 and reservation_data[2].upper() == reservation_name :
                    matching_reservations.append(i)

            # Code if no reservation found in user input
            if not matching_reservations :
                print(f'{reservation_name} NOT FOUND')
                continue

            # Code for updating the reservation directly if there's only one matching reservation
            if len(matching_reservations) == 1 :
                selected_reservation_index = matching_reservations[0]
                reservation_info = data[selected_reservation_index].strip().split('|')
            else :
                print(f"Reservation List: {reservation_name}:")
                for i in range(len(matching_reservations)) :
                    reservation_index = matching_reservations[i]
                    reservation_info = data[reservation_index].strip().split('|')
                    print(f"{i + 1}) Reservation on {reservation_info[0]} at {reservation_info[1]}")

                while True :
                    try :
                        choice = int(input("Enter the number of the reservation you want to update: "))
                        if 1 <= choice <= len(matching_reservations) :
                            selected_reservation_index = matching_reservations[choice - 1]
                            reservation_info = data[selected_reservation_index].strip().split('|')
                            break
                        else :
                            print("Invalid choice! Please enter a valid number.")
                    except ValueError :
                        print("Invalid input! Please enter a number.")

            # Rest of the code for updating the reservation...
            while True :
                # Ask the user for the field they want to update
                print("\nSelect Field To Update:")
                print("1) Date\n2) Slot\n3) Name\n4) Email\n5) Contact\n6) Number of People")

                valid_choices = ['1', '2', '3', '4', '5', '6']
                user_update = input("Please choose a number (1-6) or 'N' to stop updating this reservation: ")

                # Code to update date
                if user_update in valid_choices :
                    if user_update == '1' :
                        while True :
                            try :
                                date = input("Enter New Date (yyyy-mm-dd): ")
                                chosen_date = datetime.strptime(date, "%Y-%m-%d").date()
                                today = datetime.now().date()
                                min_reservation_date = today + timedelta(
                                    days=5)  # Minimum reservation date 5 days in advance
                                if chosen_date < min_reservation_date :
                                    print("Invalid Date! Reservation Should Be Made At Least 5 Days in Advance.")
                                    continue

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
                    # Code to update slot
                    elif user_update == '2' :
                        while True :
                            slot = input("Enter New Slot from 1-4: ")
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
                    # Code to update name
                    elif user_update == '3' :
                        while True :
                            name_new = input("Enter New Name: ").strip().upper()
                            if name_new and contains_only_letters(name_new) :
                                update_reservation(selected_reservation_index, 2, name_new)
                                print("Name updated successfully.")
                                break
                            else :
                                print("Invalid Name! Please enter a valid name.")
                    # Code to update email
                    elif user_update == '4' :
                        while True :  # valid email code
                            email = input("Enter New Email: ").lower()
                            if email.endswith('@gmail.com') or email.endswith('@yahoo.com') or email.endswith(
                                    '@hotmail.com') :
                                update_reservation(selected_reservation_index, 3, email)
                                print("Email updated successfully.")
                                break
                            else :  # valid email code
                                print("Invalid Email! Only gmail, yahoo, and hotmail domains are accepted.")
                    # Code to update contact number
                    elif user_update == '5' :
                        while True :
                            contact = input("Enter New Contact Number: ")
                            if len(contact) == 10 and contact.isdigit() :
                                update_reservation(selected_reservation_index, 4, contact)
                                print("Contact Number updated successfully.")
                                break
                            else :  # contact number should be 10-digit code
                                print("Invalid Number! Contact Should Be a 10-Digit Number.")
                    # Code to update number of people
                    elif user_update == '6' :
                        while True :
                            num_people = input("Enter New Number of People: ")
                            if num_people in ['1', '2', '3', '4'] :
                                update_reservation(selected_reservation_index, 5, num_people)
                                print("Number of People updated successfully.")
                                break
                            else :  # maximum number of 4 people per reservation code
                                print("Invalid Number of People! Maximum is 4.")
                elif user_update.upper() == 'N' :
                    break
                else :
                    print("Invalid choice! Please enter a valid number (1-6) or 'N' to stop updating this reservation.")
                    continue

            # prompt user if they want to update another reservation
            any_more_reservations = input("Do You Have Another Reservation To Update? (Y/N): ").upper()
            if any_more_reservations != 'Y' :
                print("Reservation updated successfully")
                break  # return to the main menu

    elif main_menu_input == 4 :
        pass
        # Code for displaying reservations

    elif main_menu_input == 5 :
        pass
        # Code for generating meal recommendation

    elif main_menu_input == 6 :
        main_menu_loop = False

print("--------------------------------------------------------------------------------")
print("Thank you for using the program")




