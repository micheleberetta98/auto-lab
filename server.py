from flask import Flask, render_template, request
# from servo import Servo

app = Flask(__name__)

# s1 = Servo(12)
# s2 = Servo(13)


@app.route('/')
def index():
    return render_template('controls.html')


@app.route('/pid-center')
def pid_center():
    return ''
