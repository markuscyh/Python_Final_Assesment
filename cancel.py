# Function to cancel reservations
def cancel_reservation():
    print_reservations()
    
    reservations = []
        
    data = ''
    
    with open('reservation_21100649.txt', 'r') as f :
            data = f.readlines()
    
    for i in range(len(data)) :
        reservations.append(data[i])
    
    if not reservations:
        return
    else:
        while True:
            try:
                cancel_choice = int(input("\nEnter the number of the reservation you want to cancel (or 0 to go back): "))
                if cancel_choice == 0:
                    break
                elif cancel_choice < 1 or cancel_choice > len(reservations):
                    print("Invalid input. Please enter a valid reservation number.")
                else:
                    canceled_reservation = reservations.pop(cancel_choice - 1)
                    data = canceled_reservation.split('|')
                    print("Reservation for {} on {} at {} has been canceled.\n\n".format(data[2], data[0], data[1]))
                    print_reservations()
                    
                    with open('reservation_21100649.txt', 'w') as f :
                        for line in reservations :
                            f.write(line)
                            
            except ValueError:
                print("Invalid input. Please enter a valid reservation number.")
