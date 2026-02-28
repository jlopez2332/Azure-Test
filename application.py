from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Mig's Cafe!</h1></body></html>\n"
