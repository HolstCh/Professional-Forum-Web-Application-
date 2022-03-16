from Database import mysql
from App import app
#Author: Aashik

#initialize class
class RegisteredCompany:
    #set engg type data member (String)
    def __init__(self, email, phoneNo):
        self.email = email
        self.phoneNo = phoneNo

    def contactUser(self, employeeID, message):
        self.employeeID = employeeID
        self.message = message
