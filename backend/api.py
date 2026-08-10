from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from skyfield.api import load

from backend.collision_predictor import predict_collision
from backend.ai_model import predict_collision as ai_predict_collision
from digital_twin.twin import DigitalTwin
from database.database import get_prediction_history
from backend.reinforcement_agent import reinforcement_decision
from backend.config import (
    API_TITLE,
    API_VERSION,
    CELESTRAK_URL,
    SATELLITES_TO_ANALYZE
)

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://127.0.0.1:5000",
    "http://localhost:5000",
],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    try:

        predictions = predict_collision()

        for item in predictions:

            for prediction in item.get("predictions", []):

                distance = prediction.get("distance_km", 999999)
                risk_status = prediction.get("status", "Safe Orbit")

                rl_decision = reinforcement_decision(
                    risk_status,
                    distance
                )

                prediction["recommended_action"] = rl_decision["recommended_action"]
                prediction["priority"] = rl_decision["priority"]
                prediction["fuel_consumption"] = rl_decision["fuel_consumption"]
                prediction["reason"] = rl_decision["reason"]

        return predictions

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/ai-predict")
def ai_predict():
    try:
        return ai_predict_collision(
            distance_km=25,
            relative_velocity_kms=7.8,
            time_to_closest_min=6
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/digital-twin")
def digital_twin():
    try:
        satellites = load.tle_file(CELESTRAK_URL)

        twin = DigitalTwin(satellites[0])
        twin.update()

        return twin.get_state()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/history")
def history():
    try:
        return {
            "prediction_history": get_prediction_history()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/satellites")
def satellites():
    try:
        satellites = load.tle_file(CELESTRAK_URL)
        satellites = satellites[:SATELLITES_TO_ANALYZE]

        satellite_data = []

        ts = load.timescale()
        current_time = ts.now()

        for index, sat in enumerate(satellites):

            position = sat.at(current_time).position.km
            velocity = sat.at(current_time).velocity.km_per_s

            altitude = round(
                float(
                    (position[0] ** 2 +
                     position[1] ** 2 +
                     position[2] ** 2) ** 0.5
                    - 6371
                ),
                2
            )

            speed = round(
                float(
                    (velocity[0] ** 2 +
                     velocity[1] ** 2 +
                     velocity[2] ** 2) ** 0.5
                ),
                2
            )

            # Estimated fuel level for dashboard simulation
            fuel_levels = [100, 90, 80, 70, 60]
            fuel = fuel_levels[index % len(fuel_levels)]

            # Determine satellite status
            if altitude < 300:
                status = "MONITORING"
            elif altitude < 2000:
                status = "SAFE"
            elif altitude < 35786:
                status = "SAFE"
            else:
                status = "SAFE"

            satellite_data.append({
                "id": sat.name,
                "altitude_km": altitude,
                "velocity_kms": speed,
                "fuel_percentage": fuel,
                "status": status
            })

        return satellite_data

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )