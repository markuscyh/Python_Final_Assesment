# Function to cancel reservations
def cancel_reservation():
    reservations = []

    data = ''

    with open('reservation_21100649.txt', 'r') as f:
        data = f.readlines()

    for i in range(len(data)):
        reservations.append(data[i])

    if not reservations:
        print("No reservations available.")
        return
    else:

        print("Reservations:")
        for i, reservation in enumerate(reservations, 1):
            data = reservation.split('|')
            print("{} : Date - [{}] || Session - [{}] || Name - [{}]".format(i, data[0], data[1], data[2]))

        while True:
            try:
                cancel_choice = int(input("Enter the number of the reservation you want to cancel (or 0 to go back): "))
                if cancel_choice == 0:
                    break
                elif cancel_choice < 1 or cancel_choice > len(reservations):
                    print("Invalid input. Please enter a valid reservation number.")
                else:
                    canceled_reservation = reservations.pop(cancel_choice - 1)
                    data = canceled_reservation.split('|')
                    print("Reservation for {} on {} at {} has been canceled.".format(data[2], data[0], data[1]))

                    with open('reservation_21100649.txt', 'w') as f:
                        for line in reservations:
                            f.write(line)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid reservation number.")