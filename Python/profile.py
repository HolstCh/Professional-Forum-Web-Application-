from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'draGGun.!382'
app.config['MYSQL_DB'] = 'seng401'

mysql=MySQL(app)

@app.route("/profile/create/<username>", methods=["GET", "POST"])
def createProfile(username):
    if request.method == "GET":
        # Sending empty data ONCE to forms
        return render_template("editProfile.html", data=" ")
    # end of if

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
    # end of if
#end of def

@app.route("/profile/view/<username>", methods=["GET", "POST"])
def display(username):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM " + username + "_profile")
        result=cursor.fetchall()
        
        # Sending data from MySQL to fill HTML form
        return render_template("showData.html", data=result)
# end of def

@app.route("/profile/edit/<username>", methods=["GET", "POST"])
def editProfile(username):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM " + username + "_profile")
        result=cursor.fetchall()

        return render_template("editProfile.html", data=result)
    # end of if
    
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

        cursor.mysql.connection.cursor()
        cursor.execute("""UPDATE""" + username + """_profile SET firstName=%s, middleNames=%s, lastName=%s, email=%s, 
            currentCompany=%s, profession=%s, skills=%s, description=%s, projects=%s""", (fName, mNames, lName, email, 
            curComp, prof, skills, desc, pastProj))

        return render_template("<h1 style='color:green'> Profile updated successfully! </h1>")
        # end of if
# end of def

if __name__=='__main__':
    app.run(debug=True)
    
