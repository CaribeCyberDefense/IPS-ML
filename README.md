# IPS-ML
IPS con Machine Learning (detección avanzada) + Dashboard tipo Kibana en tiempo real.

Instalación completa

pip install scapy flask flask-socketio scikit-learn joblib requests

Ejecución
1. Iniciar dashboard:
python webapp.py
2. Ejecutar IPS con ML:
sudo python sensor_ml_ips.py

Funcionamiento:

Detección híbrida:

✔ Reglas tipo Snort
✔ Machine Learning (Isolation Forest)
✔ Análisis de comportamiento

Detecta:

✔ Port scanning

✔ SQL Injection

✔ Credential leaks

✔ Anomalías desconocidas (zero-day behavior)

Respuesta automática:

✔ Bloqueo de IP en tiempo real

✔ Bloqueo temporal inteligente

Dashboard tipo Kibana:

✔ Eventos en vivo

✔ Gráficas dinámicas

✔ Flujo de ataques
