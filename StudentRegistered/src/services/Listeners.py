# src/services/Listeners.py
def student_registered_listener(data):
    student = data["student"]
    print(f"📢 Student Registered: {student.name} (ID: {student.student_id})")

def course_enrollment_listener(data):
    student = data["student"]
    course = data["course"]
    print(f"✅ {student.name} has enrolled in {course.name}.")
