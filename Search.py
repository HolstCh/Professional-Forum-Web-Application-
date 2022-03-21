from Database import mysql
from App import app

def search():
    if request.method == "POST":
        query=request.form.get("basicSearch")

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Question_Post WHERE Body LIKE '%" + query + "%'")
        results=cursor.fetchall()

        return redirect("./query=" + query)

def searchResults(query, username):
    if request.method == "GET":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Question_Post WHERE Body LIKE '%" + query + "%' OR Title LIKE '%" + query + "%'")
        results=cursor.fetchall()

        if results:
            return render_template("searchResults.html", data=results, username=username)

        else:
            return render_template("searchResults.html", msg="No results...")

    elif request.method == "POST":
        query=request.form.get("basicSearch")

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Question_Post WHERE Body LIKE '%" + query + "%'")
        results=cursor.fetchall()

        return redirect("../query=" + query)
