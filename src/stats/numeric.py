from .statistics import NumericStatistic


class Number(NumericStatistic):
    """Expects one placeholder"""

    def eval(self):
        return self.value

    def update(self, value):
        self.value += value


class Mean(NumericStatistic):
    """Expects one placeholder"""

    def update(self, value, inc_n=1):
        self.value += value
        self.n += inc_n

    def eval(self):
        if n == 0:
            return 0
        return round(self.value / self.n, self._rnd_digits)


class Ratio(NumericStatistic):
    """A ratio of value / n
    Expects two placeholders if one does not wish to see the percentage, three otherwise"""

    def __init__(self, value, r_digits=3, include_percentage=True):
        super().__init__(value, rnd_digits=r_digits)
        self._include_percentage = include_percentage

    def update(self, value, inc_n=1):
        self.value += value
        self.n += inc_n

    def eval(self):
        if self._include_percentage:
            if n == 0:
                return 0, 0, 0.0
            return (
                self.value,
                self.n,
                round(self.value / self.n * 100, self._rnd_digits),
            )
        else:
            if n == 0:
                return 0, 0
            return self.value, self.n
