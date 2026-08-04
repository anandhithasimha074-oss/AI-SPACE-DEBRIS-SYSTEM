from fastapi import FastAPI
from skyfield.api import load

from backend.collision_predictor import predict_collision
from backend.ai_model import predict_collision as ai_predict_collision
from digital_twin.twin import DigitalTwin
from database.database import get_prediction_history
from backend.config import (
    API_TITLE,
    API_VERSION,
    CELESTRAK_URL
)

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION
)


@app.get("/")
def home():
    return {
        "message": "AI Space Debris Tracking System API is running"
    }


@app.get("/status")
def status():
    return {
        "system": "Online",
        "collision_detection": "Active",
        "digital_twin": "Initializing",
        "reinforcement_learning": "Ready"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "api": "Running",
        "database": "Connected",
        "version": API_VERSION
    }


@app.get("/predict")
def predict():
    return predict_collision()


@app.get("/ai-predict")
def ai_predict():
    """
    AI-based collision prediction using the trained Random Forest model.
    Sample values are used for testing.
    """
    result = ai_predict_collision(
        distance_km=25,
        relative_velocity_kms=7.8,
        time_to_closest_min=6
    )

    return result


@app.get("/digital-twin")
def digital_twin():

    satellites = load.tle_file(CELESTRAK_URL)

    twin = DigitalTwin(satellites[0])

    twin.update()

    return twin.get_state()


@app.get("/history")
def history():
    return {
        "prediction_history": get_prediction_history()
    }