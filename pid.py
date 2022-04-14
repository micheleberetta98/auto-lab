class History():
    def __init__(self):
        self._data = [0, 0, 0, 0, 0, 0, 0, 0]
        self.dx = 0

    def add(self, x):
        self._data = [x] + self._data[:-1]

        N = len(self._data)
        self.dx = (N * self.dx - self._data[-1] + self._data[0]) / N


class PID():
    def __init__(self, Kp, Ki, Kd, target):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self._target = target
        self._integral = 0
        self.history = History()

    def update(self, x, invert=False):
        dt = 0.01
        k_inv = -1 if invert else 1

        self.history.add(x)
        dx = k_inv * saturation_filter(self.history.dx)

        # Integral
        error = k_inv * (self._target - x)
        self._integral = saturation_filter(self._integral + error * dt)

        # All together
        P = self.Kp * error
        I = self.Ki * self._integral
        D = self.Kd * (dx / dt)

        return P + I + D


def saturation_filter(x):
    return clamp(x, -150, 150)


def clamp(x, MIN, MAX):
    return max(min(x, MAX), MIN)
