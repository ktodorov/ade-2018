import requests as req

# Finds n venues close to a city
# Returns a list of tuples (city, lat, long)
def find_venues(city,n):
    api_key = "io09K9l3ebJxmxe2"
    request = req.get("https://api.songkick.com/api/3.0/search/venues.json?query={}&apikey={}".format(city,api_key))
    venues = request.json()["resultsPage"]["results"]["venue"]
    venue_coords = []
    for venue in venues[0:n]:
        venue_coords.append((venue["displayName"],venue["lat"],venue["lng"]))

    return venue_coords

# Example
# city = "amsterdam"
# n = 30
# venue_coords = find_venues(city,n)
# print(venue_coords)