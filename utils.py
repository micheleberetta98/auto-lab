from multiprocessing import Process


def clamp(x, MIN, MAX):
    return max(min(x, MAX), MIN)


class ColorRange:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper


class PIDProcess():
    def __init__(self):
        self.p = None

    def start(self, target):
        self.stop()
        self.p = Process(target=target)
        self.p.start()

    def stop(self):
        if self.p is not None:
            self.p.terminate()
