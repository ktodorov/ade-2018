from .venue import Venue

class ScoredVenue(Venue):
    score = 0.0

    def __init__(self, venue, score):
        super().__init__(venue.name, venue.latitude, venue.longitude)
        self.score = score