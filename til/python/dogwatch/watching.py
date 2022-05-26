import os
import datetime

from watchdog.events import RegexMatchingEventHandler


class MyFileWatchHandler(RegexMatchingEventHandler):
    def __init__(self, regexes):
        super().__init__(regexes=regexes)

    def on_created(self, event):
        # Info
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print(f"{datetime.datetime.now()} {filename} created")

    def on_modified(self, event):
        pass

    def on_deleted(self, event):
        pass

    def on_moved(self, event):
        pass
