# Please make sure to run "pip install flask_mysqldb"!!!
from flask_mysqldb import MySQL
from App import app

class Database:
    def getMySQL(self):
        try:
            # Fill out the following fields before running!!! Note: the deployed version of the web application has its own credentials for the database
            app.config["MYSQL_HOST"] = "Your Host"
            app.config["MYSQL_USER"] = "Your Username"
            app.config["MYSQL_PASSWORD"] = "Your Password"
            app.config["MYSQL_DB"] = "Your Database Name"

            mysql = MySQL(app)  # user this object for accessing database in multiple classes
            return mysql
        except Exception as e:
            print(e)


myData = Database()
mysql = myData.getMySQL()
