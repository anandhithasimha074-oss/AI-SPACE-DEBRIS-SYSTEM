import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Example training data
X = np.array([
    [20, 7.5],
    [35, 7.8],
    [100, 7.4],
    [10, 8.0],
    [80, 7.6],
    [45, 7.7]
])

# Labels
# 1 = Collision Risk
# 0 = Safe
y = np.array([1, 1, 0, 1, 0, 0])

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

print("AI Model trained successfully!")

test_data = np.array([[25, 7.8]])

prediction = model.predict(test_data)

if prediction[0] == 1:
    print("⚠ Collision Risk Predicted")
else:
    print("✅ Safe Orbit")