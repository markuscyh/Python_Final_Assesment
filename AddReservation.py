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

