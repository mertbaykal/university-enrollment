# src/main.py
from managers.EventLoop import EventLoop
from events.StudentRegisteredEvent import StudentRegisteredEvent
from events.CourseEnrollmentEvent import CourseEnrollmentEvent
from models.Student import Student
from models.Course import Course
from services.Listeners import student_registered_listener, course_enrollment_listener

event_loop = EventLoop()

student1 = Student(1, "Ali Yılmaz")
course1 = Course(101, "Python Programming", 30)

#event loop
event_loop.emit(StudentRegisteredEvent(student1), student_registered_listener)
event_loop.emit(CourseEnrollmentEvent(student1, course1), course_enrollment_listener)

print("🎯 Event Loop Started...")
event_loop.start()
