# # person = {
# #     "name" : "Collins",
# #     "age" : 17,
# #     "score" : 100,
# #     "course" : "Computer Science"
# # }
# #
# # print(person['name'])
# # print(person['score'])
# # person['score'] = 49
# # if person['score'] >= 50:
# #     person['status'] = 'Pass'
# # else:
# #     person['status'] = 'Fail'
# # for key, value in person.items():
# #     print(f"{key} : {value}")
# #
#
# student_1 = {
#     "name" : "Collins",
#     "score" : 30
# }
# student_2 = {
#     "name" : "Gracious",
#     "score" : 80
# }
# student_3 = {
#     "name" : "James",
#     "score" : 55
# }
#
# students = [student_1,student_2,student_3]
# for student in students:
#     if student['score'] >= 50:
#         student['status'] = 'Pass'
#     else:
#         student['status'] = 'Fail'
#
#     print(f"{student['name']} : {student['score']} - {student['status']}")
from fontTools.misc.cython import returns

students = []
while True:
    name = input('Enter name, type "done" to stop: ').title()
    if name == "Done":
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
print(students)
