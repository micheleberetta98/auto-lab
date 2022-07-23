def clamp(x, MIN, MAX):
    return max(min(x, MAX), MIN)


class ColorRange:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
