# student_record
file_name = 'students.txt'

def add_student():
    name = input('Enter name: ').title()
    with open(file_name, 'a') as file:
        file.write(f"{name}\n")
    return f'Added name - "{name}" to "{file_name}"'

def show_student():
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            if not content:
                return f'File - {file_name}, is empty!'
            return content
    except FileNotFoundError:
        return f'File - {file_name}, not found!'


def handle_option():
        choice = input('(1) - Add student\n(2) - View Student\n(3) - Exit\n: ')
        if choice == '1':
            return add_student()
        elif choice == '2':
            return show_student()
        elif choice == '3':
            return 'Operation done!'
        else:
            return f'Error!, option "{choice}" not recognised'

while True:
    output = handle_option()
    if output:
        print(output)

    if output == 'Operation done!':
        break
