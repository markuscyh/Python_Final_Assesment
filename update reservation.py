# Function to Edit/Update Reservation
import datetime
import os

def update_reservation(reservation_list):
    print('Update Reservation Selected')
    name = input('Enter Name To Update Reservation:')
    match_the_reservations = []
    for rsv in reservation_list:
        if rsv['name'] == name:
            match_the_reservations.append(rsv)
    # Function To Match The Reservation
    if match_the_reservations:
        print('Matched Reservation:')
        for i in range(len(match_the_reservations)):
            rsv = match_the_reservations[i]
            print(f"{i + 1}. {rsv['name']}, {rsv['date']}, {rsv['slot']}, {rsv['email']}, {rsv['phone_num']}")

        user_input = int(input('Enter The Number of The Reservation You Want To Update: ')) - 1
        if 0 <= user_input < len(match_the_reservations):
            rsv = match_the_reservations[user_input]
            print('Enter New Reservation Details (Leave Empty to Keep The Current Value):')

            # Function To Update Date
            while True:
                try:
                    current_date = datetime.datetime.strptime(rsv['date'], "%Y-%m-%d")
                    min_date = datetime.datetime.now() + datetime.timedelta(days=5)
                    new_date = input(f"Date ({rsv['date']} - Must Be At least 5 Days in Advance ):")
                    if new_date:
                        new_date = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                        if new_date < min_date:
                            print("Invalid Date. Date Must Be At least 5 Days in Advance.")
                            continue
                    else:
                        new_date = current_date
                    break

                except ValueError:
                    print('Invalid Date Format. Please Enter The Date in The Format YYY-MM-DD.')

            # Function To Update Time
            print("Available Slots:")
            print("1. 12:00 pm - 02:00 pm")
            print("2. 02:00 pm - 04:00 pm")
            print("3. 04:00 pm - 08:00 pm")
            print("4. 08:00 pm - 10:00 pm")

            while True:
                slot_pick = input(f"Slot ({rsv['slot']}):") or rsv['slot']
                if slot_pick not in ["1", "2", "3", "4"]:
                    print("Invalid Slot Number. Please Choose Available Slot Number.")

                else:
                    slot_list = {
                        "1: 12:00 pm - 02:00 pm",
                        "2: 02:00 pm - 04:00 pm",
                        "3: 04:00 pm - 08:00 pm",
                        "4: 08:00 pm - 10:00 pm"
                    }
                    new_slot = slot_list[slot_pick]
                    break

            new_name = input(f"Name ({rsv['name']}):") or rsv['name']
            new_email = input(f"Email ({rsv['email']}):") or rsv['email']
            new_phone = input(f"Phone ({rsv['phone']}):") or rsv['phone']
            # Function To Update Number of People
            while True:
                try:
                    new_people = int(input(f"Number of People ({rsv['people']}):")) or rsv['people']
                    if new_people <= 0 or new_people > 4:
                        print("Invalid Number of People. Maximum is 4 Per Reservation.")
                    else:
                        break
                except ValueError:
                    print("Invalid Input. Please Enter A Valid Number.")
            # Function To Check Session Availability
            session_count = sum(
                1 for reserve in reservation_list if reserve["date"] == new_date and reserve["slot"] == new_slot)
            if session_count >= 8:
                print("Sorry, The Selected Slot is Already Full. Please Choose A Different Slot.")
                return

            updated_reservation = {
                "date": new_date.strftime("%Y-%m-%d"),
                "slot": new_slot,
                "name": new_name,
                "phone": new_phone,
                "people": new_people
            }
            # Function To Replace Old Reservation
            reservation_list.remove(rsv)
            reservation_list.append(updated_reservation)
            write_reservations(reservation_list)
            print("Reservation Updated Successfully!")
        else:
            print("Invalid Reservation Number!")
    else:
        print("No Matching Reservation Found!")
        choice = input("Would You Like To Try Again? (Y/N): ")
        if choice.lower() == "y":
            update_reservation(reservation_list)


def write_reservations(reservations_list):
    with open("reservation_21100649.txt", "w") as f:
        for reservation in reservations_list:
            f.write(
                f"{reservation['name']}, {reservation['date']}, {reservation['slot']}, {reservation['email']}, {reservation['phone_num']}\n")


reservation_list_contents = []

main_menu_loop = True
while main_menu_loop:
    print(
        "\nWelcome to Charming Thyme Trattoria. Please type the number that corresponds to the option you would like to select")

    # This loop contains exception handling to help ensure that the proper input is entered
    loop = True
    while loop:
        print(
            "[1] Add Reservation \n[2] Cancel Reservation \n[3] Edit Reservations \n[4] Display Reservations \n[5] Generate Meal Recommendation \n[6] Exit")

        try:
            main_menu_input = int(input())
        except:
            print("Please enter a valid input. \n")
            print("--------------------------------------------------------------------------------\n")
        else:
            if main_menu_input < 1 or main_menu_input > 6:
                print("Please type the number that corresponds to the option you would like to select. \n")
                print("----------------------------------------------------------------------------\n")
            else:
                loop = False

    if main_menu_input == 1:
        pass
        # function
    elif main_menu_input == 2:
        pass
        # function
    elif main_menu_input == 3:
        update_reservation(reservation_list_contents)
        # function

    elif main_menu_input == 4:
        print("\n--------------------------------------------------------------------------------\n")
        list_count = 0
        for i in range(len(reservation_list_contents)):
            print(reservation_list_contents[list_count])
            list_count += 1
        # This input will allow the user to view the display list before returning to the main menu
        display_exit = input("Enter any word, number or symbol to return to the main menu: ")
        os.system('cls')
        print("\n--------------------------------------------------------------------------------\n")


    elif main_menu_input == 5:
        print("\n--------------------------------------------------------------------------------\n")
        # The while loop will allow the user to ask for a new recommendation or return to the main menu
        loop = True
        while loop:
            print(f"We recommend {meal_recommendation_generator()}")
            loop_question = "Would you like a new recommendation or return to the main menu? \n[1] Another recommendation \n[2] Exit \n"
            loop = main_menu_exit(loop_question)
        os.system('cls')
        print("\n--------------------------------------------------------------------------------\n")


    elif main_menu_input == 6:
        main_menu_loop = False

print("--------------------------------------------------------------------------------")
print("Thank you for using the program")
