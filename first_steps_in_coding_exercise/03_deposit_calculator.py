deposit = float(input())
time = int(input())
percent_per_year = float(input())
percentage = percent_per_year / 100
deposit_calc = deposit + time * ((deposit * percentage) / 12)
print(deposit_calc)
