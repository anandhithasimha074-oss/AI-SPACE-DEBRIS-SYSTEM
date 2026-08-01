from skyfield.api import load

def load_satellite_data():
    print("Downloading latest satellite data...")

    stations_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

    satellites = load.tle_file(stations_url)

    print(f"Successfully loaded {len(satellites)} satellites.\n")

    satellite_list = []

    for sat in satellites:
        satellite_info = {
            "name": sat.name,
            "status": "SAFE",
            "fuel": 100,
            "collision_probability": 0,
            "velocity": None,
            "position": None
        }

        satellite_list.append(satellite_info)

    return satellite_list


if __name__ == "__main__":
    satellites = load_satellite_data()

    print("First 10 Satellites:\n")

    for satellite in satellites[:10]:
        print(satellite)