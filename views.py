from flask import .....


views = Blueprint('views', __name__)

@view.route('/login')
def homepage():
    return render_template("main_page.html", user = current_user)
