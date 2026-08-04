import joblib
import os
import numpy as np

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "collision_model.pkl")
model = joblib.load(MODEL_PATH)

print("AI Model loaded successfully!")

def predict_collision(distance_km, relative_velocity_kms, time_to_closest_min):
    """
    Predict collision risk.

    Returns:
        1 -> Collision Risk
        0 -> Safe Orbit
    """

    input_data = np.array([[distance_km, relative_velocity_kms, time_to_closest_min]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return {
            "prediction": "Collision Risk",
            "risk": 1
        }
    else:
        return {
            "prediction": "Safe Orbit",
            "risk": 0
        }


# Example test
if __name__ == "__main__":
    result = predict_collision(25, 7.8, 6)
    print(result)