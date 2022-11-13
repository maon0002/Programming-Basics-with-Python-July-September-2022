vacation_days = int(input())
# vacation_days = 113

play_norm = 30000
work_days = 365 - vacation_days
vacation_play = vacation_days * 127
work_play = work_days * 63

total_play = vacation_play + work_play

play_norm_is = 0

hours = 0
minutes = 0

if play_norm >= total_play:
    play_norm_is = play_norm - total_play
    hours = play_norm_is // 60
    minutes = play_norm_is % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    play_norm_is = total_play - play_norm
    hours = play_norm_is // 60
    minutes = play_norm_is % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
