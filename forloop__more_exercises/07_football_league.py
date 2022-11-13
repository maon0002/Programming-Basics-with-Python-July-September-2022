capacity = int(input())
fans_count = int(input())

a_count = 0
b_count = 0
v_count = 0
g_count = 0

for x in range(fans_count):
    sector = input()
    if sector == "A":
        a_count += 1
    elif sector == "B":
        b_count += 1
    elif sector == "V":
        v_count += 1
    elif sector == "G":
        g_count += 1

total_count = a_count + b_count + v_count + g_count
percentage = total_count / capacity * 100

print(f"{a_count / total_count * 100:.2f}%")
print(f"{b_count / total_count * 100:.2f}%")
print(f"{v_count / total_count * 100:.2f}%")
print(f"{g_count / total_count * 100:.2f}%")
print(f"{percentage:.2f}%")
