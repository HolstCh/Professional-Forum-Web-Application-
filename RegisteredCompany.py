from Database import mysql
from App import app
#Author: Aashik

#initialize class
class RegisteredCompany:
    #set engg type data member (String)
    def __init__(self, email, phoneNo):
        self.email = email
        self.phoneNo = phoneNo

#Method to conttact User from the registered Company using their employee ID and a message
    def contactUser(self, employeeID, message):
        self.employeeID = employeeID
        self.message = message
