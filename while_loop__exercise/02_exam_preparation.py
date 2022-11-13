limit = int(input())
command = ""
tasks_count = 0
failed_tasks_count = 0
last_task = ""
grade_sum = 0

while True:
    command = input()
    if command != "Enough":
        grade = int(input())
        tasks_count += 1  # needed?
        grade_sum += grade
        last_task = command
        if grade <= 4:
            failed_tasks_count += 1
            if failed_tasks_count == limit:
                print(f"You need a break, {failed_tasks_count} poor grades.")
                break
    else:
        avg = grade_sum / tasks_count
        print(f"Average score: {avg:.2f}")
        print(f"Number of problems: {tasks_count}")
        print(f"Last problem: {last_task}")
        break
