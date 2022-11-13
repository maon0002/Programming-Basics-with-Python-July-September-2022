moves = int(input())

result = 0
until_9 = 0
until_19 = 0
until_29 = 0
until_39 = 0
until_50 = 0
invalid = 0

for x in range(moves):
    luck = int(input())
    if luck < 0 or luck > 50:
        invalid += 1
        result /= 2
    elif 0 <= luck <= 9:
        result += (luck * 0.20)
        until_9 += 1
    elif 10 <= luck <= 19:
        result += (luck * 0.30)
        until_19 += 1
    elif 20 <= luck <= 29:
        result += (luck * 0.40)
        until_29 += 1
    elif 30 <= luck <= 39:
        result += 50
        until_39 += 1
    elif 40 <= luck <= 50:
        result += 100
        until_50 += 1

total_count = until_9 + until_19 + until_29 + until_39 + until_50 + invalid

print(f"{result:.2f}")
print(f"From 0 to 9: {until_9 / total_count * 100:.2f}%")
print(f"From 10 to 19: {until_19 / total_count * 100:.2f}%")
print(f"From 20 to 29: {until_29 / total_count * 100:.2f}%")
print(f"From 30 to 39: {until_39 / total_count * 100:.2f}%")
print(f"From 40 to 50: {until_50 / total_count * 100:.2f}%")
print(f"Invalid numbers: {invalid / total_count * 100:.2f}%")
