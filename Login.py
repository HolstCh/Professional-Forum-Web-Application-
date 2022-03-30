#Created by: Chloe Bouchard
#File name: Login.py
#Version: 1.1

from App import app

class Login:
    #Ctor for Login
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    # Check if username and password combination exists
    def validate(self):
        query = "SELECT * FROM Users WHERE Username='" + self.username + "' AND Password='" + self.password + "'"
        result=self.executeQuery(query)
        
        return result   
        

    #function to execute an SQL Query
    #Returns the Query result
    def executeQuery(self,query):
        from Database import mysql
#         connection = mysql.connector.connect(host = "localhost", database = 'newdb', user = "root",passwd = "replace with your own password") #make sure to change password to correct one

        cursor = mysql.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        mysql.connection.commit()
        return result
        

    #For debugging. Prints all users in the user Table
    def printUsers(self):
        userQuery = "SELECT Username, Password FROM Users;"
        table_result = self.executeQuery(userQuery)

        for x in table_result:
            print(x)
    

    #check if user is already in the database table
    def user_exist(self):
        userQuery = "SELECT 1 FROM Users WHERE Username = '"+ self.username +"';"
        result = self.executeQuery(userQuery)

        if(len(result) == 0):
            return False
        else:
            return True


    #Adds user to the table, given a username and password
    #Returns false if request was not possible (usename already exists)
    def add_login(self):
        if(self.user_exist() == False):
            userQuery = "INSERT INTO Users VALUES ('" + self.username + "','" + self.password+ "');"
            self.executeQuery(userQuery)
            print("added new user") #for debugging

            return True

        else:
            print("this username already exists") #for debugging

            return False
        

    #Sets the password. Can be used if a user wants to change their password
    def set_password(self,password):
        userQuery = "UPDATE Users SET Password = '"+password + "' WHERE Username = '"+self.username +"';"
        self.executeQuery(userQuery)
