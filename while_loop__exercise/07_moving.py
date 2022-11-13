w = int(input())
h = int(input())
l = int(input())

m3 = w * h * l
total_boxes_count = 0

more_boxes = ""

while m3 >= total_boxes_count:
    more_boxes = input()
    if more_boxes == "Done":
        break
    else:
        total_boxes_count += int(more_boxes)

diff = abs(m3 - total_boxes_count)

if more_boxes == "Done":  # or m3 > total_boxes_count:
    if total_boxes_count <= m3:
        print(f"{diff} Cubic meters left.")
    else:
        print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")
