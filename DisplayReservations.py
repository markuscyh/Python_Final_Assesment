from datetime import datetime, timedelta
import os


def datechecker(reservation_list_contents):
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

    return display_list

def printreservations(display_list):
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