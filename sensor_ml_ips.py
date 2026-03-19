from scapy.all import sniff, IP, TCP, Raw
from features import extract_features
from ml_model import predict
from response import block_ip_temporary
from rules import match_rules
import requests

DASHBOARD_URL = "http://127.0.0.1:5000/alert"

def send_alert(data):
    try:
        requests.post(DASHBOARD_URL, json=data)
    except:
        pass

def analyze_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # =====================
        # Feature extraction
        # =====================
        features = extract_features(packet, src_ip)

        # =====================
        # ML Detection
        # =====================
        result = predict(features)

        alerts = []

        if result == -1:
            alerts.append("ML Anomaly")

        # =====================
        # Rule-based detection
        # =====================
        if packet.haslayer(Raw):
            payload = str(packet[Raw].load)
            alerts.extend(match_rules(payload))

        # =====================
        # Response
        # =====================
        if alerts:
            alert_data = {
                "src": src_ip,
                "dst": dst_ip,
                "alerts": alerts,
                "features": features
            }

            send_alert(alert_data)

            # 🔴 Bloqueo automático
            if "ML Anomaly" in alerts:
                block_ip_temporary(src_ip)

def start():
    sniff(filter="ip", prn=analyze_packet, store=0)

if __name__ == "__main__":
    print("[*] ML IPS corriendo...")
    start()