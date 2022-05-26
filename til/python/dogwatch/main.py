import time
from watching import MyFileWatchHandler
from watchdog.observers import Observer

if __name__ == "__main__":
    DIR_WATCH = "tmp"         # target dir
    PATTERNS = [r'^.*\.json$']  # target file patterns

    event_handler = MyFileWatchHandler(PATTERNS)

    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
