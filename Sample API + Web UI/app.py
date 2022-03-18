from flask import Flask, render_template, request, redirect, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mysql=MySQL(app)

@app.route("/", methods=["GET", "POST"])
def display():
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users")
    results=cursor.fetchall()

    if request.method == "GET":
        return render_template("test.html", data=results)
    
    # Check if API sent any data
    elif request.method == "POST":
        input=request.get_json() 

        # If post method was from API...
        if input:
            dataAsDict={
                "Key": input["Key"], 
                "Value": input["Value"]
            }

            return jsonify(dataAsDict)

        # If post method was from HTML element...
        else:
            return render_template("test.html", data=results, msg="Button pressed!")
# end of def

if __name__=='__main__':
    app.run(debug=True)
