from Database import mysql
from App import app

def questionHistory(username):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Question_Post WHERE Username=%s", (username,))
        results=cursor.fetchall()

        if results:
            return render_template("questionHistory.html", username=username, data=results)
        
        else:
            return render_template("questionHistory.html", username=username, msg="No question history...")

def answerHistory(username):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Answer_Post WHERE Username=%s", (username,))
        results1=cursor.fetchall()

        if results1:
            cursor.execute("""SELECT Question_Post.Title FROM Question_Post JOIN Answer_Post ON Question_Post.QuestionPostID
                =Answer_Post.QID WHERE Answer_Post.Username=%s""", (username,))
            
            results2=cursor.fetchall()

            data=zip(results1, results2)

            return render_template("answerHistory.html", username=username, data=data)

        else:
            return render_template("answerHistory.html", username=username, msg="No answer history...")