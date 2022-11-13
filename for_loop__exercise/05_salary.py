tabs = int(input())
salary = int(input())

concentration_tax = 0

for www in range(tabs):
    http = input()
    if http == "Facebook":
        concentration_tax += 150
    elif http == "Instagram":
        concentration_tax += 100
    elif http == "Reddit":
        concentration_tax += 50
    if salary <= concentration_tax:
        print("You have lost your salary.")
        break
diff = (salary - concentration_tax)

if salary > concentration_tax:
    print(f"{diff:.0f}")
