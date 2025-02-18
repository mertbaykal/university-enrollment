# src/managers/EventManager.py
class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, listener):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def emit(self, event):
        if event.name in self.listeners:
            for listener in self.listeners[event.name]:
                listener(event.data)
