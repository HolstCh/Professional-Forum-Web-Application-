from Database import mysql
from App import app
#Author: Aashik

#initialize class
class UnregisteredCompany:
    #set engg type data member (String)
    def __init__(self, engg):
        self.engg = engg
