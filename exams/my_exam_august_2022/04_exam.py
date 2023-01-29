students_number = int(input())
top_students = 0
fours_group = 0
threes_group = 0
fail_group = 0
sum_grades = 0

for current_student in range(students_number):
    grade = float(input())
    sum_grades += grade
    if grade > 4.99:
        top_students += 1
    elif grade > 3.99:
        fours_group += 1
    elif grade >= 3:
        threes_group += 1
    elif grade < 3:
        fail_group += 1

percentage_top = top_students / students_number * 100
percentage_fours = fours_group / students_number * 100
percentage_threes = threes_group / students_number * 100
percentage_fail = fail_group / students_number * 100

avg_grade = sum_grades / students_number

print(f"Top students: {percentage_top:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_fours:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_threes:.2f}%")
print(f"Fail: {percentage_fail:.2f}%")
print(f"Average: {avg_grade:.2f}")
