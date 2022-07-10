import cv2
from collections import deque
from cam import Camera
from simple_pid import PID


if __name__ == '__main__':
    camera = Camera(show_windows=True)
    pid_x = PID(0.87195, 0.77878, 0.01, setpoint=300, sample_time=0.01)
    pid_y = PID(0.87195, 0.77878, 0.01, setpoint=150, sample_time=0.01)

    while True:
        (orange, black) = camera.read_position()
        if black is not None:
            x, y = black
            print(f'Desired = (300, 150), actual = ({x}, {y})')
            print(f'PID action = ({pid_x.update(x)}, {pid_y.update(y)})')
            # print(f'PID action x = {pid_x.update(x)}')

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
