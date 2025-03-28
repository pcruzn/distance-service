class Position:
    def __init__(self, latitude, longitude, altitude):
        if latitude > 90.0 or latitude < -90.0:
            raise ValueError("Latitude out of range!")
        if longitude > 180.0 or longitude < -180.0:
            raise ValueError("Longitude out of range!")

        self._latitude = float(latitude)
        self._longitude = float(longitude)
        self._altitude = float(altitude)

    def __dict__(self):
        return {
            "latitude": self._latitude,
            "longitude": self._longitude,
            "altitude": self._altitude,
        }

    def __str__(self):
        return "Position is: {} {} {}".format(
            self._latitude, self._longitude, self._altitude
        )


class Waypoint(Position):
    def __init__(self, name, latitude, longitude, altitude):
        super().__init__(latitude, longitude, altitude)
        self.__name = name

    def __dict__(self):
        return {
            "name": self.__name,
            "latitude": self._latitude,
            "longitude": self._longitude,
            "altitude": self._altitude,
        }


class Trackpoint(Position):
    def __init__(self, latitude, longitude, altitude):
        super().__init__(latitude, longitude, altitude)

    def __dict__(self):
        return {
            "name": self.__name,
            "latitude": self._latitude,
            "longitude": self._longitude,
            "altitude": self._altitude,
    }
