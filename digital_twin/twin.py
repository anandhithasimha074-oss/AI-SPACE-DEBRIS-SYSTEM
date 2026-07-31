from skyfield.api import load


class DigitalTwin:

    def __init__(self, satellite):

        self.name = satellite.name
        self.latitude = 0
        self.longitude = 0
        self.altitude = 0
        self.fuel = 100

        self.satellite = satellite

    def update(self):

        ts = load.timescale()
        t = ts.now()

        geocentric = self.satellite.at(t)
        subpoint = geocentric.subpoint()

        self.latitude = subpoint.latitude.degrees
        self.longitude = subpoint.longitude.degrees
        self.altitude = subpoint.elevation.km

    def display(self):

        print("=" * 50)
        print("Digital Twin")
        print("=" * 50)

        print("Satellite :", self.name)
        print(f"Latitude  : {self.latitude:.2f}")
        print(f"Longitude : {self.longitude:.2f}")
        print(f"Altitude  : {self.altitude:.2f} km")
        print(f"Fuel      : {self.fuel}%")

        print("=" * 50)


if __name__ == "__main__":

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

    satellites = load.tle_file(url)

    twin = DigitalTwin(satellites[0])

    twin.update()

    twin.display()