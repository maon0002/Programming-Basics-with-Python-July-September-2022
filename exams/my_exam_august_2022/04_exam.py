# Задача 4. Изпит
# Напишете програма, която да пресмята статистика за оценки от изпит.
# В началото програмата получава броя на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да отпечата процента студенти с оценка
# между 2.00 и 2.99,
# между 3.00 и 3.99,
# между 4.00 и 4.99, 5.00 или повече.
# Също така и средния успех на изпита.
# Вход:
# От конзолата се четат:
#     • На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
#     • За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход:
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
#     Ред 1 - "Top students: {процент студенти с успех 5.00 или повече}%"
#     Ред 2 - "Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
#     Ред 3 - "Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
#     Ред 4 - "Fail: {по-малко от 3.00}%"
#     Ред 5 - "Average: {среден успех}"
# Всички числа трябва да са форматирани до втория знак след десетичната запетая.

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
