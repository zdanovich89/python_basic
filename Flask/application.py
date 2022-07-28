from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World from Flask Main Page"


@application.route("/help")
def help_page():
    return "<b><font color=blue>This is Help Page V2!!!</b> "


@application.route("/user")
def usermain_page():
    return "User's main Page!!"


@application.route("/user/<username>")
def show_user_page(username):
    return "Hello " + username.upper()


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "Subpath is: " + subpath


@application.route("/square/<int:x>")
def calc_square(x):
    return "Square from: " + str(x) + " = " + str(x*x)


@application.route("/htmlpage")
def show_htmlpage():
    myfile = open("mypage.html", "r")
    page = myfile.read()
    myfile.close()
    return page


# ----------------Main-----------------
if __name__ == "__main__":
    application.run()