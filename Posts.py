from datetime import datetime

class Posts:
    def viewPost(self, id):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("""SELECT Title, Username, Timestamp, Profession, ProfessionCategory, Tags, Body FROM
            Question_Post WHERE QuestionPostID=""" + id)

        result1=cursor.fetchall()
        cursor.execute("SELECT Username, Timestamp, Body FROM Answer_Post WHERE QID=" + id)
        result2=cursor.fetchall()
        cursor.close()

        return result1, result2      # Return list of result from MySQL queries
    # end of def

    def postQuestion(self, username, title, body, profType, tags):
        from App import request
        from Database import mysql

        timestamp=datetime.now().replace(microsecond=0)

        cursor=mysql.connection.cursor()
        cursor.execute("""INSERT INTO Question_Post (Username, Title, Body, Timestamp, Profession, ProfessionCategory, Tags)
             VALUES (%s, %s, %s, %s, %s, %s, %s)""", (username, title, body, timestamp, "Engineer", profType, tags))

        mysql.connection.commit()
        cursor.execute("SELECT MAX(QuestionPostID) FROM Question_Post WHERE Username=%s", (username,))
        results=cursor.fetchone()
        cursor.close()

        return str(results[0])      # Return ID of most recent question posted by user
    # end of def

    def mostRecentQuestion(self):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT MAX(Timestamp) FROM Question_Post")
        time=cursor.fetchall()
        cursor.execute("SELECT * FROM Question_Post WHERE Timestamp=%s", (time,))
        result=cursor.fetchall()

        return result
    # end of def

    def mostRecentQuestionByUser(self, username):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT MAX(Timestamp) FROM Question_Post WHERE Username=%s", (username,))
        time=cursor.fetchall()
        cursor.execute("SELECT * FROM Question_Post WHERE Timestamp=%s", (time,))
        result=cursor.fetchall()

        return result
    # end of def

    def mostRecentAnswerByUser(self, username):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT MAX(Timestamp) FROM Answer_Post WHERE Username=%s", (username,))
        time=cursor.fetchall()
        cursor.execute("SELECT * FROM Answer_Post WHERE Timestamp=%s", (time,))
        result=cursor.fetchall()

        return result
    # end of def

    def postAnswer(self, username, qid, answer):
        from App import request
        from Database import mysql

        timestamp=datetime.now().replace(microsecond=0)
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT Profession FROM Profiles WHERE Username=%s", (username,))
        profession=cursor.fetchall()

        cursor.execute("""INSERT INTO Answer_Post (QID, Username, Body, Timestamp, Profession)
            VALUES (""" + qid + """, %s, %s, %s, %s)""", (username, answer, timestamp, profession))

        mysql.connection.commit()
    # end of def
    
    def getAnswer(self, aid):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Answer_Post WHERE AID=" + aid)
        result=cursor.fetchall()

        return result
    # end of def

# end of class
