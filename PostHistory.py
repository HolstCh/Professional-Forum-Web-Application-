from Database import mysql
from App import app

class PostHistory:
    def questionHistory(username):
            cursor=mysql.connection.cursor()
            cursor.execute("SELECT * FROM Question_Post WHERE Username=%s", (username,))
            
            return cursor.fetchall()
    # end of def

    def answerHistory(username):
            cursor=mysql.connection.cursor()
            cursor.execute("SELECT * FROM Answer_Post WHERE Username=%s", (username,))
            results1=cursor.fetchall()

            if results1:
                cursor.execute("""SELECT Question_Post.Title FROM Question_Post JOIN Answer_Post ON Question_Post.QuestionPostID
                    =Answer_Post.QID WHERE Answer_Post.Username=%s""", (username,))

                results2=cursor.fetchall()
                data=zip(results1, results2)

                return data

            else:
                return None
    # end of def
