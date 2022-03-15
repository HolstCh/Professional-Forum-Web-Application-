# Please make sure to run "pip install flask_mysqldb"!!!
from flask_mysqldb import MySQL
from App import app

try:
    # Fill out the following fields before running!!!
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "Your Username Here"
    app.config["MYSQL_PASSWORD"] = "Your Password Here"
    app.config["MYSQL_DB"] = "Your Database Name Here"

    mysql = MySQL(app)  # user this object for accessing database in multiple classes
except Exception as e:
    print(e)
