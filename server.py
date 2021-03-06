from cam import scale, center
from flask import Flask, render_template, request
from main import main_loop
from joystick import event_loop
from utils import PIDProcess

app = Flask(__name__)


p = PIDProcess()


@app.route('/')
def index():
    return render_template('controls.html')


@app.route('/pid-center')
def pid_center():
    global p
    p.start(main_loop, args=(center,))
    return ''


@app.route('/pid-position')
def pid_position():
    global p
    target_x = int(request.args['posx']) * scale
    target_y = int(request.args['posy']) * scale
    target = (target_x, target_y)

    p.start(main_loop, args=(target,))
    return ''


@app.route('/pid-joystick')
def pid_joystick():
    global p
    s = int(request.args['sensitivity'])
    p.start(event_loop, args=(s,))
    return ''


@ app.route('/pid-stop')
def pid_stop():
    global p
    p.stop()
    return ''
