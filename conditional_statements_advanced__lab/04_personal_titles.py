age = float(input())
sex = input()
address_as = ""

if sex == "m":
    if age < 16:
        address_as = "Master"
    else:
        address_as = "Mr."
elif sex == "f":
    if age < 16:
        address_as = "Miss"
    else:
        address_as = "Ms."
print(address_as)
