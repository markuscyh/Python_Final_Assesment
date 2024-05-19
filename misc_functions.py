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


# Function to check if a string contains only letters
def contains_only_letters(input_str) :
    return all(char.isalpha() for char in input_str)


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