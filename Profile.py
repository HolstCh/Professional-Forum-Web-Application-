from flask import Flask, render_template, request, redirect
from App import app
from Database import mysql

# Getting profile data from HTML and creating a new MySQL table in database to store data
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
        cursor.execute("""INSERT INTO Profiles (username, firstName, middleNames, lastName, email, currentCompany,
            profession, skills, description, projects) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (username,
            fName, mNames, lName, email, curComp, prof, skills, desc, pastProj))

        mysql.connection.commit()
        cursor.close()

        return redirect("login.html")
    # end of if
#end of def

# Display profile in HTML
def display(username):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM " + username + "_profile")
        result=cursor.fetchall()
        cursor.close()
        
        return render_template("showData.html", data=result)
# end of def

# Get data from MySQL table and allow user to edit it, where any edits will be sent to MySQL
def editProfile(username):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM " + username + "_profile")
        result=cursor.fetchall()
        cursor.close()

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
        cursor.execute("""UPDATE Profiles SET firstName=%s, middleNames=%s, lastName=%s, email=%s, 
            currentCompany=%s, profession=%s, skills=%s, description=%s, projects=%s""", (fName, mNames, lName, email, 
            curComp, prof, skills, desc, pastProj))

        return redirect("../view/" + username)      # Redirects to "localhost:5000/profile/view/<username>"
        # end of if
# end of def
    
