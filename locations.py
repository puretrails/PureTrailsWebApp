from read_loc import *

locations = []

class location:
    def __init__(self, lat, lon):
        if type(lat) is not float:
            quit()
        if type(lon) is not float:
            quit()
        self.coords = (lat, log)
    def __str__(self):
        return ("Location at (%d, %d)\n", self.place, self.coords[0], self.coord[1])

def add_loc(place, lat, lon):
    new_loc = location(lat, lon)
    locations.append(new_loc)
