from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Create API app
app = FastAPI(
    title="AI Cyber Digital Twin API",
    description="Cybersecurity anomaly detection using ML",
    version="1.0"
)

# Load saved ML files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")
feature_count = joblib.load("feature_count.pkl")


# Input schema
class InputData(BaseModel):
    data: list[float]


@app.get("/")
def home():
    return {"message": "Cyber AI API running"}


@app.get("/health")
def health():
    return {"status": "API healthy"}


@app.post("/predict")
def predict(input_data: InputData):

    try:
        arr = np.array(input_data.data).reshape(1, -1)

        # Feature count check
        if arr.shape[1] != feature_count:
            return {
                "error": f"Expected {feature_count} features, got {arr.shape[1]}"
            }

        scaled = scaler.transform(arr)
        reduced = pca.transform(scaled)
        prediction = model.predict(reduced)

        if prediction[0] == -1:
            return {"result": "Anomaly detected"}
        else:
            return {"result": "Normal traffic"}

    except Exception as e:
        return {"error": str(e)}
