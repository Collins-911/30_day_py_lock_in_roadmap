students = {
    "Collins": {
        "age": 17,
        "course": "Computer Science",
        "level": 200
    },
    "James": {
        "age": 16,
        "course": "Cyber Security",
        "level": 100
    },
    "Ada": {
        "age": 21,
        "course": "Software Engineering",
        "level": 300
    }
}

students['David'] = {
    "age" : 17,
    "course" : "Data Science",
    "level" : 400
}

while True:
    name = input('Enter student name, type (done) to stop: ').title()
    if name == "Done":
        break

    search = students.get(name,f"Cannot find name - {name}")
    print(search)