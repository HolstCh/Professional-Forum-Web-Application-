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

HOST = "http://127.0.0.1:5000/"
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
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)

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
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)

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
        query=request.form.get("basicSearch")
        results = MyFilter.professionType(query, professionFilter)
        if results:
            return render_template("searchResults.html", data=results, username=username)

        else:
            return render_template("searchResults.html", username=username, msg="No results...")

    elif request.method == "POST":
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)



@app.route("/addCompany/<username>", methods=["GET", "POST"])
def addCompany(username):
    if request.method == "POST" and request.form.get("basicSearch") == None:
        name = request.form.get("company", None)
        position = request.form.get("position", None)
        start = request.form.get("start", None)
        end = request.form.get("end", None)
        profile = Profile()
        profile.addCompany(username, name, position, start, end)
        flash("Company added successfully")

        return render_template("addCompany.html", username = username)

    elif request.method == "GET":
        return render_template("addCompany.html", username = username)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        query = request.form.get("basicSearch")

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
        fName=request.form.get("fName", None)
        mNames=request.form.get("mNames", None)
        lName=request.form.get("lName", None)
        email=request.form.get("email", None)
        curComp=request.form.get("curComp", None)
        prof=request.form.get("prof", None)
        skills=request.form.get("skills", None)
        desc=request.form.get("desc", None)
        pastProjs=request.form.get("proj", None)
        myProfile = Profile()
        myProfile.createProfile(username, fName, mNames, lName, email, curComp, prof, skills, desc, pastProjs)

        return redirect(url_for('registeredMain'))

    else:
        return render_template('createProfile.html')


@app.route("/profile/view/<username>", methods=["GET", "POST"])
def viewProfile(username):
    if request.method == "GET":
        myProfile=Profile()
        profile=myProfile.getData(username)
        companies=myProfile.getPastCompanies(username)

        return render_template("viewProfile.html", profile=profile, companies=companies, username=username)
    
    elif request.method == "POST" and request.form.get("basicSearch") != None:
        query = request.form.get("basicSearch")

        return redirect("../../../query=" + query)

    elif request.method == "POST" and request.form.get("basicSearch") == None:
        return redirect("../../../addCompany/" + username)


@app.route("/profile/edit/<username>", methods=["GET", "POST"])
def editProfile(username):
    if request.method == "GET":
        myProfile = Profile()
        data = myProfile.getData(username)

        return render_template("editProfile.html", data=data, username=username)

    elif request.method == "POST" and request.form.get("basicSearch") == None:
        fName=request.form.get("fName", None)
        mNames=request.form.get("mNames", None)
        lName=request.form.get("lName", None)
        email=request.form.get("email", None)
        curComp=request.form.get("curComp", None)
        prof=request.form.get("prof", None)
        skills=request.form.get("skills", None)
        desc=request.form.get("desc", None)
        pastProjs=request.form.get("proj", None)
        myProfile = Profile()
        myProfile.pushEdits(username, fName, mNames, lName, email, curComp, prof, skills, desc, pastProjs)

        return redirect("/view/" + username)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)


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
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)


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
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)


@app.route("/post/question", methods=["GET", "POST"])
def newQuestion():
    if request.method == "GET":
        return render_template("questionPost.html", username=username)

    elif request.method == "POST" and request.form.get("basicSearch") == None:
        title=request.form.get("title", None)
        body=request.form.get("ques", None)
        profType=request.form.get("prof", None)
        global select   # Make variable accessible to if/else/elif blocks

        # Check which dropdown menu option was selected and get all checkboxes under that category
        if profType == "Civil":
            select=request.form.getlist("civilCB", None)

        elif profType == "Chemical":
            select=request.form.getlist("chemCB", None)

        elif profType == "Electrical":
            select=request.form.getlist("elecCB", None)

        elif profType == "Geomatics":
            select=request.form.getlist("geoCB", None)

        elif profType == "Mechanical":
            select=request.form.getlist("mechCB", None)

        elif profType == "Software":
            select=request.form.getlist("softCB", None)
            
        myPost = Posts()
        qid = myPost.postQuestion(username, title, body, profType, str(tags))

        return redirect("./view/" + qid)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)


