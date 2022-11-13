from sys import maxsize

max_number = -maxsize

while True:
    number = input()
    if number == "Stop":
        break
    else:
        number = int(number)
        if number > max_number:
            max_number = number
print(max_number)
