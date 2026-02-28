from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI()

# CORS enable (frontend html එකෙන් call කරන්න)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
BASE = Path(__file__).resolve().parent
MODEL_DIR = BASE / "weather_model_artifacts"

condition_model = joblib.load(MODEL_DIR / "condition_model.joblib")
temp_model = joblib.load(MODEL_DIR / "temp_model.joblib")
wind_model = joblib.load(MODEL_DIR / "wind_model.joblib")
label_encoder = joblib.load(MODEL_DIR / "label_encoder.joblib")

@app.get("/")
def home():
    return {"message": "Weather API running"}

@app.get("/predict")
def predict(city: str = Query(...), month: str = Query(...)):

    X_in = pd.DataFrame([{"city": city, "month": month}])

    # Predict condition
    cond_idx = condition_model.predict(X_in)[0]
    condition = label_encoder.inverse_transform([cond_idx])[0]

    # Predict temperature
    temp = float(temp_model.predict(X_in)[0])

    # Predict windspeed
    wind = float(wind_model.predict(X_in)[0])

    return {
        "city": city,
        "month": month,
        "weather_condition": condition,
        "temperature": round(temp, 2),
        "windspeed": round(wind, 2)
    }
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI()

# CORS enable (frontend html එකෙන් call කරන්න)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
BASE = Path(__file__).resolve().parent
MODEL_DIR = BASE / "weather_model_artifacts"

condition_model = joblib.load(MODEL_DIR / "condition_model.joblib")
temp_model = joblib.load(MODEL_DIR / "temp_model.joblib")
wind_model = joblib.load(MODEL_DIR / "wind_model.joblib")
label_encoder = joblib.load(MODEL_DIR / "label_encoder.joblib")

@app.get("/")
def home():
    return {"message": "Weather API running"}

@app.get("/predict")
def predict(city: str = Query(...), month: str = Query(...)):

    X_in = pd.DataFrame([{"city": city, "month": month}])

    # Predict condition
    cond_idx = condition_model.predict(X_in)[0]
    condition = label_encoder.inverse_transform([cond_idx])[0]

    # Predict temperature
    temp = float(temp_model.predict(X_in)[0])

    # Predict windspeed
    wind = float(wind_model.predict(X_in)[0])

    return {
        "city": city,
        "month": month,
        "weather_condition": condition,
        "temperature": round(temp, 2),
        "windspeed": round(wind, 2)
    }