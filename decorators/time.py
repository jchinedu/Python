from tomlkit import value


class TimeWithProperties:
    def __init__(self, second, minute, hour):
        self.second = second
        self.minute = minute
        self.hour = hour

    @property
    def second(self):
        return self.second

    def seconds(self):
        if value < 0 and value > 59:
            raise ValueError("seconds must be between 0 and 69")
        self_second = value

    time1 = timeWithProperties()