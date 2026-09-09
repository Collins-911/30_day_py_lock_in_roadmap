# Part 1
student_names = ['Collins','James','Cedar','Jesse','Ada']
print(f"{student_names[0]} | {student_names[2]} | {student_names[-1]}")

# Part 2
# Version 1
scores = [45, 67, 82, 39, 91, 55]
for score in scores:
    print(score)

# Version 2
scores = [45, 67, 82, 39, 91, 55]
for score in scores:
    print(f"Score: {score}")

# Part 3
for i in range(1,11):
    print(i)
for i in range(2,21,2):
    print(i)

scores = [45, 67, 82, 39, 91, 55, 73, 28]
pass_count = 0
for score in scores:
    if score >= 50:
        pass_count+=1
print(f"Number of students who passed: {pass_count}")

scores = [45, 67, 82, 39, 91, 55, 73, 28]
def calculate_average(scores):
    total = 0
    if scores:
        for s in scores:
            total += s
        avg = total / len(scores)
        return avg
    else:
        return None
print(calculate_average(scores))

scores = [45, 67, 82, 39, 91, 55, 73, 28]
def count_passed(scores):
    if not scores:
        return None

    count_pass = 0
    for score in scores:
        if score >= 50:
            count_pass+=1
    return count_pass

print(count_passed(scores))


names = ["John", "Mary", "David", "Sarah", "Mike"]
scores = [72, 45, 88, 39, 61]

for i in range(len(names)):
    name = names[i]
    score = scores[i]

    if score >= 50:
        status = 'Pass'
    else:
        status = 'Fail'
    print(f"{name}: {score} - {status}")
