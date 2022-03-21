class Search:
    # Note: default constructor is used

    def getQuery(self):
        from app import request
        query=request.form.get("basicSearch")
        
        return query
    # end of def

    def searchResults(self, query):
        from Database import mysql

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Question_Post WHERE Body LIKE '%" + query + "%' OR Title LIKE '%" + query + "%'")
        results=cursor.fetchall()
        cursor.close()

        return results
    # end of def
