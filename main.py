import random
import time

def fight(player_name, player_health, opponent_name, opponent_health):
    print(player_name + " has " + str(player_health) + " total health")
    print(opponent_name + " has " + str(opponent_health) + " total health")
    print(" ")

    moves = [
        {"name": "Throw apple", "damage": 30, "success_chance": 0.9},
        {"name": "Left hook", "damage": 100, "success_chance": 0.1},
        {"name": "Right hook", "damage": 150, "success_chance": 0.05},
        {"name": "Flamethrower", "damage": 40, "success_chance": 0.5}
    ]

    while player_health > 0 and opponent_health > 0:
        print_moves(moves)
        print(" ")

        # Player's move
        player_move = input("Enter your move: ")
        player_damage, player_success_chance, move_description = get_move_details(player_move, moves)

        print("You chose: " + move_description)
        time.sleep(1)  # Introduce a delay
        print(" ")

        # Determine if the player's move is successful
        if random.random() < player_success_chance:
            print(player_name + " successfully executed the move!")
            time.sleep(1)  # Introduce a delay
            print(player_name + " dealt " + str(player_damage) + " damage to " + opponent_name + ".")
            opponent_health -= player_damage
        else:
            print(player_name + "'s move missed!")

        print(" ")
        time.sleep(1)  # Introduce a delay

        # Check if opponent is still alive
        if opponent_health <= 0:
            print("You defeated " + opponent_name + "!")
            break

        # Opponent's move
        opponent_move = str(random.randint(1, len(moves)))
        opponent_damage, opponent_success_chance, move_description = get_move_details(opponent_move, moves)

        print(opponent_name + " chose: " + move_description)
        time.sleep(1)  # Introduce a delay
        print(" ")

        # Determine if the opponent's move is successful
        if random.random() < opponent_success_chance:
            print(opponent_name + " successfully executed the move!")
            time.sleep(1)  # Introduce a delay
            print(opponent_name + " dealt " + str(opponent_damage) + " damage to " + player_name + ".")
            player_health -= opponent_damage
        else:
            print(opponent_name + "'s move missed!")

        print(" ")
        time.sleep(1)  # Introduce a delay

        # Check if player is still alive
        if player_health <= 0:
            print("You were defeated by " + opponent_name + "!")
            break

        print("After the moves:")
        print(player_name + " has " + str(player_health) + " total health")
        print(opponent_name + " has " + str(opponent_health) + " total health")
        print(" ")
        time.sleep(1)  # Introduce a delay

    return player_health

def print_moves(moves):
    for index, move in enumerate(moves, start=1):
        print(f"{index}. {move['name']} (Deals {move['damage']} damage, {int(move['success_chance'] * 100)}% chance of hitting)")

def get_move_details(move_index, moves):
    try:
        move_index = int(move_index)
        if 1 <= move_index <= len(moves):
            move = moves[move_index - 1]
            return move["damage"], move["success_chance"], move["name"]
    except ValueError:
        pass

    print("Invalid move. No damage dealt.")
    return 0, 0, "Invalid move"

def play_game():
    player_health = 115
    opponent_health_katie = 150
    opponent_health_ella = 100
    player_name = "Emma Zhu"

    print("Came across two paths, one leads to a cave and the other leads to a mine")

    while True:
        print("Which path do you choose?")
        print("1. Cave")
        print("2. Mine")

        choice = input("Enter your choice: ")

        if "1" == choice:
            print(" ")
            print("You walk into the cave and find a treasure chest")
            print("You open the chest and out pops Katie Kudela")
            print("Now you have to fight Katie with Emma Zhu, your pokemon!!")
            player_health = fight(player_name, player_health, "Katie Kudela", opponent_health_katie)

            if player_health > 0:
                print("You win!")
            else:
                print("You lost the fight against Katie. Better luck next time.")

        elif "2" == choice:
            print(" ")
            print("You walk into the mine and find an abandoned car")
            print("You open the car, and out pops Ella Roberson")
            print("Now you have to fight Ella Roberson with Emma Zhu, your pokemon!!")
            player_health = fight(player_name, player_health, "Ella Roberson", opponent_health_ella)

            if player_health > 0:
                print("You win!")
            else:
                print("You lost the fight against Ella. Better luck next time.")

        print(" ")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
