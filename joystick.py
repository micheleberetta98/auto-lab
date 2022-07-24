import pygame as pg
import os

from servo import Servo
from control import BASE_X, BASE_Y


class Joystick:
    RIGHT_HANDLE_HOR_AXIS = 3
    RIGHT_HANDLE_VER_AXIS = 4

    def __init__(self, joystick_id=0):
        # Need to bypass a pygame bug when running without GUI
        os.environ['SDL_VIDEODRIVER'] = 'dummy'

        print('Initializing...')
        pg.init()
        if not pg.display.get_init():
            pg.display.init()
            pg.display.set_mode((1, 1))  # Again, to bypass the same bug as before

        if not pg.joystick.get_init():
            pg.joystick.init()

        self.j = pg.joystick.Joystick(joystick_id)
        if not self.j.get_init():
            self.j.init()
        print('Joystick OK')

    def get_handle_value(self, axis):
        val = self.j.get_axis(axis)
        return val if val is not None else 0

    def clear(self):
        self.j.quit()
        pg.quit()


def event_loop(sensitivity=30):
    j = Joystick()

    sx = Servo(12, base=BASE_X)
    sy = Servo(13, base=BASE_Y)
    print('Servo OK')

    while True:
        try:
            pg.event.pump()
            x_val = j.get_handle_value(Joystick.RIGHT_HANDLE_HOR_AXIS)
            y_val = j.get_handle_value(Joystick.RIGHT_HANDLE_VER_AXIS)

            sx.move_to(sensitivity * x_val)
            sy.move_to(sensitivity * y_val)
        except KeyboardInterrupt:
            break

    j.clear()


if __name__ == '__main__':
    event_loop(sensitivity=30)
