import time
import sys

from watchdog.events import FileSystemEvent, FileModifiedEvent, FileSystemEventHandler
from watchdog.observers import Observer


class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event: FileSystemEvent) -> None:
        if type(event) == FileModifiedEvent:
            print(event.src_path)

if len(sys.argv) != 2:
    sys.exit(f"usage: main.py <path>")

path = sys.argv[1]

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
