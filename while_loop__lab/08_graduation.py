name = input()
grade_count = 0
grades_sum = 0
execution = 0

while True:
    grade_n = float(input())
    grade_count += 1
    grades_sum += grade_n
    if grade_n < 4:
        execution += 1
        if execution == 2:
            print(f"{name} has been excluded at {grade_count} grade")
            break
        else:
            grade_count -= 1
            grades_sum -= grade_n
    elif grade_count == 12:
        avg_grade = grades_sum / grade_count
        print(f"{name} graduated. Average grade: {avg_grade:.2f}")
        break
