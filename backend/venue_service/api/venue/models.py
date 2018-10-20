from django.db import models

class Venue:
    name = ""
    latitude = 0.0
    longitude = 0.0

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class ScoredVenue(Venue):
    score = 0.0

    def __init__(self, venue, score):
        super().__init__(venue.name, venue.latitude, venue.longitude)
        self.score = score