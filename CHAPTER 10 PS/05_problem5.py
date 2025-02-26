import random


class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in Trian no. {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Trian no. {self.trainNo} is running successfully!")
    
    def getFare(self, fro, to):
        print(f"Ticket fare in Trian no. {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}") 
        