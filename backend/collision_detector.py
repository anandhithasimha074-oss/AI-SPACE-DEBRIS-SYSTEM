from skyfield.api import load
import numpy as np


def calculate_distance(pos1, pos2):
    return np.linalg.norm(pos1 - pos2)


def detect_collisions():

    print("Loading satellite data...")

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    satellites = load.tle_file(url)

    ts = load.timescale()
    t = ts.now()

    sat1 = satellites[0]
    sat2 = satellites[1]

    pos1 = sat1.at(t).position.km
    pos2 = sat2.at(t).position.km

    distance = calculate_distance(pos1, pos2)

    print(f"\nSatellite 1 : {sat1.name}")
    print(f"Satellite 2 : {sat2.name}")

    print(f"\nDistance = {distance:.2f} km")

    if distance < 50:
        print("\n⚠ Collision Risk Detected!")
    else:
        print("\n✅ Safe Distance")


if __name__ == "__main__":
    detect_collisions()