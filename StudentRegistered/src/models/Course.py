# src/models/Course.py
class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []

    def enroll_student(self, student):
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student)
            return True
        return False
