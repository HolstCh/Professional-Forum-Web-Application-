from flask import Flask, redirect, url_for, render_template, request, jsonify, flash

import Search
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

HOST = "http://127.0.0.1:5000/"


@app.route('/')
def home():  # put application's code here
    return redirect(url_for('unregisteredMain'))


@app.route('/unregisteredMain', methods=["POST", "GET"])
def unregisteredMain():
    if request.method == "POST":
        search = Search()
        searchValue = search.getQuery()
        listOfTuples = search.searchResults(searchValue)
        print(listOfTuples)
        if searchValue:
            print(searchValue)
            filter = Filter()
            profession = request.form["inputProfession"]
            updatedListOfTuples = filter.professionType(listOfTuples, profession)
            print(updatedListOfTuples)
            return render_template("mainPage.html")
        else:
            return render_template("mainPage.html")
    else:
        return render_template("mainPage.html")


@app.route('/registeredMain', methods=["POST", "GET"])
def registeredMain():
    if request.method == "POST":
        search = Search()
        searchValue = search.getQuery()
        listOfTuples = search.searchResults(searchValue)
        print(listOfTuples)
        if searchValue:
            print(searchValue)
            filter = Filter()
            profession = request.form["inputProfession"]
            updatedListOfTuples = filter.professionType(listOfTuples, profession)
            print(updatedListOfTuples)
            return render_template("mainPage.html")
        else:
            return render_template("userHome.html")
    else:
        return render_template("userHome.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        myLogin = Login(username, password)
        userExists = myLogin.authenticate()
        if userExists:
            return redirect(url_for("registeredMain"))
        else:
            return render_template('loginPage.html')
    else:
        return render_template('loginPage.html')


@app.route('/signUp', methods=["POST", "GET"])
def signUp():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        myLogin = Login(username, password)
        userExists = myLogin.authenticate()
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
        myProfile = Profile()
        myProfile.createProfile(username)
        return redirect(url_for('registeredMain'))
    else:
        return render_template('createProfile.html')


if __name__ == '__main__':
    app.run(debug=True)
