# To run server:
#   1. cd "C:\Users\coolp\Documents\Dylan\School\Y3 - 2022 WINTER\SENG 401 - Software Architecture\Project\test"
#   2. python -m venv test
#   3. scripts\activate
#   4. python -m flask run

# Installation commands:
#   > python -m pip install flask
#   > python -m pip install flask_mysqldb

from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'draGGun.!382'
app.config['MYSQL_DB'] = 'seng401'

mysql=MySQL(app)

@app.route("/", methods=["GET", "POST"])
def signUp():
    if request.method == "GET":
        return render_template("testSignUp.html")

    if request.method == "POST":
        global username
        username=request.form.get("username", None)
        password=request.form.get("password", None)

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username=%s", (username,))
        result=cursor.fetchall()

        if result:
            #return "<h1 style='color:red'> Record already exists! </h1>"
            return render_template("testSignUp.html", data=username)
        else:
            cursor.execute("INSERT INTO Users (username, password) VALUES(%s, %s)", (username, password))
            mysql.connection.commit()
            return redirect("./edit/profile")
        #end of if
# end of def

@app.route("/edit/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        return render_template("testProfile.html")

    if request.method == "POST":
        fName=request.form.get("fName", None)
        mNames=request.form.get("mNames", None)
        lName=request.form.get("lName", None)
        email=request.form.get("email", None)
        curComp=request.form.get("curComp", None)
        prof=request.form.get("prof", None)
        skills=request.form.get("skills", None)
        desc=request.form.get("desc", None)
        pastProj=request.form.get("proj", None)

        cursor=mysql.connection.cursor()
        cursor.execute("""CREATE TABLE """ + username + """_profile (
           firstName text not null, 
           middleNames text, 
           lastName text not null, 
           email text not null, 
           currentCompany text, 
           profession text not null,
           skills text, 
           description text, 
           projects text
        )""")

        mysql.connection.commit()

        cursor.execute("""INSERT INTO """ + username + """_profile (firstName, middleNames, lastName, email, currentCompany,
            profession, skills, description, projects) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (fName, mNames, lName,
            email, curComp, prof, skills, desc, pastProj))

        mysql.connection.commit()
        cursor.close()

        return "<h1 style='color:green'> Record added successfully! </h1>"

if __name__=='__main__':
    app.run(debug=True)