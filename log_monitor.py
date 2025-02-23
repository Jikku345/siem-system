import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LogMonitor(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".log"):
            with open(event.src_path, "r") as log_file:
                lines = log_file.readlines()
                print("[LOG UPDATE] ", lines[-1].strip())

def start_monitoring(log_path):
    event_handler = LogMonitor()
    observer = Observer()
    observer.schedule(event_handler, log_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    log_path = "./logs"
    start_monitoring(log_path)
