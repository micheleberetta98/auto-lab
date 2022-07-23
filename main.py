import cv2
from cam import Camera, center
from collections import deque
from control import create_pid, BASE_X, BASE_Y
from datetime import datetime
from servo import Servo
from simple_pid import PID


def main_loop(open_camera_frame=False):
    s1 = Servo(12, base=BASE_X)
    s2 = Servo(13, base=BASE_Y)

    camera = Camera(show_windows=open_camera_frame)
    pid_x = create_pid(center[0])
    pid_y = create_pid(center[1], Ku=0.130)

    while True:
        orange = camera.read_position()
        if orange is None:
            s1.move_to(0)
            s2.move_to(0)
        else:
            (x, y) = orange
            control_x = pid_x(x)
            control_y = pid_y(y)

            s1.move_to(control_x)
            s2.move_to(control_y)

            print(f'Time: {datetime.now()}')
            print(f'\tAngle x = {control_x}\tAngle y = {control_y}')
            print(f'\tDesired = {center}\tActual = ({x}, {y})')

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()


if __name__ == '__main__':
    main_loop(open_camera_frame=False)
