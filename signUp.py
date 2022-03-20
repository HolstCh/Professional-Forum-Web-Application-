from Database import mysql
from App import app

def signUp():
    if request.method == "GET":
        return render_template("signUp.html")

    if request.method == "POST":
        username=request.form.get("username", None)
        password=request.form.get("password", None)

        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO Users (Username, Password, Type) VALUES (%s, %s, %s)", (username, password, "Registered User"))
        mysql.connection.commit()

        return redirect("/profile/create" + username)