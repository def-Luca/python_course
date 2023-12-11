import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input(" how many players will play 2 - 4 ? ")
    if players.isdigit():
        players = int(players)
        if  2<= players <=4:
            print("welcome!")
            break
        else:
            print("invalid player number")
    else:
        print("please introduce a number")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nplayer's number {player_idx +1} turn\n")
        print(f" Scores {player_scores}")
        current_score = 0

        while True:
            should_roll = input("would you like to roll the dice? (y) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You hit a one. Turn over")
                current_score = 0
            else:
                current_score += value
                print(f"you hit a {value} ")

            print("Your score is", current_score)


        player_scores[player_idx] += current_score
        print(f"your total score is {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"player number {winning_idx+1} won with a total score of {max_score}")