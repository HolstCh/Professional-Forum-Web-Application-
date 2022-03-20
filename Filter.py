import pymysql.cursors

from Database import mysql
from App import app


class Filter:
    def __init__(self, stringInput):
        self.stringInput = stringInput
        self.keywordsList = self.stringInput.split(" ")

    def searchKeywords(self):
        global completeMatch
        try:
            cursor = mysql.connection.cursor()
            query = "SELECT * FROM QUESTION_POST WHERE Title LIKE " + "'%" + self.stringInput + "%'"
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) == 0:
                completeMatch = False
                print(self.keywordsList)
                print('No complete question match found in searchKeywords()')
            else:
                return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()

        if completeMatch is False:
            if len(self.keywordsList) == 1:
                try:
                    cursor = mysql.connection.cursor()
                    query = "SELECT * FROM QUESTION_POST WHERE Title LIKE " + "'%" + self.keywordsList[0] + "%'"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                except Exception as e:
                    print(e)
                    print('No single keyword match')
                finally:
                    cursor.close()
            elif len(self.keywordsList) == 2:
                try:
                    cursor = mysql.connection.cursor()
                    query = "SELECT * FROM QUESTION_POST WHERE Title LIKE " + "'%" + self.keywordsList[0] + "%' OR Title Like " \
                    "'%" + self.keywordsList[1] + "%'"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                except Exception as e:
                    print(e)
                    print('No two keyword match')
                finally:
                    cursor.close()
            elif len(self.keywordsList) == 3:
                try:
                    cursor = mysql.connection.cursor()
                    query = "SELECT * FROM QUESTION_POST WHERE Title LIKE " + "'%" + self.keywordsList[0] + "%' OR Title LIKE " \
                    "'%" + self.keywordsList[1] + "%' OR Title LIKE "\
                    "'%" + self.keywordsList[2] + "%'"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                except Exception as e:
                    print(e)
                    print('No three keyword match')
                finally:
                    cursor.close()
            elif len(self.keywordsList) == 4:
                try:
                    cursor = mysql.connection.cursor()
                    query = "SELECT * FROM QUESTION_POST WHERE Title LIKE " + "'%" + self.keywordsList[0] + "%' OR Title LIKE "\
                            "'%" + self.keywordsList[1] + "%' OR Title LIKE "\
                            "'%" + self.keywordsList[2] + "%' OR Title LIKE "\
                            "'%" + self.keywordsList[3] + "%'"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                except Exception as e:
                    print(e)
                    print('No four keyword match')
                finally:
                    cursor.close()
            elif len(self.keywordsList) >= 5:
                try:
                    cursor = mysql.connection.cursor()
                    query = "SELECT * FROM QUESTION_POST WHERE Title LIKE " + "'%" + self.keywordsList[0] + "%' OR Title LIKE " \
                            "'%" + self.keywordsList[1] + "%' OR Title LIKE "\
                            "'%" + self.keywordsList[2] + "%' OR Title LIKE "\
                            "'%" + self.keywordsList[3] + "%' OR Title LIKE "\
                            "'%" + self.keywordsList[4] + "%'"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                except Exception as e:
                    print(e)
                    print('No five keyword or more match')
                finally:
                    cursor.close()

    def isProfession(self):
        return True

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
