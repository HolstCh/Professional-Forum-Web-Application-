#Created by: Chloe Bouchard
#File name: Login.py
#Version: 1.0

import mysql.connector
debug = True

class Login:
    #Ctor for Login
    def __init__(self, username, password, connection):
        self.username = username
        self.password = password
        self.connection = connection
        

    #function to execute an SQL Query
    #Returns the Query result
    def executeQuery(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


    #Cross checks if a username and password correspond with eachother
    #return boolean result
    def authenticate(self):
        userQuery = "SELECT password FROM USERS WHERE username = '" + self.username + "';"
        result = self.executeQuery(userQuery)
        convert = str(result)
        convert = convert[3:len(convert) - 4] #remove useless characters from front and end
        if(self.password == convert):
            return 1 #password matches with the one in table
        elif (self.user_exist() == False):
            return 0 #username does not exist
        else:
            return -1 #password does not match
    

    #For debugging. Prints all users in the user Table
    def printUsers(self):
        userQuery = "SELECT username, password FROM USERS;"
        table_result = self.executeQuery(userQuery)
        for x in table_result:
            print(x)
    

    #check if user is already in the database table
    def user_exist(self):
        userQuery = "SELECT 1 FROM users WHERE username = '"+ self.username +"';"
        result = self.executeQuery(userQuery)
        if(len(result) == 0):
            return False
        else:
            return True


    #Adds user to the table, given a username and password
    #Returns false if request was not possible (usename already exists)
    def add_login(self):
        if(self.user_exist() == False):
            userQuery = "INSERT INTO USERS VALUES ('" + self.username + "','" + self.password+ "');"
            self.executeQuery(userQuery)
            print("added new user") #for debugging
            return True
        else:
            print("this username already exists") #for debugging
            return False
        

    #Sets the password. Can be used if a user wants to change their password
    def set_password(self,password):
        userQuery = "UPDATE users SET password = '"+password + "' WHERE username = '"+self.username +"';"
        self.executeQuery(userQuery)

    

if(debug == True):
    db_connection = mysql.connector.connect(host = "localhost", database = 'newdb', user = "root",passwd = "TestPass") #make sure to change password to correct one

    #---------------------------TEST 1---------------------------------------
    print("TEST 1")
    myLogin = Login('tester1', 'password1', db_connection) #create Login object
    myLogin.add_login()    #add object to database table

    if(myLogin.authenticate() == -1): #authentication should work
        print("The password does not match the username")
    elif (myLogin.authenticate() == 0):
        print("The username does not exist")
    else:
        print("the Login was successful")

    #--------------------------TEST 2-----------------------------------------------
    print("\nTEST 2")
    myLogin2 = Login('chloe646', 'other!',db_connection) #this Login is not added to the table, so it should fail the authentication
    if(myLogin2.authenticate() == -1): 
        print("The password does not match the username")
    elif (myLogin2.authenticate() == 0):
        print("The username does not exist") #should output this, since the username is not in the table
    else:
        print("the Login was successful")

    #---------------------------TEST 3--------------------------------------------
    print("\nTEST 3")
    myLogin3 = Login('tester1', 'password1',db_connection)  #this should not work, since tester1 already exists
    myLogin3.add_login()

    #---------------------------TEST 4---------------------------------------------
    print("\nTEST 4")
    myLogin4 = Login('tester3', 'password1',db_connection)  #this should be allowed
    myLogin4.add_login()
