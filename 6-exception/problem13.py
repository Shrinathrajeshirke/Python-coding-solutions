# Creates a Logger class
# Logs messages to "log.txt"
# Log levels: INFO, WARNING, ERROR
# Each log has timestamp
# Methods:

# info(message)
# warning(message)
# error(message)
# show_logs()
# clear_logs()

from datetime import datetime

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def write_log(self, level, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{level:7}] {time} | {message}\n"

        with open(self.filename, "a") as f:
            f.write(log_line)

    def info(self, message):
        self.write_log("INFO", message)

    def warning(self, message):
        self.warning("WARNING", message)

    def error(self, message):
        self.warning("ERROR", message)

    def show_logs(self):
        try:
            with open(self.filename, "r") as f:
                print("=== Logs ===")
                lines = f.readlines()
                if not lines:
                    print("No logs yet")
                else:
                    for line in lines:
                        print(line, end="")
        except FileNotFoundError:
            print("file not found")
        
    def clear_logs(self):
        with open(self.filename, "w") as f:
            pass
    

log = Logger("log.txt")
log.info("Program started")
log.warning("Low memory!")
log.error("File not found!")
log.show_logs()