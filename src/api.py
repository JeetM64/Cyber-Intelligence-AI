from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load ML files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")
features = joblib.load("feature_names.pkl")


@app.get("/")
def home():
    return {"message": "Cyber AI running"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file, header=None)

        # Remove label columns
        df = df.iloc[:, :-2]

        # Same preprocessing as training
        df = pd.get_dummies(df)

        # Align features
        for col in features:
            if col not in df.columns:
                df[col] = 0

        df = df[features]

        # ML prediction
        scaled = scaler.transform(df)
        reduced = pca.transform(scaled)
        pred = model.predict(reduced)

        anomaly_count = int((pred == -1).sum())
        total = len(df)

        # Feature insights
        variance = df.var().sort_values(ascending=False).head(8)

        return {
            "total_records": total,
            "anomalies_detected": anomaly_count,
            "risk_percent": round(anomaly_count/total*100, 2),

            "traffic_distribution": {
                "normal": int((pred == 1).sum()),
                "anomaly": anomaly_count
            },

            "feature_variance": variance.to_dict(),

            "risk_level":
                "High" if anomaly_count/total > 0.25 else
                "Moderate" if anomaly_count/total > 0.10 else
                "Low",

            "recommendation":
                "Monitor unusual traffic spikes, IDS alerts and firewall logs."
        }

    except Exception as e:
        return {"error": str(e)}
