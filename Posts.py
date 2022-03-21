from Database import mysql
from App import app
from datetime import datetime

def viewPost(id):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("""SELECT Title, Username, Timestamp, Profession, ProfessionCategory, Body FROM 
            Question_Post WHERE QuestionPostID=""" + id)
        result1=cursor.fetchall()
        cursor.execute("SELECT Username, Timestamp, Body FROM Answer_Post WHERE QID=" + id)
        result2=cursor.fetchall()

        return render_template("viewPost.html", question=result1, answers=result2, qid=id)
    # end of if
# end of def

def postQuestion(username):
    if request.method == "GET":
        return render_template("test.html")
    # end of if

    elif request.method == "POST":
        title=request.form.get("title", None)
        body=request.form.get("ques", None)
        profession=request.form.get("prof", None)
        global select
        timestamp=datetime.now().replace(microsecond=0)

        if profession == "Civil":
            select=request.form.getlist("civilCB", None)
        
        elif profession == "Chemical":
            select=request.form.getlist("chemCB", None)

        elif profession == "Electrical":
            select=request.form.getlist("elecCB", None)
        
        elif profession == "Geomatics":
            select=request.form.getlist("geoCB", None)

        elif profession == "Mechanical":
            select=request.form.getlist("mechCB", None)

        elif profession == "Software":
            select=request.form.getlist("softCB", None)

        cursor=mysql.connection.cursor()
        cursor.execute("""INSERT INTO Question_Post (Username, Title, Body, Timestamp, Profession, ProfessionCategory)
             VALUES (%s, %s, %s, %s, %s, %s)""", (username, title, body, timestamp, profession, select))

        mysql.connection.commit()
        cursor.execute("SELECT MAX(QuestionPostID) FROM Question_Post")
        results=cursor.fetchone()

        #print(results[0], file=sys.stdout)

        return redirect("./view/" + str(results[0]))
    # end of if
# end of def
