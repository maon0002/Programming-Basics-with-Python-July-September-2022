floors = int(input())
rooms = int(input())
prefix = ""

for x in range(floors, 0, -1):
    if x == floors:
        prefix = "L"
    elif x % 2 != 0:
        prefix = 'A'
    else:
        prefix = "O"
    for y in range(rooms):
        print(f"{prefix}{x}{y}", end=" ")
    print()
