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