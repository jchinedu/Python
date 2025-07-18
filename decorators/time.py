class TimeWithProperties:
    def __init__(self, second=0, minute=0, hour=0):
        self.second = second
        self.minute = minute
        self.hour = hour

    @property
    def second(self):
        return self._second

    @second.setter
    def seconds(self, value):
        if  0 > value > 59:
            raise ValueError("seconds must be between 0 and 69")
        self._second = value

    @property
    def minute(self):
        return self._minute


    @minute.setter
    def minute(self, value):
        if 0 > value > 59:
            raise ValueError("minutes must be between 0 and 59")
        self._minute = value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if 0 > value > 23:
            raise ValueError("hours must be between 0 and 23")
        self._hour = value

    @second.setter
    def second(self, value):
        self._second = value

    def __str__(self):
        return f"{self.second} {self.minute} {self.hour}"


time1 = TimeWithProperties()