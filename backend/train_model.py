import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
data = pd.read_csv("backend/data/collision_dataset.csv")

# Features and target
X = data[["distance_km", "relative_velocity_kms", "time_to_closest_min"]]
y = data["risk"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save trained model
os.makedirs("backend/models", exist_ok=True)
joblib.dump(model, "backend/models/collision_model.pkl")

print("Model saved successfully!")