@app.route("/post/view/<qid>", methods=["GET", "POST"])
def viewPost(qid):
    if request.method == "GET":
        myPost = Posts()
        question = myPost.viewPost(qid)[0]
        answers = myPost.viewPost(qid)[1]

        return render_template("viewPost.html", question=question, answers=answers, username=username)

    elif request.method == "POST" and request.form.get("basicSearch") == None:
        answer=request.form.get("ans")
        myPost = Posts()
        myPost.postAnswer(username, qid, answer)
        question = myPost.viewPost(qid)[0]
        answers = myPost.viewPost(qid)[1]

        return render_template("viewPost.html", question=question, answers=answers, username=username)

    elif request.method == "POST" and request.form.get("basicSearch") != None:
        query = request.form.get("basicSearch")

        return redirect("http://127.0.0.1:5000/query=" + query)


# --------------------------------------------------------------------------------------------------------------------- #

@app.route("/api/user", methods=["GET", "POST"])
def apiUsers():
    from Login import Login

    if request.method == "GET" and request.get_json() != None:
        data=request.get_json()
        username=data["username"]
        password=data["password"]

        myLogin=Login(username, password)
        user=myLogin.validate()

        return jsonify(user)

    elif request.method == "POST" and request.get_json() != None:
        data=request.get_json()
        username=data["username"]
        password=data["password"]
        myLogin=Login(username, password)
        myLogin.add_login()

        return "Login created successfully!"

@app.route("/api/profile", methods=["GET", "POST"])
def apiProfile():
    from Profile import Profile
    
    if request.method == "GET" and request.get_json() != None:
        username=request.get_json()["username"]
        myProfile=Profile()
        profile=myProfile.getProfile(username)

        return jsonify(profile)

    elif request.method == "POST" and request.get_json() != None:
        data=request.get_json()
        username=data["username"]
        firstName=data["first name"]
        middleNames=data["middle names"]
        lastName=data["last name"]
        email=data["email"]
        currentCompany=data["current company"]
        profession=data["profession"]
        skills=data["skills"]
        description=data["description"]
        projects=data["projects"]

        myProfile=Profile()
        myProfile.createProfile(username, firstName, middleNames, lastName, email, currentCompany, profession, skills,
            description, projects)

        return "Profile created successfully!"

@app.route("/api/question", methods=["GET", "POST"])
def apiQuestion():
    from Posts import Posts

    if request.method == "GET" and request.get_json() != None:
        qid=request.get_json()["id"]
        myPost=Posts()
        question=myPost.viewPost(qid)[0]

        return jsonify(question)

    elif request.method == "POST" and request.get_json() != None:
        data=request.get_json()
        username=data["username"]
        title=data["title"]
        body=data["body"]
        professionCategory=data["profession category"]
        tags=data["tags"]

        myPost=Posts()
        myPost.postQuestion(username, title, body, professionCategory, tags)

        return "Question successfully added!"

@app.route("/api/answer", methods=["GET", "POST"])
def apiAnswer():
    from Posts import Posts

    if request.method == "GET" and request.get_json() != None:
        aid=request.get_json()["id"]
        myPost=Posts()
        answer=myPost.getAnswer(aid)

        return jsonify(answer)

    elif request.method == "POST" and request.get_json() != None:
        data=request.get_json()
        username=data["username"]
        qid=data["qid"]
        body=data["body"]

        myPost=Posts()
        myPost.postAnswer(username, qid, body)

        return "Answer successfully added!"

@app.route("/api/pastCompany", methods=["GET", "POST"])
def apiPastCompanies():
    from Profile import Profile

    if request.method == "GET" and request.get_json() != None:
        username=str(request.get_json()["username"])
        myProfile=Profile()
        pastCompanies=myProfile.getPastCompanies(username)

        return jsonify(pastCompanies)

    elif request.method == "POST" and request.get_json() != None:
        data=request.get_json()
        username=data["username"]
        company=data["company"]
        position=data["position"]
        start=data["start"]
        end=data["end"]

        myProfile=Profile()
        myProfile.addCompany(username, company, position, start, end)

        return "Past Company successfully added!"

# --------------------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)
