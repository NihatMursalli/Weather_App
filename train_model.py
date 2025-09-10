import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import numpy as np

# Create dummy dataset
np.random.seed(42)
data = pd.DataFrame({
    "day": np.tile(range(1, 29), 12),
    "month": np.repeat(range(1, 13), 28),
    "temp": np.random.uniform(10, 35, 336),
    "humidity": np.random.uniform(30, 90, 336),
    "wind": np.random.uniform(0, 15, 336),
    "visibility": np.random.uniform(1, 10, 336),
    "clouds": np.random.randint(0, 2, 336),
    "pressure": np.random.uniform(980, 1030, 336),
    "target": np.random.uniform(10, 35, 336)  # next day temp
})

X = data.drop("target", axis=1)
y = data["target"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
