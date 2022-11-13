import sys

pairs = int(input())

max_diff = -sys.maxsize
pairs_value = 0
previous_pairs_value = 0
pairs_total = 0
pairs_match = 1

for i in range(pairs):
    num_1 = int(input())
    num_2 = int(input())
    pairs_value = num_1 + num_2
    pairs_total += pairs_value
    if pairs == 1:
        break
    elif i == 0:
        previous_pairs_value = pairs_value
    else:
        if pairs_value == previous_pairs_value:
            pairs_match += 1

        elif pairs_value != previous_pairs_value:
            if abs(pairs_value - previous_pairs_value) > max_diff:
                max_diff = abs(pairs_value - previous_pairs_value)
                previous_pairs_value = pairs_value
            else:
                previous_pairs_value = pairs_value

if pairs_match == pairs or pairs == 1:
    print(f"Yes, value={pairs_value:.0f}")
else:
    print(f"No, maxdiff={max_diff}")
