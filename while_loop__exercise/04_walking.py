steps_per_day = 0
steps_goal = 10000
is_tired = False
last_input = ""

while steps_per_day < steps_goal:
    current_steps = input()
    if current_steps == "Going home":
        is_tired = True
        continue
    elif int(float(current_steps)) > 0:
        steps_per_day += int(float(current_steps))
        if is_tired:
            break

diff = abs(steps_goal - steps_per_day)
if is_tired:
    if steps_per_day < steps_goal:
        print(f"{diff} more steps to reach goal.")
    else:
        print(f"Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
else:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
