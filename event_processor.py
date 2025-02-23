import json

def analyze_log(log_entry):
    if "failed login" in log_entry.lower():
        return {"alert": "Failed Login Attempt Detected", "severity": "High"}
    elif "unauthorized access" in log_entry.lower():
        return {"alert": "Unauthorized Access Detected", "severity": "Critical"}
    return None

def process_logs(log_file):
    with open(log_file, "r") as f:
        logs = f.readlines()
    
    alerts = []
    for log in logs:
        alert = analyze_log(log)
        if alert:
            alerts.append(alert)
    
    with open("alerts.json", "w") as alert_file:
        json.dump(alerts, alert_file, indent=4)

if __name__ == "__main__":
    process_logs("logs/security.log")