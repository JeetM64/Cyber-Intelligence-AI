# 🚀 Cyber Intelligence AI
AI-powered network threat detection dashboard using Machine Learning.

---

## 📌 Overview
Cyber Intelligence AI is an anomaly detection system designed to identify suspicious network traffic using machine learning.

It combines:

- FastAPI backend (ML inference)
- React dashboard frontend
- ML anomaly detection model

This project acts as a cybersecurity AI digital twin for monitoring network behavior.

---

## 🎯 Features

- Machine Learning threat detection
- Risk level prediction
- Feature importance visualization
- Network traffic insights dashboard
- CSV dataset upload support
- Interactive charts

---

## 🧠 Tech Stack

### Frontend
- React.js
- Chart.js
- CSS Dashboard UI

### Backend
- FastAPI
- Python
- Pandas / NumPy
- Scikit-learn

### ML Model
- PCA dimensionality reduction
- Isolation Forest anomaly detection

---

## 📂 Project Structure

Cyber-Intelligence-AI/
│
├── frontend/ → React dashboard  
├── src/ → FastAPI backend  
├── notebooks/ → ML experiments  
├── data/ → sample datasets  
├── model.pkl → trained ML model  
├── scaler.pkl → preprocessing scaler  
├── pca.pkl → PCA model  

---

## ▶️ How To Run Project

### 1️⃣ Clone Repo
git clone https://github.com/JeetM64/Cyber-Intelligence-AI.git

cd Cyber-Intelligence-AI

---

### 2️⃣ Backend Setup
pip install -r requirements.txt

python -m uvicorn src.api:app --reload

Backend runs on:
http://127.0.0.1:8000

---

### 3️⃣ Frontend Setup
cd frontend

npm install

npm start

Frontend runs on:
http://localhost:3000

---

## 📊 How It Works

1. Upload network CSV dataset
2. Backend preprocesses data
3. ML model detects anomalies
4. Dashboard shows:
   - Traffic ratio
   - Risk score
   - Feature importance
   - Threat insights

---

## 🚀 Future Scope

- Real-time packet monitoring
- Deep learning models
- Cloud deployment
- Alert system
- Authentication

---

## 👨‍💻 Author

Jeet Mhatre  
Machine Learning & Full Stack Developer

GitHub: https://github.com/JeetM64
