from skyfield.api import load
import numpy as np

from backend.explainable_ai import explain_collision
from backend.reinforcement_agent import reinforcement_decision
from backend.ai_model import predict_collision as ai_predict_collision
from database.database import save_prediction
from backend.logger import log_info, log_error

from backend.config import (
    CELESTRAK_URL,
    SAFE_DISTANCE,
    SATELLITES_TO_ANALYZE,
    PREDICTION_INTERVALS
)


def calculate_distance(pos1, pos2):
    return np.linalg.norm(pos1 - pos2)


def predict_collision():

    try:

        print("Predicting future collision risk...")
        log_info("Collision prediction started.")

        satellites = load.tle_file(CELESTRAK_URL)

        satellites = satellites[:SATELLITES_TO_ANALYZE]

        ts = load.timescale()

        current_time = ts.now()

        future_times = [
            current_time + minutes / 1440
            for minutes in PREDICTION_INTERVALS
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

                    # Temporary orbital velocity value
                    relative_velocity = 7.8

                    time_to_closest = (
                        t.utc_datetime() - current_time.utc_datetime()
                    ).total_seconds() / 60

                    ai_result = ai_predict_collision(
                        distance_km=round(float(distance), 2),
                        relative_velocity_kms=relative_velocity,
                        time_to_closest_min=max(1, round(time_to_closest, 2))
                    )

                    status = ai_result["prediction"]

                    explanation = explain_collision(
                        round(float(distance), 2),
                        status
                    )

                    maneuver = reinforcement_decision(
                        status,
                        round(float(distance), 2)
                    )

                    save_prediction(
                        sat1.name,
                        sat2.name,
                        round(float(distance), 2),
                        status,
                        maneuver["recommended_action"],
                        t.utc_strftime("%Y-%m-%d %H:%M:%S")
                    )

                    print("-" * 40)
                    print("Time :", t.utc_strftime("%H:%M:%S"))
                    print("Distance :", round(float(distance), 2), "km")
                    print("Relative Velocity :", relative_velocity, "km/s")
                    print("Status :", status)
                    print("Explanation :", explanation)
                    print("Recommended Maneuver :", maneuver)

                    log_info(
                        f"{sat1.name} - {sat2.name} | "
                        f"Distance: {round(float(distance), 2)} km | "
                        f"Status: {status}"
                    )

                    results.append({
                        "time": t.utc_strftime("%H:%M:%S"),
                        "distance_km": round(float(distance), 2),
                        "relative_velocity_kms": relative_velocity,
                        "status": status,
                        "explanation": explanation,
                        "recommended_maneuver": maneuver
                    })

                all_predictions.append({
                    "satellite_1": sat1.name,
                    "satellite_2": sat2.name,
                    "predictions": results
                })

        log_info("Collision prediction completed successfully.")

        return all_predictions

    except Exception as e:

        log_error(f"Collision prediction failed: {str(e)}")
        raise


if __name__ == "__main__":

    output = predict_collision()

    print("\nPrediction Completed Successfully!")