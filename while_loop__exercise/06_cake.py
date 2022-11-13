x = int(input())
y = int(input())
z = x * y
eaten_parts = 0
next_parts_eaten = ""

while z > eaten_parts:  # and next_parts_eaten == "STOP":
    next_parts_eaten = input()
    if next_parts_eaten != "STOP":
        eaten_parts += int(next_parts_eaten)
    else:
        break

diff = abs(z - eaten_parts)
if z >= eaten_parts and next_parts_eaten == "STOP":
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
