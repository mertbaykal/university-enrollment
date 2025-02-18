
# University Enrollment System

This project implements an event-driven system for university and course enrollment using Python. No external dependencies are required.

## Project Structure

```
📂 university-enrollment-system/
├── 📂 src/
│   ├── 📂 events/
│   ├── 📂 managers/
│   ├── 📂 models/
│   ├── 📂 services/
│   ├── main.py
└── README.md
```

## Getting Started

### 1️⃣ Create Directories and Files

Ensure the directory structure is correct. If not, run:

```sh
mkdir -p src/events src/managers src/models src/services
touch src/events/Event.py src/events/StudentRegisteredEvent.py src/events/CourseEnrollmentEvent.py
touch src/managers/EventLoop.py src/managers/EventManager.py
touch src/models/Student.py src/models/Course.py
touch src/services/Listeners.py src/main.py README.md
```

### 2️⃣ Install Python

Make sure Python is installed by running:

```sh
python --version
```

### 3️⃣ Run the Project

Navigate to the project directory:

```sh
cd university-enrollment-system/src
```

Run the main program:

```sh
python main.py
```

Expected Output:

```
🎯 Event Loop Started...
📢 Student Registered: Ali Yılmaz (ID: 1)
✅ Ali Yılmaz has enrolled in Python Programming.
```

