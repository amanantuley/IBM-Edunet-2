import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("hour.csv")

# Feature Engineering
df['dayofweek'] = pd.to_datetime(df['dteday']).dt.dayofweek
features = ['temp', 'hum', 'windspeed', 'season', 'yr', 'mnth', 'holiday',
            'weekday', 'workingday', 'weathersit', 'hr', 'dayofweek']
X = df[features]
y = df['cnt']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Save model
joblib.dump(model, "bike_model.pkl")
