import flask
import api


rock = []
pop = []
country = []
hiphop = []
alternative = []

app = flask.Flask(__name__)

# set up a separate route to serve the index.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page
@bp.route("/")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


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

app.run()
