def greet(name):
    return f"Hello {name}!"
print(greet('Ben'))

def calculate(a,b):
    try:
        return float(a) + float(b)
    except ValueError:
        return None

r = calculate(2,'4')
if r is None:
    print('Cannot compute!')
else:
    print(f"Sum: {r}")

def safe_divide(a,b):
    try:
        return float(a) / float(b)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

s = safe_divide(10,'1.3')
if s is None:
    print('Cannot compute!')
else:
    print(f"Division: {s}")

students = []
while True:
    name = input('Enter name type (done) to stop: ').title()
    if name == 'Done':
        break
    try:
        score = int(input('Enter score: '))
    except ValueError:
        continue

    student = {
        "name" : name,
        "score" : score
    }
    students.append(student)

def student_result(students):
    for x in students:
        if x['score'] >= 70:
            x['grade'] = 'A'
        elif x ['score'] >= 60:
            x['grade'] ='B'
        elif x['score'] >= 59:
            x['grade'] = 'C'
        elif x['score'] >= 49:
            x['grade'] = 'D'
        else:
            x['grade'] = 'F'

        print(f"{x['name']} scored {x['score']} - Grade: {x['grade']}")

print(student_result(students))








