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
        cursor.execute("""INSERT INTO Profiles (Username, FirstName, MiddleNames, LastName, Email, CurrentCompany,
            Profession, Skills, Description, Projects) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (username,
            fName, mNames, lName, email, curComp, prof, skills, desc, pastProj))

        mysql.connection.commit()
        cursor.close()
    #end of def

    # Display profile in HTML
    def getProfile(self, username):
        from Database import mysql
        
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Profiles WHERE Username=%s", (username,))
        result=cursor.fetchall()
        cursor.close()

        return result
    # end of def
    
    def pushEdits(self, username):
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
        cursor.execute("""UPDATE Profiles SET FirstName=%s, MiddleNames=%s, LastName=%s, Email=%s, CurrentCompany=%s,
            Profession=%s, Skills=%s, Description=%s, Projects=%s WHERE Username=%s""", (fName, mNames, lName, email, 
            curComp, prof, skills, desc, pastProj, username))
        
        mysql.connection.commit()

        cursor.close()
    # end of def

    def addCompany(self, username):
        from Database import mysql
        from App import request

        name = request.form.get("company", None)
        position = request.form.get("position", None)
        start = request.form.get("start", None)
        end = request.form.get("end", None)

        cursor = mysql.connection.cursor()
        cursor.execute("""INSERT INTO past_companies (Username, CompanyName, Start, End, Position) VALUES (%s, %s, %s, %s, %s)""",
            (username, name, start, end, position))
        #cursor.execute(userQuery)
        cursor.close()

    def getPastCompanies(self, username):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Past_Companies WHERE Username=%s", (username,))
        result=cursor.fetchall()
        cursor.close()

        return result
