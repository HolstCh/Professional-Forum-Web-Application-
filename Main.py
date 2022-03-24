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
from Posts import *
from PostHistory import *

HOST = "http://knowpros.pythonanywhere.com"
username = None
professionFilter = None


@app.route('/')
def home():
    return redirect(url_for('unregisteredMain'))


@app.route('/unregisteredMain', methods=["POST", "GET"])
def unregisteredMain():
    username = None
    global professionFilter
    if request.method == "POST":
        profFilter = request.form["inputProfession"]
        professionFilter = profFilter
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)

    else:
        myPost = Posts()
        data = myPost.mostRecentQuestion()

        return render_template("mainPage.html", data=data)


@app.route('/registeredMain/<username>', methods=["POST", "GET"])
def registeredMain(username):
    global professionFilter
    if request.method == "POST":
        profFilter = request.form["inputProfession"]
        professionFilter = profFilter
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)

    else:
        myPost = Posts()
        question = myPost.mostRecentQuestionByUser(username)
        answer = myPost.mostRecentAnswerByUser(username)

        return render_template("userHome.html", username=username, question=question, answer=answer)


@app.route("/query=<query>", methods=["GET", "POST"])
def search(query):
    global professionFilter
    if request.method == "GET":
        MySearch = Search()
        MyFilter = Filter()
        results = MySearch.searchResults(query)
        results = MyFilter.professionType(results, professionFilter)
        if results:
            return render_template("searchResults.html", data=results, username=username)

        else:
            return render_template("searchResults.html", username=username, msg="No results...")

    elif request.method == "POST":
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)



@app.route("/addCompany/<username>", methods=["GET", "POST"])
def addCompany(username):
    if request.method == "POST" and request.form.get("basicSearch") == None:
        profile = Profile()
        profile.addCompany(username)
        flash("Company added successfully")

        return render_template("addCompany.html", username = username)


#         return render_template("addCompany.html", username=username)

    elif request.method == "GET":
        return render_template("addCompany.html", username = username)

#         return render_template("addCompany.html", username=username)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("../../query=" + query)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        global username
        username = request.form["username"]
        password = request.form["password"]
        myLogin = Login(username, password)
        # userExists = myLogin.authenticate()
        userExists = myLogin.validate()

        if userExists:
            return redirect("./registeredMain/" + username)
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
   # global data

    if request.method == "POST":
        myProfile = Profile()
        myProfile.createProfile(username)

        return redirect(url_for('registeredMain'))

    else:
        return render_template('createProfile.html')


@app.route("/profile/view/<username>", methods=["GET", "POST"])
def viewProfile(username):
    if request.method == "GET":
        myProfile = Profile()
        data = myProfile.getData(username)

        return render_template("viewProfile.html", data=data, username=username)

    elif request.method == "POST":
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)

    # Add post later (will be for "add past company")


@app.route("/profile/edit/<username>", methods=["GET", "POST"])
def editProfile(username):
    if request.method == "GET":
        myProfile = Profile()
        data = myProfile.getData(username)

        return render_template("editProfile.html", data=data, username=username)

    elif request.method == "POST" and request.form.get("basicSearch") == None:
        myProfile = Profile()
        myProfile.pushEdits(username)

        return redirect("/view/" + username)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)


@app.route("/questions/<username>", methods=["GET", "POST"])
def questionHistory(username):
    if request.method == "GET":
        myPostHistory = PostHistory()
        data = myPostHistory.questionHistory(username)

        if data:
            return render_template("questionHistory.html", data=data, username=username)
        else:
            return render_template("questionHistory.html", username=username, msg="No question history...")

    elif request.method == "POST":
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)


@app.route("/answers/<username>", methods=["GET", "POST"])
def answerHistory(username):
    if request.method == "GET":
        myPostHistory = PostHistory()
        data = myPostHistory.answerHistory(username)

        if data:
            return render_template("answerHistory.html", data=data, username=username)
        else:
            return render_template("answerHistory.html", username=username, msg="No answer history...")

    elif request.method == "POST":
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)


@app.route("/post/question", methods=["GET", "POST"])
def newQuestion():
    if request.method == "GET":
        return render_template("questionPost.html", username=username)

    elif request.method == "POST" and request.form.get("basicSearch") == None:
        myPost = Posts()
        qid = myPost.postQuestion(username)

        return redirect("./view/" + qid)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)


@app.route("/post/view/<qid>", methods=["GET", "POST"])
def viewPost(qid):
    if request.method == "GET":
        myPost = Posts()
        question = myPost.viewPost(qid)[0]
        answers = myPost.viewPost(qid)[1]

        return render_template("viewPost.html", question=question, answers=answers, username=username)

    elif request.method == "POST" and request.form.get("basicSearch") == None:
        myPost = Posts()
        myPost.postAnswer(username, qid)
        question = myPost.viewPost(qid)[0]
        answers = myPost.viewPost(qid)[1]

        return render_template("viewPost.html", question=question, answers=answers, username=username)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        MySearch = Search()
        query = MySearch.getQuery()

        return redirect("http://knowpros.pythonanywhere.com/query=" + query)


# --------------------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)

