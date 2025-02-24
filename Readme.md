# Security Information and Event Management (SIEM) System

## Project Overview
This project is a simple Security Information and Event Management (SIEM) system that monitors logs, processes security events, and displays alerts on a web dashboard.

## Features
- **Log Monitoring:** Tracks security logs in real-time.
- **Event Processing:** Analyzes logs for potential security threats.
- **Web Dashboard:** Displays alerts and system status using Flask.
- **Alert Notifications:** Sends alerts when suspicious activity is detected.

## Folder Structure
```
siem-system/
│── logs/               # Directory for storing log files
│── scripts/            # Additional scripts for data processing
│── templates/          # HTML templates for Flask dashboard
│── main.py             # Entry point of the SIEM system
│── log_monitor.py      # Script to monitor and parse logs
│── event_processor.py  # Processes logs to detect threats
│── dashboard.py        # Web interface to display alerts
│── send_alert.py       # Script to send alerts to the dashboard
│── requirements.txt    # List of dependencies
```

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Jikku345/siem-system.git
   cd siem-system
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the SIEM System
1. **Start the Log Monitor:**
   ```sh
   python log_monitor.py
   ```

2. **Start the SIEM Dashboard:**
   ```sh
   python dashboard.py
   ```
   Open your browser and go to: **http://127.0.0.1:5000**

3. **Send a Test Alert:**
   ```sh
   python send_alert.py
   ```

## Troubleshooting
- **Template Not Found Error?**
  - Ensure the `templates/` folder exists and contains `dashboard.html`.
- **ModuleNotFoundError: No module named 'requests'?**
  - Run `pip install requests` to install the missing package.
- **Git Push Issues?**
  - Run `git pull origin main --rebase` before pushing.

## License
This project is open-source and available for use under the MIT License.

