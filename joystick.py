import pygame as pg
import os

from servo import servo

# Need to bypass a pygame bug when running without GUI
os.environ['SDL_VIDEODRIVER'] = 'dummy'

print('Initializing...')
pg.init()
pg.display.init()
pg.display.set_mode((1, 1))  # Again, to bypass the same bug as before

pg.joystick.init()
joystick = pg.joystick.Joystick(0)
joystick.init()
print('Joystick OK')

sx = Servo(12)
sy = Servo(13)
print('Servo OK')

print('Now you can play!')
print('Use ^C to quit')

while True:
    try:
        pg.event.pump()

        x_val = joystick.get_axis(3)
        y_val = joystick.get_axis(4)

        sx.move_to(30 * x_val)
        sy.move_to(30 * y_val)

    except KeyboardInterrupt:
        joystick.quit()
        pg.quit()
        break
