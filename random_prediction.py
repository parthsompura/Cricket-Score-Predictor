#Hello
#can't we try to make it as this by the help of python
import random
team1 = input("Enter the First team: ")
team2 = input("Enter the second team: ")

team_playing = input("Who is doing batting: ")
if team_playing.upper() == team1.upper() or team_playing.upper() == team2.upper():
    pass
else:
    print("You written the team that is not playing")
    quit()

is_match_started = input("Is Match Started[Y/N]: ")
is_match_started = is_match_started.upper()

while True:
    if is_match_started.upper() == 'Y' or is_match_started.upper() == 'N':
        break
    print("Wrong Input Please Try Again")
    is_match_started = input("Is Match Started[Y/N]: ")
    is_match_started = is_match_started.upper()

if is_match_started == 'Y':
    overs = int(
        input("Please tell how many overs completed(only over not balls): "))
    if overs >= 20:
        print("I think you late")
        quit()
    runs = int(input("Please tell how many run are(according to full over): "))
    wickets = int(input("Please tell how many wickets are taken: "))
    if wickets >= 10:
        print(f"10 wickets are over {team_playing} made {runs} runs")
        quit()
    if wickets < 0:
        print("What a joke")
        quit()
    rr = runs / overs
    print(f"Hmm.... Run rate at this time is {rr}")
    low_or_sum_rpo = [1, 0.5, 0.1, 0.8, 0.45, 0.68]
    neg_or_pos = random.randint(0, 1)
    rpo_changer = random.randint(0, len(low_or_sum_rpo))
    rpo_changer = low_or_sum_rpo[rpo_changer]
    if neg_or_pos == 0:
        rr - rpo_changer
    elif neg_or_pos == 1:
        rr + rpo_changer

    if overs <= 0:
        print("Please tell after 1 over")
    else:
        if wickets <= 3:
            if (overs < 9 and rr > 9) or (overs >= 9):
                predict = int(rr * 20)
                print(
                    f"I think they will make between {predict - 3} - {predict + 3}")
            else:
                print(f"{team_playing} are slow but may beat after some overs: ")
                sum_rpo = [1, 2, 0.5, 0.8, -0.1, -0.3]
                rpo_changer = random.randint(0, len(sum_rpo))
                rpo_changer = sum_rpo[rpo_changer]
                rr += rpo_changer
                predict = int(rr * 20)
                print(
                    f"I think they can make between {predict - 3} - {predict + 3}")
        elif wickets > 3 and wickets <= 7:
            to_minus = random.randint(9, 24)
            if (overs < 9 and rr > 9) or (overs >= 9):
                predict = int(rr * 20) - to_minus
                print(
                    f"I think they will make between {predict - 3} - {predict + 3}")
            else:
                print(f"{team_playing} are slow but may beat after some overs: ")
                sum_rpo = [1, 2, 0.5, 0.8, -0.1, -0.3]
                rpo_changer = random.randint(0, len(sum_rpo))
                rpo_changer = sum_rpo[rpo_changer]
                rr += rpo_changer
                predict = int(rr * 20) - to_minus
                print(
                    f"I think they can make between {predict - 3} - {predict + 3}")
        elif wickets > 7:
            to_minus = random.randint(18, 40)
            if (overs < 9 and rr > 9) or (overs >= 9):
                predict = int(rr * 20) - to_minus
                print(
                    f"I think they will make between {predict - 3} - {predict + 3}")
            else:
                print(f"{team_playing} are slow but may beat after some overs: ")
                sum_rpo = [1, 2, 0.5, 0.8, -0.1, -0.3]
                rpo_changer = random.randint(0, len(sum_rpo))
                rpo_changer = sum_rpo[rpo_changer]
                rr += rpo_changer
                predict = int(rr * 20) - to_minus
                print(
                    f"I think they can make between {predict - 3} - {predict + 3}")
elif is_match_started == 'N':
    print("Please come after started match")
