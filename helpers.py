# module name: helpers.py
from geo_location import Position
import geopy.distance


class Distance:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def km(self):
        return geopy.distance.geodesic(
            ((self.source.__dict__())["latitude"],
             (self.source.__dict__()["longitude"])),
            ((self.destination.__dict__())["latitude"],
             (self.destination.__dict__()["longitude"]))
        ).km

    def nautical(self):
        return geopy.distance.geodesic(
            ((self.source.__dict__())["latitude"],
             (self.source.__dict__()["longitude"])),
            ((self.destination.__dict__())["latitude"],
             (self.destination.__dict__()["longitude"]))
        ).nautical


#print(
#    Distance(
#        Position(-33.0351516, -71.5955963, None),
#        Position(-33.0348327, -71.5980458, None)
#    ).km()
#)

