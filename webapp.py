from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

alerts = []

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    alerts.append(data)

    socketio.emit("new_alert", data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)