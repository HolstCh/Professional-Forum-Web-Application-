from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'draGGun.!382'
app.config['MYSQL_DB'] = 'seng401'

mysql=MySQL(app)

@app.route("/post/view/<id>", methods=["GET"])
def viewPost(id):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT Title, Username, Body, QuestionDate FROM Question_Post WHERE QID=" + id)
        result1=cursor.fetchall()
        cursor.execute("SELECT Username, Body, AnswerDate FROM Answer_Post WHERE QID=" + id)
        result2=cursor.fetchall()

        return render_template("viewPost.html", question=result1, answers=result2, qid=id)
    # end of if
# end of def

if __name__=='__main__':
    app.run(debug=True)
