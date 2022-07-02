from utils import clamp, SlidingQueue


class PID():
    def __init__(self, Kp, Ki, Kd, target):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.speeds = SlidingQueue()
        self.target = target
        self.integral = 0
        self.last_value = 0

    def update(self, x, invert=False):
        dt = 0.01
        k_inv = -1 if invert else 1

        # Derivative part
        self.speeds.add(x - self.last_value)
        self.last_value = x
        dx = k_inv * saturation_filter(self.speeds.avg())

        # Error (proportional part)
        error = k_inv * (self.target - x)

        # Integral
        self.integral = saturation_filter(self.integral + error * dt)

        # All together
        P = self.Kp * error
        I = self.Ki * self.integral
        D = self.Kd * (dx / dt)

        return saturation_filter(P + I + D)


def saturation_filter(x):
    return clamp(x, -150, 150)
