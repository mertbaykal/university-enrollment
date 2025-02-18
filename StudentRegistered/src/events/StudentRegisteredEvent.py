# src/events/StudentRegisteredEvent.py
from events.Event import Event

class StudentRegisteredEvent(Event):
    def __init__(self, student):
        super().__init__("StudentRegistered", {"student": student})
