from skyfield.api import load
import numpy as np

SAFE_DISTANCE = 50  # km


def calculate_distance(pos1, pos2):
    return np.linalg.norm(pos1 - pos2)


def predict_collision():
    print("Predicting future collision risk...")

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

    satellites = load.tle_file(url)

    ts = load.timescale()

    sat1 = satellites[0]
    sat2 = satellites[1]

    future_times = [
        ts.now(),
        ts.now() + 5 / 1440,
        ts.now() + 10 / 1440
    ]

    for t in future_times:

        pos1 = sat1.at(t).position.km
        pos2 = sat2.at(t).position.km

        distance = calculate_distance(pos1, pos2)

        print("-" * 40)
        print("Time :", t.utc_strftime("%H:%M:%S"))
        print("Distance :", round(distance, 2), "km")

        if distance < SAFE_DISTANCE:
            print("⚠ Collision Risk")
        else:
            print("✅ Safe")


if __name__ == "__main__":
    predict_collision()