change = float(input())
cents = round(change * 100)

coins_counter = 0

while cents > 0:
    if cents >= 200:
        cents -= 200
        coins_counter += 1
    elif cents >= 100:
        cents -= 100
        coins_counter += 1
    elif cents >= 50:
        cents -= 50
        coins_counter += 1
    elif cents >= 20:
        cents -= 20
        coins_counter += 1
    elif cents >= 10:
        cents -= 10
        coins_counter += 1
    elif cents >= 5:
        cents -= 5
        coins_counter += 1
    elif cents >= 2:
        cents -= 2
        coins_counter += 1
    elif cents >= 1:
        cents -= 1
        coins_counter += 1

print(coins_counter)
