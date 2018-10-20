class Location:
    latitude = 0.0
    longitude = 0.0

    def __init__(self, latitude = 0.0, longitude = 0.0, json = {}):
        self.latitude = latitude
        self.longitude = longitude

        if json:
            self.latitude = json["latitude"]
            self.longitude = json["longitude"]