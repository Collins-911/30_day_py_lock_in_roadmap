with open('student.txt', 'w') as file:
    file.write('Name: Collins \nCourse: Computer Science \nDay: 6')
with open('student.txt', 'r') as file:
    content = file.read()
print(content)
with open('student.txt', 'a') as file:
    file.write('\nLearning Python every day.')