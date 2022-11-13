hall_rent = int(input())

oscars = hall_rent * 0.70
catering = oscars * 0.85
sound = catering * 0.50

expenses = hall_rent + oscars + catering + sound
print(f"{expenses:.2f}")
