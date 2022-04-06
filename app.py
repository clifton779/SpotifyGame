# pylint: disable=too-few-public-methods
# pylint: disable=too-many-locals
# pylint: disable=no-member
import os
from dotenv import find_dotenv, load_dotenv
import flask
import api
import requests
from flask_login import LoginManager, UserMixin
from flask_login import login_user, login_required, logout_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv(find_dotenv())

app = flask.Flask(__name__)

bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

app.config["SECRET_KEY"] = "I have a secret key, wizard!"
# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = "app.login"
login_manager.init_app(app)

rock = []
pop = []
country = []
hiphop = []
alternative = []

@login_manager.user_loader
def load_user(user_id):
    """This function is used to load user"""
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """This class is used to create User database"""

    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name
    
db.create_all()


@app.route("/")
def start():
    """This function is called on landing page to sign up"""
    value = 0
    page = 0
    if "page" in flask.session:
        page = flask.session["page"]
    if "user_exists" in flask.session:
        if flask.session["user_exists"]:
            value = 1
    return flask.render_template("signup.html", value=value, page=page)


@app.route("/signUpPage", methods=["GET", "POST"])
def sign():
    """This function is called on signUpPage to store the form data"""
    # code to validate and add user to database goes here
    
    username = flask.request.form.get("username")
    password_hash = flask.request.form.get("password_hash")
    # if this returns a user, then the username already exists in database
    user = User.query.filter_by(username=username).first()

    if user:
        print("im here")
        # if a user is found, we want to redirect back to signup page so user can try again
        flask.session["user_exists"] = True
        flask.session["page"] = 1
        return flask.redirect(flask.url_for("start"))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    print("im nre user here")
    new_user = User(username=username, password_hash=generate_password_hash(password_hash))
    print(password_hash)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return flask.render_template("login.html")

@app.route("/loginPage", methods=["GET", "POST"])
def login():
    """This function is used to login the user"""
    return flask.render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    """This function is used to logout the user"""
    logout_user()
    return flask.redirect(flask.url_for("login"))


@bp.route("/getsongs", methods=["POST", "GET"])
def get_songs(genre):
    arr = []
    urls = []
    names = []
    if genre == "rock":
        arr = rock
    elif genre == "pop":
        arr = pop
    elif genre == "hiphop":
        arr = hiphop
    elif genre == "country":
        arr = country
    elif genre == "alternative":
        arr = alternative
    urls = api.get_song_urls(arr)
    names = api.get_song_titles(arr)
    jsondata = []
    for url, name in zip(urls, names):
        jsondata.append({"url": url, "name": name})
    return flask.jsonify({"songs": jsondata})


app.register_blueprint(bp)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', '8080')),
    debug=True
)