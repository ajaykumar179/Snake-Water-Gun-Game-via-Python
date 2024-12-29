import random
game_data = {
    "win_matrix": [
        ['D', 'W', 'L'],
        ['L', 'D', 'W'],
        ['W', 'L', 'D']
    ],
    "choice_list": ["Snake", "Water", "Gun"],
    "labels": {"Snake": 0, "Water": 1, "Gun": 2}
}

player_1 = input("Player1 Select your option from (Snake, Water, Gun)? ")
player_2 = random.choice(game_data["choice_list"])
print(f"System selected: {player_2}")

#Result
result = game_data["win_matrix"][game_data["labels"][player_1]][game_data["labels"][player_2]]
#conditional statements for printing the result
if result == 'W':
    print("you won")
elif result == 'L':
    print("you lose")
else:
    print("you draw")


