from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from utils import clamp
from time import sleep


class Servo():
    def __init__(self, pin, min_angle=-90, max_angle=90):
        self.servo = AngularServo(pin, min_angle=min_angle, max_angle=max_angle, pin_factory=PiGPIOFactory())
        self._min = min_angle
        self._max = max_angle
        self.move_to(0)

    def move_to(self, angle):
        self._set(angle)

    def up(self, delta=10):
        self._set(self.servo.angle + delta)

    def down(self, delta=10):
        self._set(self.servo.angle - delta)

    def _set(self, angle):
        self.servo.angle = clamp(angle, self._min, self._max)


if __name__ == '__main__':
    s = Servo(12)
    for angle in [-90, -75, -50, -25, 0, 25, 50, 75, 90]:
        s.move_to(angle)
        sleep(0.5)
    s.move_to(0)

    s = Servo(13)
    for angle in [-90, -75, -50, -25, 0, 25, 50, 75, 90]:
        s.move_to(angle)
        sleep(0.5)
    s.move_to(0)
