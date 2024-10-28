#from werkzeug.urls import url_quote_plus
from urllib.parse import quote as url_quote
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
