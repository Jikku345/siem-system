from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")

# List to store alerts
alerts = []

@app.route("/")
def home():
    return render_template("dashboard.html", alerts=alerts)

@app.route("/send_alert", methods=["POST"])
def send_alert():
    data = request.get_json()
    if "alert" in data and "severity" in data:
        alerts.append({"alert": data["alert"], "severity": data["severity"]})
        return jsonify({"message": "Alert added successfully!"}), 200
    return jsonify({"error": "Invalid alert format"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
