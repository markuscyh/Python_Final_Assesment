#This code is to append more reservations onto the reservations.txt file.
import datetime
import os

def add_reservation(reservation_list):
  print("\n--------------------------------------\nWelcome user to the Add Reservation submenu!")
  '''
  Error checking 1: In case user accidentally enters 1 when they did not intend to do so,
  the user can return to main menu when selection 2
  '''
  while confimration == True:
    selection = int(input("Do you wish to proceed? \n[1]--Proceed? \n[2]--Return to main menu? \nEnter your selection: ")
    #Use of match case as it is simpler.                
    match selection:
      case 1: #Proceed confirmed
        confirmation = False
        print("Proceeding...")
      
      case 2: #Return to main menu
        confirmation = False
      
      case _: #Invalid entry
        print("Invalid entry, please try again")
        confirmation = True
