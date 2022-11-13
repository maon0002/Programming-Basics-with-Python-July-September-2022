actor_name = input()
academy_points = float(input())
pers_in_the_jury = int(input())

extra_points = 0
total_points = 0

for persons in range(pers_in_the_jury):
    next_jury = input()
    next_points = float(input())
    extra_points += (len(next_jury) * next_points) / 2
    if extra_points + academy_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {extra_points + academy_points:.1f}!")
        break

diff = abs((extra_points + academy_points) - 1250.5)

if extra_points + academy_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
