rows = int(input())

for i in range(rows):
    for j in range(rows):
        if \
                (i == 0 and j == 0) or \
                        (i == rows - 1 and j == rows - 1) or \
                        (j == rows - 1 and i == 0) or \
                        (j == 0 and i == rows - 1):
            print("+ ", end='')
        elif \
                (j == 0 and (i != 0 or i != rows)) or \
                        (j == rows - 1 and (i != 0 or i != rows)):
            print("| ", end="")
        else:
            print("- ", end='')
    print()
