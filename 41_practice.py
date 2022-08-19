class Train:
    def __init__(self):
        self.seats = 7800
        self.fare = 75


    def bookTickets(self):
        self.seats -= 1

    def getStatus(self):
        print(self.seats)

    def getFareInfo(self):
        print(self.fare)

tr = Train()
tr.getFareInfo()
tr.getStatus()
tr.bookTickets()
tr.getStatus()