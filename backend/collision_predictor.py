from skyfield.api import load
import numpy as np
from backend.explainable_ai import explain_collision
from backend.reinforcement_agent import reinforcement_decision

SAFE_DISTANCE = 50  # km


def calculate_distance(pos1, pos2):
    return np.linalg.norm(pos1 - pos2)


def predict_collision():

    print("Predicting future collision risk...")

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

    satellites = load.tle_file(url)

    satellites = satellites[:5]   # Analyze first 5 satellites

    ts = load.timescale()

    future_times = [
        ts.now(),
        ts.now() + 5 / 1440,
        ts.now() + 10 / 1440
    ]

    all_predictions = []

    for i in range(len(satellites)):
        for j in range(i + 1, len(satellites)):

            sat1 = satellites[i]
            sat2 = satellites[j]

            print("\n" + "=" * 60)
            print(f"{sat1.name}  ↔  {sat2.name}")
            print("=" * 60)

            results = []

            for t in future_times:

                pos1 = sat1.at(t).position.km
                pos2 = sat2.at(t).position.km

                distance = calculate_distance(pos1, pos2)

                if distance < SAFE_DISTANCE:
                    status = "Collision Risk"
                else:
                    status = "Safe"

                explanation = explain_collision(
                    round(distance, 2),
                    status
                )

                maneuver = reinforcement_decision(
                    status,
                    round(distance, 2)
                )

                print("-" * 40)
                print("Time :", t.utc_strftime("%H:%M:%S"))
                print("Distance :", round(distance, 2), "km")
                print("Status :", status)
                print("Explanation :", explanation)
                print("Recommended Maneuver :", maneuver)

                results.append({
                    "time": t.utc_strftime("%H:%M:%S"),
                    "distance_km": round(distance, 2),
                    "status": status,
                    "explanation": explanation,
                    "recommended_maneuver": maneuver
                })

            all_predictions.append({
                "satellite_1": sat1.name,
                "satellite_2": sat2.name,
                "predictions": results
            })

    return all_predictions


if __name__ == "__main__":

    output = predict_collision()

    print("\nPrediction Completed Successfully!")