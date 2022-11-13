from sys import maxsize

minimum = maxsize

while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = int(command)
        if command < minimum:
            minimum = command

print(minimum)
