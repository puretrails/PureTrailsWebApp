file = "trash_cans.txt"
file = open(file, "r")

coordinates = []

for line in file:
    new_words = []
    if '>' in line or '<' in line:
        continue
    else:
        words = line.split(" ")

    del words[0]
    for word in words:
        if ',' in word:
            word = word.replace(',', '')
            new_words.append(word)
        if '\n' in word:
            word = word.replace('\n', '')
            new_words.append(word)

    coords = (float(new_words[0]), float(new_words[1]))
    coordinates.append(coords)

locations = []
readable_loc = []

class location:
    def __init__(self, lat, lon):
        if type(lat) is not float:
            quit()
        if type(lon) is not float:
            quit()
        self.coords = (lat, lon)
    def __str__(self):
        return ("Location at (%.10f, %.10f)\n" % (self.coords[0], self.coords[1]))

def add_loc(lat, lon):
    new_loc = location(lat, lon)
    locations.append(new_loc)
    readable_loc.append(str(new_loc))

for coord in coordinates:
    add_loc(coord[0], coord[1])

print(locations)
print(readable_loc)
