from flask import Flask, render_template, request
from multiprocessing import Process
from time import sleep

app = Flask(__name__)


class PIDProcess():
    def __init__(self):
        self.p = None

    def start(self, target):
        self.stop()
        self.p = Process(target=target)
        self.p.start()

    def stop(self):
        if self.p is not None:
            self.p.terminate()


p = PIDProcess()


@app.route('/')
def index():
    return render_template('controls.html')


@app.route('/pid-center')
def pid_center():
    global p
    p.start(handle_center)
    return ''


@app.route('/pid-stop')
def pid_stop():
    global p
    p.stop()
    return ''


def handle_center():
    while True:
        print('running...')
        sleep(1)
