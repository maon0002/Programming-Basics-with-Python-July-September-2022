people_in_jury = int(input())
presentation_name = input()

grade_counter = 0
presentation_counter = 0
presentation_grade_counter = 0

sum_grades = 0
sum_presentation_grades = 0

while presentation_name != "Finish":
    presentation_counter += 1
    while presentation_grade_counter <= people_in_jury:  # int(grade) > 0
        grade_counter += 1
        presentation_grade_counter += 1
        grade = float(input())
        sum_grades += grade
        sum_presentation_grades += grade
        if presentation_grade_counter == people_in_jury:
            avg_presentation_grade = sum_presentation_grades / presentation_grade_counter
            print(f"{presentation_name} - {avg_presentation_grade:.2f}.")
            sum_presentation_grades = 0
            presentation_grade_counter = 0

            break
    presentation_name = input()
avg_total = sum_grades / grade_counter
print(f"Student's final assessment is {avg_total:.2f}.")
