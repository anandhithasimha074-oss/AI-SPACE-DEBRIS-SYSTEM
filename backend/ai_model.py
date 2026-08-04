import joblib
import os
import numpy as np

# Load the trained model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "collision_model.pkl"
)

model = joblib.load(MODEL_PATH)

print("AI Model loaded successfully!")


def predict_collision(
    distance_km,
    relative_velocity_kms,
    time_to_closest_min
):
    """
    Predict collision risk using the trained Random Forest model.

    Returns:
    {
        prediction,
        risk,
        confidence
    }
    """

    input_data = np.array([
        [
            distance_km,
            relative_velocity_kms,
            time_to_closest_min
        ]
    ])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        return {
            "prediction": "Collision Risk",
            "risk": 1,
            "confidence": confidence
        }

    return {
        "prediction": "Safe Orbit",
        "risk": 0,
        "confidence": confidence
    }


if __name__ == "__main__":

    result = predict_collision(
        25,
        7.8,
        6
    )

    print(result)