import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_scr = "C:/Users/panki/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"{event.src_path} has been created")

    def on_modified(self,event):
        print(f"{event.src_path} has been modified")

    def on_moved(self,event):
        print(f"{event.src_path} has been moved")

    def on_deleted(self,event):
        print(f"{event.src_path} has been deleted")
    
eventHandler = FileEventHandler()

observer = Observer()
observer.schedule(eventHandler,from_scr,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()