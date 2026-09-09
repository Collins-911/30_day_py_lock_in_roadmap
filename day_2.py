scores = [45, 78, 92, 34, 67, 88, 51]
def analyze_score(scores):
    highest_number = 0
    for n in scores:
        if n > highest_number:
            highest_number = n
    lowest_number = highest_number
    for s in scores:
        if s < lowest_number:
            lowest_number = s
    total = 0
    for t in scores:
        total+=t
    av = total / len(scores)
    pass_count = 0
    fail_count = 0
    for score in scores:
        if score >= 50:
            pass_count+=1
        else:
            fail_count+=1

    return highest_number, lowest_number, av, pass_count, fail_count


highest, lowest, average, passed, failed = analyze_score(scores)
# print(f"Highest: {highest} | Lowest: {lowest} | Average: {average} | Passed: {passed} | Failed: {failed}")


# def analyze_number():
#     try:
#         number = int(input('> '))
#     except ValueError:
#         return None
#     if number > 0:
#         return 'positive'
#     elif number < 0:
#         return 'negative'
#     else:
#         return 'zero'
#
# result = analyze_number()
# if result is None:
#     print('Cannot compute!')
# else:
#     print(result)

def calculate(a,b,operation):
    try:
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiplication':
            return a * b
        elif operation == 'division':
            return a / b
        else:
            return 'Operation not recognised'

    except ValueError:
        return None
    except ZeroDivisionError:
        return None

# cal = calculate(1,2,'add')
# print(cal)

def grade_student(name, score):
    try:
        score = float(score)

        if score < 0 or score > 100:
            grade = None
        elif score >= 70:
            grade = 'A'
        elif score >= 60:
            grade = 'B'
        elif score >= 50:
            grade = 'C'
        elif score >= 45:
            grade = 'D'
        elif score >= 40:
            grade = 'E'
        else:
            grade = 'F'

        return name, grade

    except ValueError:
        return None


result = grade_student(name='Collins', score=-1)

if result is None:
    print('Invalid score')
else:
    student_name, student_grade = result
    print(f"Name: {student_name} | Grade: {student_grade}")