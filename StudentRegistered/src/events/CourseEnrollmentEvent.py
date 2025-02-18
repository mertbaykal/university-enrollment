# src/events/CourseEnrollmentEvent.py
from events.Event import Event

class CourseEnrollmentEvent(Event):
    def __init__(self, student, course):
        super().__init__("CourseEnrollment", {"student": student, "course": course})
