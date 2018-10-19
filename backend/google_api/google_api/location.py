class Location:
    latitude = 0.0
    longitude = 0.0

    def __init__(self, json = {}):
        self.latitude = json["latitude"]
        self.longitude = json["longitude"]