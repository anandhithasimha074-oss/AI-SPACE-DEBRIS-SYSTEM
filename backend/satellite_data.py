from skyfield.api import load

def load_satellite_data():
    print("Downloading latest satellite data...")

    stations_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

    satellites = load.tle_file(stations_url)

    print(f"Successfully loaded {len(satellites)} satellites.\n")

    return satellites


if __name__ == "__main__":
    satellites = load_satellite_data()

    print("First 10 Satellites:\n")

    for satellite in satellites[:10]:
        print(satellite.name)