from django.db import models

class DbDistance(models.Model):
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