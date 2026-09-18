from database import save_students
def add_student(students):

    # Name
    while True:
        name = input('Enter name: ').title().strip()
        if not name:
            print('Please enter name!')
            continue
        if len(name) < 3:
            print(f'Name - {name}, must be more that 3 char!')
            continue
        if name.isdigit():
            print(f'Name - {name}, must be a word')
            continue
        if name in students:
            print(f'Name - {name}, already exists!')
            continue
        break

    # Age
    while True:
        try:
            age = int(input('Enter age: ').strip())
        except ValueError:
            print(f'Age must be a number!')
            continue
        if age <= 0:
            print(f'Age - {age}, must be positive!')
            continue
        break

    # Level
    while True:
        try:
            level = int(input('Enter level: ').strip())
        except ValueError:
            print('Level must be a number!')
            continue

        if level not in [100, 200, 300, 400, 500, 600]:
            print(f'Invalid level - {level}')
            continue
        break

    # Score
    while True:
        try:
            score = int(input('Enter score: ').strip())
        except ValueError:
            print(f'Score must be a number!')
            continue
        if score < 0 or score > 100:
            print(f'Score - {score}, must be between 0 and 100!')
            continue
        break

    # Add student
    students[name] = {
        "age": age,
        "level": level,
        "score": score
    }
    save_students(students)
    print(f'Student - {name}, added successfully!')


def search_student(students):
    if not students:
        print("No students to search!")
        return None

    search = input('Enter student name you want to search: ').title().strip()

    if search in students:
        return search, students[search]
    else:
        return search, None


def delete_student(students):
    if not students:
        print('No students to delete!')
        return

    student_name = input('Enter student name to delete: ').title().strip()
    if student_name in students:
        del students[student_name]
        save_students(students)
        print(f'Deleted name - {student_name}')
    else:
        print(f'Student - {student_name}, not found!')


def view_students(students):
    if not students:
        print('No students found!')
        return

    for name, details in students.items():
        print(f'Name - {name}\nAge - {details["age"]}\nLevel - {details["level"]}\nScore - {details["score"]}\n----------')


def update_student(students):
    student_name = input('Enter student name: ').title()
    if student_name in students:
        option = input('1 - Age\n2 - Level\n3 - Score\n4 - Cancel\nChoose: ')

        # Age
        if option == '1':
            while True:
                try:
                    new_age = int(input('Enter new age: ').strip())
                except ValueError:
                    print('Age must be a number!')
                    continue
                if new_age <= 0:
                    print(f'Age - {new_age} must be positive')
                    continue
                students[student_name]['age'] = new_age
                save_students(students)
                print('Student age has been updated successfully!')
                break
        # Level
        elif option == '2':
            while True:
                try:
                    new_level = int(input('Enter new level: ').strip())
                except ValueError:
                    print('Level must be a number!')
                    continue
                if new_level not in [100, 200, 300, 400, 500, 600]:
                    print(f'Level - {new_level}, is invalid!')
                    continue
                students[student_name]['level'] = new_level
                save_students(students)
                print('Student level has been updated successfully!')
                break
        # Score
        elif option == '3':
            while True:
                try:
                    new_score = int(input('Enter new score: ').strip())
                except ValueError:
                    print('Score must be a number!')
                    continue

                if new_score < 0 or new_score > 100:
                    print(f'Score - {new_score}, must be between 0 and 100!')
                    continue
                students[student_name]['score'] = new_score
                save_students(students)
                print('Student score has been updated successfully!')
                break
        elif option == '4':
            print('Update cancelled!')
    else:
        print(f'Name - {student_name}, is not in data base')
