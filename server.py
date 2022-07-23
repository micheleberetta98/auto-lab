from flask import Flask, render_template, request
from time import sleep
from main import main_loop
from utils import PIDProcess

app = Flask(__name__)


p = PIDProcess()


@app.route('/')
def index():
    return render_template('controls.html')


@app.route('/pid-center')
def pid_center():
    global p
    p.start(main_loop())
    return ''


@app.route('/pid-stop')
def pid_stop():
    global p
    p.stop()
    return ''
