from simple_pid import PID

BASE_X = -10
BASE_Y = -20

Ku = 0.124
Tu = 10.14  # secondi


def create_pid(setpoint, Ku=Ku, Tu=Tu):
    Kp = 0.6 * Ku
    Ki = 1.2 * Ku / Tu
    Kd = 3 * Ku * Tu / 40

    return PID(Kp, Ki, Kd, setpoint=setpoint, sample_time=0.01)
