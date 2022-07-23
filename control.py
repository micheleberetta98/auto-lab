from simple_pid import PID

BASE_X = -10
BASE_Y = -15

Ku = 0.124
Tu = 10.14  # secondi


def create_pid(setpoint, base, Ku=Ku, Tu=Tu):
    Kp = 0.6 * Ku
    Ki = 1.2 * Ku / Tu
    Kd = 3 * Ku * Tu / 40

    f = PID(Kp, Ki, Kd, setpoint=setpoint, sample_time=0.01)

    def pid(v):
        return f(v) + base

    return pid
