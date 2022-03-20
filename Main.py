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

HOST = "http://127.0.0.1:5000/"


@app.route('/')
def home():  # put application's code here
    return redirect(url_for('main'))


@app.route('/main', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        # "name" in HTML form not pulling data from search bar? testing with else branch for now
        searchBarInput = request.form["basicSearch"]
        myFilter = Filter(searchBarInput)
        match = myFilter.searchKeywords()
        print(match)
        if match:
            print("yay, match")
        else:
            return render_template("mainPage.html")
    else:
        searchBarInput = "test up to first 5 keywords here"
        myFilter = Filter(searchBarInput)
        match = myFilter.searchKeywords()
        print(match)
        if match:
            print("yay, match")
            return render_template("mainPage.html")
        else:
            return render_template("mainPage.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        myLogin = Login(username, password)
        userExists = myLogin.authenticate()
        if userExists:
            return redirect(url_for("main"))
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
            return redirect(url_for("main"))
    else:
        return render_template('signUp.html')


if __name__ == '__main__':
    app.run(debug=True)
