# IPS-ML
ML-IPS: Intelligent Intrusion Prevention System with Real-Time Dashboard

ML-IPS is an advanced Intrusion Detection and Prevention System (IDS/IPS) built in Python that combines machine learning, rule-based detection, and real-time visualization to identify and block malicious network activity.

Inspired by enterprise-grade solutions like Suricata and modern observability stacks such as Elastic Stack, this project provides a lightweight yet powerful security platform for network monitoring, anomaly detection, and automated response.

Key Features:
Real-Time Network Monitoring

✔ Packet capture using Scapy
✔ Deep packet inspection (DPI)
✔ Live traffic analysis

Machine Learning Detection:

✔ Anomaly detection using Scikit-learn (Isolation Forest)
✔ Behavioral analysis of network traffic
✔ Detection of unknown (zero-day) threats

Rule-Based Engine (Snort-like):
Custom detection rules
Signature-based attack detection
Support for:
  ✔ SQL Injection
  ✔ Credential leaks
  ✔ Suspicious payloads
  
Intrusion Prevention (IPS):
✔ Automatic IP blocking (iptables / firewall)
✔ Temporary and dynamic blocking
✔ Risk-based response engine

Real-Time Dashboard:
✔ Web-based interface built with Flask
✔ Live alerts via WebSockets
✔ Interactive charts (similar to Kibana)

Use Cases:
✔ SOC (Security Operations Center) labs
✔ Cybersecurity training & research
✔ Network anomaly detection
✔ Blue Team / Defensive security environments
✔ Infrastructure protection (enterprise / critical systems)

Tech Stack:
✔ Python 3.x
✔ Scapy
✔ Flask + SocketIO
✔ Scikit-learn
✔ Chart.js
✔ iptables / OS Firewall

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

Disclaimer

This tool is intended for:
✔ Educational purposes
✔ Security research
✔ Authorized environments only
Do not use in networks without proper authorization.

Future Enhancements:
✔ Integration with Elasticsearch / SIEM platforms
✔ Threat Intelligence feeds (AbuseIPDB, VirusTotal)
✔ Advanced ML models (LSTM, Autoencoders)
✔ GeoIP-based blocking
✔ SOAR (Security Orchestration & Automated Response)

Contributing
Contributions, improvements, and ideas are welcome.
Feel free to open issues or submit pull requests.

License
MIT License

Caribe CyberDefense
Hans Cruz
