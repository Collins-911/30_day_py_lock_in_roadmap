import json

def load_students():
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
            return students
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_students(students):
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)