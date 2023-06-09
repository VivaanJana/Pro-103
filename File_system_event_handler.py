import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/tanuk/Downloads"
to_dir="C:/Users/tanuk/OneDrive/Desktop/Pyprojects/Project103"
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Hey, "+event.src_path+" has been created")
    def on_deleted(self, event):
        print("Oh no! "+event.src_path+" was deleted")
    def on_modified(self, event):
        print("Hey, "+event.src_path+" has been modified")
    def on_moved(self, event):
        print("Hey, "+event.src_path+" has moved")

event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)    
observer.start()
try:
    while True:
        time.sleep(2)
        print("In process")
except KeyboardInterrupt:
    print("Process breached")
    observer.stop()