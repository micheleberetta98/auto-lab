def clamp(x, MIN, MAX):
    return max(min(x, MAX), MIN)


class SlidingQueue():
    def __init__(self):
        self._data = [0, 0, 0, 0, 0, 0, 0, 0]

    def add(self, x):
        self._data = [x] + self._data[:-1]

    def avg(self):
        return sum(self._data) / len(self._data)
