from curses import keyname
import os,shutil,time,random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_path = '/Users/shreyjkatrodiya/Downloads'



class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey,{event.src_path}has been created!")
    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}")
    def on_modified(self,event):
        print(f"Hey,{event.src_path}has been modified!")
    def on_move(self,event):
        print(f"Someone move {event.src_path}")

event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,from_path,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("its running")

except KeyboardInterrupt:
    print("it's stop")
    observer.stop()