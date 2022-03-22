from Database import mysql
from App import app


class Filter:
    def professionType(self, listOfTuples, profession):
        result = [tuple for tuple in listOfTuples if profession == tuple[7]]
        return result

    def isProfessionCategory(self):
        return True

    # sort posts by newest
    # def sortByDate(self):
    #     list.sort()

    # #sort posts by highest votes
    # def sortByVotes(self):

    # #search for post by account
    # def searchByAccount(self, account):

    # #search for tags
    # def searchByTag(self, tag):

    # #search by category of profession
    # def searchByProfessionCategory(self, category):

    # #search by specific company
    # def searchByCompany(self, company):
