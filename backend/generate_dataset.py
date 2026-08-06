import pandas as pd
import random
import os

random.seed(42)

data = []

for _ in range(200):

    distance = round(random.uniform(5, 150), 2)
    velocity = round(random.uniform(5.5, 15.5), 2)
    time_to_closest = round(random.uniform(1, 30), 2)

    # Simple rule for generating labels
    if distance < 40 and velocity > 10 and time_to_closest < 10:
        risk = 1
    else:
        risk = 0

    data.append([
        distance,
        velocity,
        time_to_closest,
        risk
    ])

df = pd.DataFrame(
    data,
    columns=[
        "distance_km",
        "relative_velocity_kms",
        "time_to_closest_min",
        "risk"
    ]
)

output_path = os.path.join(
    os.path.dirname(__file__),
    "data",
    "collision_dataset.csv"
)

df.to_csv(output_path, index=False)

print(f"Dataset generated successfully!")
print(f"Total samples: {len(df)}")
print(f"Saved to: {output_path}")