# To run server:
#   1. cd "C:\Users\coolp\Documents\Dylan\School\Y3 - 2022 WINTER\SENG 401 - Software Architecture\Project\test"
#   2. python -m venv test
#   3. scripts\activate
#   4. python -m flask run

# Installation commands:
#   > python -m pip install flask
#   > python -m pip install flask_mysqldb

from flask import Flask, render_template, request, redirect, jsonify
from flask_mysqldb import MySQL
from datetime import datetime
import json, sys

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'draGGun.!382'
app.config['MYSQL_DB'] = 'seng401'

mysql=MySQL(app)

@app.route("/", methods=["GET", "POST"])
def display():
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users")
    results=cursor.fetchall()

    if request.method == "GET":
        return render_template("test.html", data=results)
    
    elif request.method == "POST":
        input=request.get_json() 

        if input:
            dataAsDict={
                "Key": input["Key"], 
                "Value": input["Value"]
            }

            return jsonify(dataAsDict)

        else:
            return render_template("test.html", data=results, msg="Button pressed!")
# end of def

if __name__=='__main__':
    app.run(debug=True)