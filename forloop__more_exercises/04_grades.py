students_count = int(input())
grades_2 = 0
grades_3 = 0
grades_4 = 0
grades_5 = 0
grades_total = 0

for x in range(students_count):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        grades_2 += 1
        grades_total += grade
    elif 3.00 <= grade <= 3.99:
        grades_3 += 1
        grades_total += grade
    elif 4.00 <= grade <= 4.99:
        grades_4 += 1
        grades_total += grade
    elif grade >= 5:
        grades_5 += 1
        grades_total += grade

total_grades_count = grades_2 + grades_3 + grades_4 + grades_5
avg_grade = grades_total / total_grades_count

print(f"Top students: {grades_5 / total_grades_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {grades_4 / total_grades_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {grades_3 / total_grades_count * 100:.2f}%")
print(f"Fail: {grades_2 / total_grades_count * 100:.2f}%")
print(f"Average: {avg_grade:.2f}")
