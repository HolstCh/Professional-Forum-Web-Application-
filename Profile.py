class Profile:
    # Getting profile data from HTML and creating a new MySQL table in database to store data
    def createProfile(self, username):
        from App import request
        from Database import mysql
        
        fName=request.form.get("fName", None)
        mNames=request.form.get("mNames", None)
        lName=request.form.get("lName", None)
        email=request.form.get("email", None)
        curComp=request.form.get("curComp", None)
        prof=request.form.get("prof", None)
        skills=request.form.get("skills", None)
        desc=request.form.get("desc", None)
        pastProj=request.form.get("proj", None)
        
        cursor=mysql.connection.cursor()
        cursor.execute("""INSERT INTO Profiles (username, firstName, middleNames, lastName, email, currentCompany,
            profession, skills, description, projects) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (username,
            fName, mNames, lName, email, curComp, prof, skills, desc, pastProj))

        mysql.connection.commit()
        cursor.close()
    #end of def

    # Display profile in HTML
    def display(self, username):
        from Database import mysql
        
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Profiles")
        result=cursor.fetchall()
        cursor.close()

        return result
    # end of def

    # Get data from MySQL table and allow user to edit it, where any edits will be sent to MySQL
    def displayEditableProfile(self, username):
        from App import request
        from Database import mysql
        
            cursor=mysql.connection.cursor()
            cursor.execute("SELECT * FROM Profiles")
            result=cursor.fetchall()
            cursor.close()

            return result
    # end of def
    
    def pushEdits(self, username):
        from App import app, request
        from Database import mysql
        
        fName=request.form.get("fName", None)
        mNames=request.form.get("mNames", None)
        lName=request.form.get("lName", None)
        email=request.form.get("email", None)
        curComp=request.form.get("curComp", None)
        prof=request.form.get("prof", None)
        skills=request.form.get("skills", None)
        desc=request.form.get("desc", None)
        pastProj=request.form.get("proj", None)

        cursor.mysql.connection.cursor()
        cursor.execute("""UPDATE Profiles SET firstName=%s, middleNames=%s, lastName=%s, email=%s, 
            currentCompany=%s, profession=%s, skills=%s, description=%s, projects=%s""", (fName, mNames, lName, email, 
            curComp, prof, skills, desc, pastProj))

        cursor.close()
    # end of def
