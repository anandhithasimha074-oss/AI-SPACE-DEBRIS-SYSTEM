from skyfield.api import load


def predict_satellite_positions():
    print("Loading satellite data...")

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    satellites = load.tle_file(url)

    ts = load.timescale()
    t = ts.now()

    print(f"\nLoaded {len(satellites)} satellites.\n")

    print("Current Positions of First 5 Satellites\n")

    for satellite in satellites[:5]:

        geocentric = satellite.at(t)

        subpoint = geocentric.subpoint()

        print(f"Satellite : {satellite.name}")
        print(f"Latitude  : {subpoint.latitude.degrees:.2f}°")
        print(f"Longitude : {subpoint.longitude.degrees:.2f}°")
        print(f"Altitude  : {subpoint.elevation.km:.2f} km")
        print("-" * 50)


if __name__ == "__main__":
    predict_satellite_positions()