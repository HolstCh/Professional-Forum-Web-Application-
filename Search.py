class Search:
    # Note: default constructor is used

    def getQuery(self):
        from app import request
        
        return request.form.get("basicSearch")
    # end of def

    def searchResults(self, query):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Question_Post WHERE Body LIKE '%" + query + "%' OR Title LIKE '%" + query + "%'")

        return cursor.fetchall()
    # end of def
