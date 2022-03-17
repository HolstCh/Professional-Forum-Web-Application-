from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'draGGun.!382'
app.config['MYSQL_DB'] = 'seng401'

mysql=MySQL(app)

@app.route("/post/answer/<qid>", methods=["GET", "POST"])
def postAnswer(qid):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT Title, Username, Body FROM Question_Post WHERE QID=" + qid)
        result1=cursor.fetchall()

        return render_template("postAnswer.html", question=result1)
    # end of if

    if request.method == "POST":
        # get username
        timestamp=datetime.now().replace(microsecond=0)
        body=request.form.get("ans", None)

        cursor=mysql.connection.cursor()
        # insert into table

        return """<h1 style='color:green'> Answer added successfully! </h1>
                <p>""" + str(timestamp) + """</p>
                <p>""" + body + """</p>"""
            
    # end of if
# end of def

if __name__=='__main__':
    app.run(debug=True)
