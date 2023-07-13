#This code is to append more reservations onto the reservations.txt file.
#Coordinated with update reservation.py
import datetime
import os

def add_reservation(reservation_list):
  Add_rsv = [datetime, slot, name, email, phone_num, pax]
  print("\n--------------------------------------\nWelcome user to the Add Reservation submenu!")
  '''
  Error checking 1: In case user accidentally enters 1 when they did not intend to do so,
  the user can return to main menu when selection 2
  '''
  confirmation = True
  while confirmation == True:
      selection = input("Do you wish to proceed? \n[1]--Proceed? \n[2]--Return to main menu? \nEnter your selection: ")
      #Use of match case as it is simpler.                
      if selection == '1' or selection == '2':
          confirmation = False
      else: #Invalid entry
          print("Invalid entry, please try again\n")
          confirmation = True
  
  if selection == '1': #Proceed
      print("Proceeding \n--------------------------------------\n")
  elif selection == '2': #Return to main menu
      print("returning")
