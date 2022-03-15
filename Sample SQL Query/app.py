# Please make sure to run "pip install flask_mysqldb"!!!

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__)

# Fill out the following fields before running!!!
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]=""
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]=""

mysql=MySQL(app)

@app.route("/", methods=["POST", "GET"])
def sampleSearch():
    if request.method == "GET":
        return render_template("testPage.html")

    if request.method == "POST":
        fName=request.form["fName"]
        lName=request.form["lName"]
        email=request.form["email"]
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Profile WHERE firstName=%s AND lastName=%s AND email=%s", (fName, lName, email))
        result=cursor.fetchone()
        cursor.close()

        if result:
            return "<h1 style='color:green'> Found matching record! </h1>"
        else:
            return "<h1 style='color:red'> No matching records exist... </h1>"
# end of testPage

if __name__=='__main__':
    app.run()