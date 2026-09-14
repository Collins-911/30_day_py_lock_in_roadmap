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

def add_student(students):
    while True:
        name = input('Enter name: ').title().strip()
        if not name:
            print('Please type in name!')
            continue
        if len(name) < 3:
            print(f'Name - {name}, must be at least 3 characters!')
            continue
        if name.isdigit():
            print('Name cannot be a number!')
            continue
        if name in students:
            print(f'Name - {name}, already exists!')
            continue
        break
    while True:
        try:
            age = int(input('Enter age: '))
            if age <= 0:
                print('Must be a positive integer!')
                continue
            break
        except ValueError:
            print('Must be an integer!')
    while True:
        course = input('Enter course: ').title().strip()
        if not course:
            print('Please type in course!')
            continue
        break

    students[name] = {
        'age': age,
        'course': course
    }
    print(f'{name} added successfully!')

students = load_students()

while True:
    add_student(students)
    save_students(students)
    again = input('Add another student? (y/n): ').lower().strip()
    if again != 'y':
        break
print('Database saved successfully!')