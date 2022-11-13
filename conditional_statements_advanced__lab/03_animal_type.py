animal_class = input()
class_is = ""
if animal_class == "dog":
    class_is = "mammal"
elif animal_class == "crocodile" \
        or animal_class == "tortoise" \
        or animal_class == "snake":
    class_is = "reptile"
else:
    class_is = "unknown"

print(class_is)
