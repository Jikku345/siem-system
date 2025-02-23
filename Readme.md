Security Information and Event Management (SIEM) System

Overview

This SIEM System is a security monitoring tool that collects, analyzes, and displays security alerts from logs. The system includes a Flask-based web dashboard to visualize security events in real-time.

Features

Log Monitoring: Watches log files for suspicious activities.

Real-Time Alerts: Sends alerts to the web dashboard when a security event occurs.

Flask Dashboard: Displays alerts with severity levels.

API for Alert Injection: Supports external scripts to send alerts via HTTP requests.

Project Structure

siem-system/
│── logs/                # Directory for storing log files
│── scripts/             # Additional scripts for log processing
│── templates/           # HTML templates for Flask dashboard
│── main.py              # Entry point for the SIEM system
│── log_monitor.py       # Log monitoring script
│── event_processor.py   # Processes and categorizes security events
│── dashboard.py         # Web interface for viewing alerts
│── send_alert.py        # Script to send test alerts
│── requirements.txt     # List of required Python packages
│── README.md            # Project documentation

Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/siem-system.git
cd siem-system

2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Start the SIEM Dashboard

python dashboard.py

✅ Open http://127.0.0.1:5000 to view alerts.

5️⃣ Send a Test Alert

python send_alert.py

✅ The alert should now appear on the dashboard.

API Endpoints

GET / - Displays the web dashboard.

POST /send_alert - Sends an alert (JSON format required):

{
  "alert": "Unauthorized login detected!",
  "severity": "High"
}

Troubleshooting

ModuleNotFoundError: No module named 'requests'

pip install requests

Flask App Not Running?
Check if another process is using port 5000:

netstat -ano | findstr :5000   # Windows
lsof -i :5000                  # macOS/Linux

If in use, run Flask on another port:

python dashboard.py --port 5001

Contributing

Feel free to submit issues or pull requests to enhance this SIEM system!

License

This project is licensed under the MIT License.

