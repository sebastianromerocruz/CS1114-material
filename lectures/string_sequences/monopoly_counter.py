MIN_NUM_PLAYERS = 2
MAX_NUM_PLAYERS = 8
ROUNDING_FACTOR = 2

# STEP 1
number_of_players = int(input("Enter a valid number of players: "))

while number_of_players < MIN_NUM_PLAYERS or number_of_players > MAX_NUM_PLAYERS:
    number_of_players = int(input("Enter a valid number of players: "))

# We need starting values that any amount can surpass
winner = -1
winning_cash = -1

for player in range(1, number_of_players + 1):
    money = 0
    user_input = input("Enter the value of a property/asset, or DONE to finish: ")

    # STEP 2
    while user_input != "DONE":
        user_input = round(float(user_input), ROUNDING_FACTOR)
        money += user_input
        user_input = input("Enter the value of a property/asset, or DONE to finish: ")

    # STEP 4
    print("Player", player, "has", money, "dollars.")

    if money > winning_cash:
        # Replace the current winner and their cash amount if it is larger than the previous one
        winning_cash = money
        winner = player
        print("Player", player, "is in the lead!")

# STEP 5
print(winner, "wins with", winning_cash, "dollars!")
