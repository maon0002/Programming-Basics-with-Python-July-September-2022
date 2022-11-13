legacy = float(input())
year_to = int(input())

ivan_years = 18

expenses = 0

for y in range(1800, year_to + 1):
    if y == 1800:
        expenses += 12000
    elif y % 2 == 0:
        ivan_years += 1
        expenses += 12000
    else:
        ivan_years += 1
        expenses += (12000 + (50 * ivan_years))

diff = abs(expenses - legacy)

if expenses <= legacy:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
