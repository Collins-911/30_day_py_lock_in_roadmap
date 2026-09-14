students = {}

def add_student():
    name = input('Enter name: ')
    if name in students:
        return f'Name - {name} already exists!'
    try:
        score = int(input('Enter score'))
    except ValueError:
        return 'Must be an integer'

    students[name] = {
        "score" : score
    }
    return None

def grade_student(name,score):
    name = students[name]
    score = students[score]

    for key, values in students.items():
        if 70 <= values['score'] <= 100:
            students['grade'] = 'A'
        elif 60 <= values['score'] <= 69:
           students['grade'] = 'B'
        elif 50 <= values['score'] <= 59:
            students['grade'] = 'C'
        elif 45 <= values['score'] <= 49:
            students['grade'] = 'D'
        elif 40 <= values['score'] <= 69:
            students['grade'] = 'E'
        else:
            students['grade'] = 'F'
    return f'Student - {students[name]}, {students[score]} - {students['grade']}'

print(grade_student())

