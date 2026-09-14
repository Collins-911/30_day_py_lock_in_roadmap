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
        json.dump(students,file,indent=4)

def add_student(students):

    #Name
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
            print(f'Age - {age}, must be a number!')
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
            print(f'Level - {level}, must be a number!')
        if level not  in [100,200,300,400,500,600]:
            print(f'Invalid level - {level}')
            continue

        break

    while True:
        try:
            score = int(input('Enter score: ').strip())
        except ValueError:
            print(f'Score - {score}, must be a number!')
            continue
        if score < 0 or score > 100:
            print(f'Score - {score}, must be between 0 and 100!')
            continue
        break

    #Add student
    students[name] = {
        "age" : age,
        "level" : level,
        "score" : score
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
        print(f'Deleted name - {student_name}')
        
def view_student(students):
 if not students:
     print('No students found!')
     return 
 
 for name, details in students.items():
     print(f'Name - {name}, Age - {details["age"]}, Level - {details["level"]}, Score - {details["score"]}')

def handle_choice(students):
    while True:
        choice = input('1 - Add student\n2 - Search student\n3 - Delete student\n4 - View all students\n5 - Exit\nChoose an option: ')
        if choice == '1':
            add_student(students)
        elif choice == '2':
            result = search_student(students)

            if result:
                search, student = result

                if student:
                    print(f"Age: {student['age']}")
                    print(f"Level: {student['level']}")
                    print(f"Score: {student['score']}")
                else:
                    print(f"Student - {search}, not found!")
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            view_student(students)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print(f'Invalid option - {choice}')

students = load_students()
handle_choice(students)






