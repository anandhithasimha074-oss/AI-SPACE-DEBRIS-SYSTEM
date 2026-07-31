from skyfield.api import load
from datetime import datetime


class DigitalTwin:

    def __init__(self, satellite):

        self.name = satellite.name
        self.latitude = 0
        self.longitude = 0
        self.altitude = 0
        self.velocity = 0
        self.fuel = 100
        self.risk_status = "Unknown"
        self.last_updated = None

        self.satellite = satellite


    def update(self):

        ts = load.timescale()
        t = ts.now()

        geocentric = self.satellite.at(t)

        subpoint = geocentric.subpoint()

        self.latitude = round(subpoint.latitude.degrees, 4)
        self.longitude = round(subpoint.longitude.degrees, 4)
        self.altitude = round(subpoint.elevation.km, 2)

        self.last_updated = datetime.now().strftime("%H:%M:%S")

        self.risk_status = "Monitoring"


    def get_state(self):

        return {
            "satellite": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "altitude_km": self.altitude,
            "fuel_percentage": self.fuel,
            "risk_status": self.risk_status,
            "last_updated": self.last_updated
        }


    def display(self):

        print("=" * 50)
        print("Digital Twin")
        print("=" * 50)

        print("Satellite :", self.name)
        print("Latitude :", self.latitude)
        print("Longitude :", self.longitude)
        print("Altitude :", self.altitude, "km")
        print("Fuel :", self.fuel, "%")
        print("Risk :", self.risk_status)

        print("=" * 50)


if __name__ == "__main__":

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

    satellites = load.tle_file(url)

    twin = DigitalTwin(satellites[0])

    twin.update()

    twin.display()

    print(twin.get_state())