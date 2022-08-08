from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
# class MyHandler(FileSystemEventHandler):
#     def on_any_event(self, event):
#         print(event.event_type, event.src_path)

#     def on_created(self, event):
#         print("on_created", event.src_path)

#     def on_deleted(self, event):
#         print("on_deleted", event.src_path)

#     def on_modified(self, event):
#         print("on_modified", event.src_path)

#     def on_moved(self, event):
#         print("on_moved", event.src_path)
    
# event_handler = MyHandler()
# observer = Observer()
# observer.schedule(event_handler, path='C:/Users/Admin/YandexDisk/groc_alg/test_bot', recursive=False)
# observer.start()
# while True:
#     try:
#         pass
#     except KeyboardInterrupt:
#         observer.stop()

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        # print (event)
        print("on_created", event.src_path)

    def on_deleted(self, event):
        print (event)

    def on_moved(self, event):
        print (event)

observer = Observer()
observer.schedule(Handler(), path='test_bot', recursive=True)
observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()