import requests

url = "http://127.0.0.1:5000/send_alert"

alert_data = {
    "alert": "Unauthorized login attempt detected!",
    "severity": "High"
}

response = requests.post(url, json=alert_data)

print("Response:", response.json())
