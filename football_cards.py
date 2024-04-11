cards = input().split()

team_a = 11
team_b = 11

for card in cards:
    card_args = card.split("-")
    team_name = card_args [0]
    player_number = card_args [1]
    if team == "A":
        team_a -= 1
    else:
        team_b -= 1
    if team_a < 7 or team_b < 7:
        print("Team A - {} ; Team B - {}".format(team_a, team_b))
        print("Game was terminated")
        break
else:
    print("Team A - {} ; Team B - {}".format(team_a, team_b))
