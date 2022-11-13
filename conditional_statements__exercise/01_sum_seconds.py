player_one = int(input())
player_two = int(input())
player_three = int(input())

players_total = player_three + player_two + player_one
total_minutes = players_total // 60
total_seconds = players_total % 60

time = f'{total_minutes}:{total_seconds}'

if len(str(total_minutes)) == 1 and len(str(total_seconds)) == 2:
    print(time)
else:
    print(f'{total_minutes}:0{total_seconds}')
