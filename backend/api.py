from fastapi import FastAPI
from backend.collision_predictor import predict_collision
from skyfield.api import load
from digital_twin.twin import DigitalTwin

app = FastAPI(
    title="AI Space Debris Tracking API",
    version="1.0"
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
@app.get("/predict")
def predict():
    return predict_collision()
@app.get("/digital-twin")
def digital_twin():

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

    satellites = load.tle_file(url)

    twin = DigitalTwin(satellites[0])

    twin.update()

    return twin.get_state()