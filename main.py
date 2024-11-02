from flask import Flask, request, render_template
from flask_cors import CORS
from scrappers.freefy import freefy

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/discover")
def discover():
    return freefy().discover()

@app.route("/search")
def search():
    query = request.args.get("q")
    return freefy().search(query)

@app.route("/search/tracks")
def search_tracks():
    query = request.args.get("q")
    page = request.args.get("page")
    return freefy().searchTracks(query, page)



if __name__ == "__main__":
    app.run(debug=True)