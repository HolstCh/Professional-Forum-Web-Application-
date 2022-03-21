class PostHistory:
    def questionHistory(username):
        from Database import mysql
        
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Question_Post WHERE Username=%s", (username,))
        results=cursor.fetchall()
        cursor.close()

        return results
    # end of def

    def answerHistory(username):
        from Database import mysql
        
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM Answer_Post WHERE Username=%s", (username,))
        results1=cursor.fetchall()

        if results1:
            cursor.execute("""SELECT Question_Post.Title FROM Question_Post JOIN Answer_Post ON Question_Post.QuestionPostID
                =Answer_Post.QID WHERE Answer_Post.Username=%s""", (username,))

            results2=cursor.fetchall()
            cursor.close()

            return zip(results1, results2)      # Bundle results from MySQL query

        else:
            cursor.close()

            return None     # If first query was empty, return none
    # end of def
