from Database import mysql
from App import app
from datetime import datetime

class Posts:
    def viewPost(self, id):
        cursor=mysql.connection.cursor()
        cursor.execute("""SELECT Title, Username, Timestamp, Profession, ProfessionCategory, Body FROM 
            Question_Post WHERE QuestionPostID=""" + id)

        result1=cursor.fetchall()
        cursor.execute("SELECT Username, Timestamp, Body FROM Answer_Post WHERE QID=" + id)
        result2=cursor.fetchall()
        
        return zip(result1, result2)      # Return list of result from MySQL queries
        # end of if
    # end of def

    def postQuestion(self, username):
        title=request.form.get("title", None)
        body=request.form.get("ques", None)
        profession=request.form.get("prof", None)
        timestamp=datetime.now().replace(microsecond=0)

        global select   # Make variable accessible to if/else/elif blocks

        # Check which dropdown menu option was selected and get all checkboxes under that category
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
        cursor.execute("SELECT MAX(QuestionPostID) FROM Question_Post WHERE Username=%s", (username,))
        results=cursor.fetchone()
        
        return str(results[0])      # Return ID of most recent question posted by user
    # end of def
