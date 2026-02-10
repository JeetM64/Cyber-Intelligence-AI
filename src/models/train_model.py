import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest

# ======================
# LOAD DATASET
# ======================
data = pd.read_csv("data/archive/KDDTrain+.txt", header=None)
print("Dataset loaded:", data.shape)

# ======================
# REMOVE LABEL + DIFFICULTY COLUMN
# ======================
data = data.iloc[:, :-2]

# ======================
# ENCODE CATEGORICAL DATA
# ======================
data = pd.get_dummies(data)

# Ensure all column names are string
data.columns = data.columns.astype(str)

# Save feature count
feature_count = data.shape[1]
joblib.dump(feature_count, "feature_count.pkl")

print("Feature count:", feature_count)

# ======================
# FEATURE SCALING
# ======================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# ======================
# PCA DIMENSION REDUCTION
# ======================
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# ======================
# MODEL TRAINING
# ======================
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X_pca)
print("Model trained successfully")

# ======================
# SAVE EVERYTHING
# ======================
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(pca, "pca.pkl")

print("All files saved successfully")
