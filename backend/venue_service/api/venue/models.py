from django.db import models

class Venue:
    name = ""
    latitude = 0.0
    longitude = 0.0

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude