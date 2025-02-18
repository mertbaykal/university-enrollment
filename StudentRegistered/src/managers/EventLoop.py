# src/managers/EventLoop.py
import queue

class EventLoop:
    def __init__(self):
        self.event_queue = queue.Queue()
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            if not self.event_queue.empty():
                event = self.event_queue.get()
                event["handler"](event["event"])
    
    def stop(self):
        self.running = False

    def emit(self, event, handler):
        self.event_queue.put({"event": event, "handler": handler})
