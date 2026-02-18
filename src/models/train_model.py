import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest

data = pd.read_csv("data/archive/KDDTrain+.txt", header=None)
data = data.iloc[:, :-2]

data = pd.get_dummies(data)
data.columns = data.columns.astype(str)

joblib.dump(list(data.columns), "feature_names.pkl")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

pca = PCA(n_components=5)
X_pca = pca.fit_transform(X_scaled)

model = IsolationForest(contamination=0.05)
model.fit(X_pca)

joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(pca, "pca.pkl")
