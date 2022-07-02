from collections import deque
import argparse
import imutils
import cv2
import cam
from pid import PID


if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    pid_x = PID(0.87195, 0.77878, 0.01, target=300)
    pid_y = PID(0.87195, 0.77878, 0.01, target=150)

    while True:
        (orange, black) = cam.read_position(camera)
        if black is not None:
            x, y = black
            print(f'Desired = (300, 150), actual = ({x}, {y})')
            print(f'PID action = ({pid_x.update(x)}, {pid_y.update(y)})')
            # print(f'PID action x = {pid_x.update(x)}')

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()
