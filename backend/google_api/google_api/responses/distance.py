class Distance:
    kilometers = 0.0
    minutes = 0.0

    def __init__(self, kilometers, minutes):
        self.kilometers = kilometers
        self.minutes = minutes

    def toJson(self):
        return { "kilometers" : self.kilometers, "minutes" : self.minutes }