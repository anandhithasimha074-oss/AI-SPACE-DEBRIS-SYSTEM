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

    satellites = satellites[:10]  # Check first 10 satellites

    print(f"\nChecking {len(satellites)} satellites...\n")

    for i in range(len(satellites)):
        for j in range(i + 1, len(satellites)):

            sat1 = satellites[i]
            sat2 = satellites[j]

            pos1 = sat1.at(t).position.km
            pos2 = sat2.at(t).position.km

            distance = calculate_distance(pos1, pos2)

            if distance < 50:
                status = "🚨 COLLISION RISK"
            elif distance < 200:
                status = "⚠ HIGH RISK"
            elif distance < 500:
                status = "🟡 MEDIUM RISK"
            else:
                status = "🟢 SAFE"

            print(f"{sat1.name} ↔ {sat2.name}")
            print(f"Distance : {distance:.2f} km")
            print(f"Status   : {status}")
            print("-" * 60)

if __name__ == "__main__":
    detect_collisions()