scandinaviaSeats = 200
emiratesSeats = 200
dutchSeats = 200
virginSeats = 200
britishSeats = 200

scandinavia1 = "Scandinavian Airline"
emirates1 = "Emirates Airways"
dutch1 = "Dutch Airways"
virgin1 = "Virgin Airline"
british1 = "British Airways"

hotel1 = "Four Seasons"
hotel2 = "Marriott International"
hotel3 = "Hilton Resort"

scandinaviaPrice = 50
emiratesPrice = 90
dutchPrice = 60
virginPrice = 40
britishPrice = 70

bookFlight = input("Would you like to book a flight with us? ")

if bookFlight.lower() == "yes":
    print("Choose Flight")
    if scandinaviaSeats >= 1:
        print(scandinavia1)
    if emiratesSeats >= 1:
        print(emirates1)
    if dutchSeats >= 1:
        print(dutch1)
    if virginSeats >= 1:
        print(virgin1)
    if britishSeats >= 1:
        print(british1)
    else:
        print("No flights available at the moment")

chooseFlight = int(input("Choose your airline"))
availableFlights = [scandinavia1, emirates1, dutch1, virgin1, british1]
if chooseFlight >= 1 and chooseFlight <= 5:
    if chooseFlight == 1:
        ticketPrice = scandinaviaPrice
    elif chooseFlight == 2:
        ticketPrice = emiratesPrice
    elif chooseFlight == 3:
        ticketPrice = dutchPrice
    elif chooseFlight == 4:
        ticketPrice = virginPrice
    else:
        ticketPrice = britishPrice
    print("Your flight is: ", availableFlights[chooseFlight-1])
else:
    print("You did not choose")

buyTicket = int(input("Choose the number of flyers"))
print("Your ticket price is $",buyTicket*ticketPrice)

bookHotel = input("Would you like to book a hotel with us: ")
if bookHotel.lower() == "yes":
    print("Choose your stay", "\n", hotel1, "\n", hotel2, "\n", hotel3)

chooseHotel=int(input("Choose your hotel"))
availableHotels = [hotel1, hotel2, hotel3]
if chooseHotel >= 1 and chooseHotel <= 3:
    print("Your hotel is: ", availableHotels[chooseHotel-1])
else:
    print("You did not choose")
