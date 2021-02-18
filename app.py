from flask import Flask
app = Flask(stats418hello105645306world)

@app.route("/")
def hello():
    return "Hello, World!"
