text = input()

a = 1
e = 2
i = 3
o = 4
u = 5
sum_char = 0

for char in text:
    if char == "a":
        sum_char += a
    if char == "e":
        sum_char += e
    if char == "i":
        sum_char += i
    if char == "o":
        sum_char += o
    if char == "u":
        sum_char += u
else:
    pass
print(sum_char)
