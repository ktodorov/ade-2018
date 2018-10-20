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

class Distance(models.Model):
    sourceLatitude = models.FloatField()
    sourceLongitude = models.FloatField()
    destinationLatitude = models.FloatField()
    destinationLongitude = models.FloatField()
    kilometers = models.FloatField()
    minutes = models.FloatField()

    def populate(self, slat, slong, dlat, dlong, km, minutes):
        self.sourceLatitude = slat
        self.sourceLongitude = slong
        self.destinationLatitude = dlat
        self.destinationLongitude = dlong
        self.kilometers = km
        self.minutes = minutes

    def __unicode__(self):
       return self.kilometers