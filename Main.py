from flask import Flask, redirect, url_for, render_template, request, jsonify, flash

from App import app
from Database import mysql
from Filter import *
from Login import *
from Profile import *
from ProfessionCategory import *
from RegisteredCompany import *
from UnregisteredCompany import *
from Engineer import *
from Search import *

username=None
HOST = "http://127.0.0.1:5000/"


@app.route('/')
def home():  # put application's code here
    return redirect(url_for('unregisteredMain'))


@app.route('/unregisteredMain', methods=["POST", "GET"])
def unregisteredMain():
    if request.method == "POST":
        MySearch=Search()
        query=MySearch.getQuery()
        
        return redirect("./query=" + query)

    else:
        return render_template("mainPage.html")


@app.route('/registeredMain', methods=["POST", "GET"])
def registeredMain():
    if request.method == "POST":
        MySearch=Search()
        query=MySearch.getQuery()
        
        return redirect("./query=" + query)

    else:
        return render_template("userHome.html", username=username)
    
    
@app.route("/query=<query>", methods=["GET", "POST"])
def search(query):
    if request.method == "GET":
        MySearch=Search()
        results=MySearch.searchResults(query)

        if results:
            return render_template("searchResults.html", data=results, username=username)

        else:
            return render_template("searchResults.html", username=username, msg="No results...")
    
    elif request.method == "POST":
        MySearch=Search()
        query=MySearch.getQuery()

        return redirect("../query=" + query)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        global username
        username = request.form["username"]
        password = request.form["password"]
        myLogin = Login(username, password)
        #userExists = myLogin.authenticate()
        userExists = myLogin.validate()

        if userExists:
            return redirect(url_for("registeredMain"))
        else:
            return render_template('loginPage.html', msg="INVALID LOGIN")

    else:
        return render_template('loginPage.html')


@app.route('/signUp', methods=["POST", "GET"])
def signUp():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        myLogin = Login(username, password)
        userExists = myLogin.user_exist()

        if userExists:
            return render_template('signUp.html', data=username)
        else:
            myLogin.add_login()
            return redirect(url_for("createProfile", username=username))

    else:
        return render_template('signUp.html')


@app.route('/createProfile/<username>', methods=["POST", "GET"])
def createProfile(username):
    global data
    
    if request.method == "POST":
        myProfile=Profile()
        myProfile.createProfile(username)
        
        return redirect(url_for('registeredMain'))

    else:
        return render_template('createProfile.html')


@app.route("/profile/view/<username>", methods=["GET", "POST"])
def viewProfile(username):
    from Profile import Profile

    if request.method == "GET":
        myProfile=Profile()
        data=myProfile.getData(username)

        return render_template("viewProfile.html", data=data, username=username)

    # Add post later (will be for "add past company")
    
    
@app.route("/profile/edit/<username>", methods=["GET", "POST"])
def editProfile(username):
    from Profile import Profile
    
    if request.method == "GET":
        myProfile=Profile()
        data=myProfile.getData(username)

        return render_template("editProfile.html", data=data, username=username)

    elif request.method == "POST":
        myProfile=Profile()
        myProfile.pushEdits(username)

        return redirect("../view/" + username)
    
@app.route("/questions/<username>", methods=["GET"])
def questionHistory(username):
    from PostHistory import PostHistory

    myPostHistory=PostHistory()
    data=myPostHistory.questionHistory()

    if data:
        return render_template("questionHistory.html", data=data, username=username)
    else:
        return render_template("questionHistory.html", username=username, msg="No question history...")    
    
    
@app.route("/answers/<username>", methods=["GET"])
def answerHistory(username):
    from PostHistory import PostHistory

    myPostHistory=PostHistory()
    data=myPostHistory.answerHistory()

    if data:
        return render_template("answerHistory.html", data=data, username=username)
    else:
        return render_template("answerHistory.html", username=username, msg="No answer history...")
    
# --------------------------------------------------------------------------------------------------------------- #    
    
if __name__ == '__main__':
    app.run(debug=True)
