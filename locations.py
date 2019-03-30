locations = []

class location:
    def __init__(self, place, lat, lon):
        if type(place) is not str:
            quit()
        if type(lat) is not int:
            quit()
        if type(lon) is not int:
            quit()
        self.place = place
        self.coords = (lat, log)
    def __str__(self):
        return ("%s at (%d, %d)\n", self.place, self.coords[0], self.coord[1])

def add_loc(place, lat, lon):
    new_loc = location(place, lat, lon)
    locations.append(new_loc)
