digit = int(input())
check = ""
if digit == 0:
    check = "No"
elif -100 <= digit <= 100:
    check = "Yes"
else:
    check = "No"
print(check)
