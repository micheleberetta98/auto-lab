import cv2
from collections import deque
from cam import Camera, center
from datetime import datetime
from simple_pid import PID
from servo import Servo

Ku = 0.124
Tu = 10.14  # secondi

Kp = 0.6 * Ku
Ki = 1.2 * Ku / Tu
Kd = 3 * Ku * Tu / 40

output_limits = (-60, 60)
sample_time = 0.01

if __name__ == '__main__':
    s1 = Servo(12)
    s2 = Servo(13)

    camera = Camera(show_windows=True)
    pid_x = PID(Kp, Ki, Kd, setpoint=center[0], output_limits=output_limits, sample_time=sample_time)
    pid_y = PID(Kp, Ki, Kd, setpoint=center[1], output_limits=output_limits, sample_time=sample_time)

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
            print(f'\tAngle x = {control_x}\t\tAngle y = {control_y}')
            print(f'\Desired = {center}\t\Actual = ({x}, {y})')

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
