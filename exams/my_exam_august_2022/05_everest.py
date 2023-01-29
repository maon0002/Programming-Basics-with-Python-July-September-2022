days = 1
height = 5364
top_reached = False
input_line = input()

while input_line != "END":
    choice = input_line

    if height >= 8848:
        top_reached = True
        break

    if choice == "Yes":
        days += 1
        plus_height = int(input())
        height += plus_height
    elif choice == "No":
        plus_height = int(input())
        height += plus_height
    else:
        break

    if days == 5:
        break
    if height >= 8848:
        top_reached = True
        break

    input_line = input()

if top_reached:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed!")
    print(f"{height}")