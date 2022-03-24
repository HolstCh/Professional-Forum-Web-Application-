from Database import mysql
from App import app

class Filter:
    def professionType(self, listOfTuples, profession):
        result = [tuple for tuple in listOfTuples if profession == tuple[7]]
        return result
