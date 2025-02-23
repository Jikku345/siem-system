import threading
import log_monitor
import event_processor
import dashboard

def start_monitoring():
    print("Starting log monitoring...")
    log_monitor.start_monitoring("./logs")

def start_dashboard():
    print("Starting SIEM dashboard...")
    dashboard.app.run(debug=True, port=5000)

if __name__ == "__main__":
    # Start log monitoring in a separate thread
    monitor_thread = threading.Thread(target=start_monitoring)
    monitor_thread.start()

    # Start dashboard
    start_dashboard()
