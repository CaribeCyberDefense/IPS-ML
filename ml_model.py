#Modelo de detección de anomalías con Isolation Forest:
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Modelo global
model = IsolationForest(contamination=0.05)

# Dataset inicial (simulado)
# [packet_size, num_ports, frequency]
training_data = np.array([
    [500, 2, 10],
    [600, 3, 15],
    [450, 1, 8],
    [700, 2, 12],
])

model.fit(training_data)

# Guardar modelo
joblib.dump(model, "model.pkl")

def load_model():
    return joblib.load("model.pkl")

def predict(features):
    model = load_model()
    prediction = model.predict([features])
    return prediction[0]  # -1 = anomalía