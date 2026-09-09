students = {}

def add_students():
    student_name = input('Enter student name: ').title()
    if student_name in students:
        print(f"Student name - {student_name} already exist!")
    try:
        student_age = int(input('Enter student age: '))
        if student_age > 35:
            return f"Student is too old!"
        elif student_age < 16:
            return "Student is too young!"
        student_level = int(input('Enter student level: '))
        if student_level not in [100, 200, 300, 400, 500, 600]:
            return "Level doesn't exists!"
    except ValueError:
        return 'Age and Level must be integers'

    students[student_name] = {
        "age": student_age,
        "level": student_level
    }
    return None

def search_student():
    name = input('Enter student name, type (done) to stop: ').title()
    if name == "Done":
        return 'Done!'
    search = students.get(name, f"Name - {name} not found!")
    return search

count = 2
while True:
    if count == 0:
        break
    else:
        update = add_students()
        if update:
            print(update)
        count -= 1

search = search_student()
print(search)