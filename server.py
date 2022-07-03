from flask import Flask, render_template, request
from servo import Servo

app = Flask(__name__)

s1 = Servo(12)
s2 = Servo(13)


@app.route("/")
def index():
    return render_template("controls.html")


@app.route("/keypress", methods=['GET'])
def keypress():
    key = request.args['key']

    if key == 'W':
        s1.up()
    elif key == 'S':
        s1.down()
    elif key == 'A':
        s2.up()
    elif key == 'D':
        s2.down()

    return key
