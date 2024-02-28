import random
import json
import matplotlib.pyplot as plt
import requests


class Rock:
    def __init__(self):
        self.lose = [Paper, Spock]


class Paper:
    def __init__(self):
        self.lose = [Scissors, Lizard]


class Scissors:
    def __init__(self):
        self.lose = [Rock, Spock]


class Lizard:
    def __init__(self):
        self.lose = [Rock, Scissors]


class Spock:
    def __init__(self):
        self.lose = [Paper, Lizard]


def determine_winner(player, opponent):
    if type(player) in opponent.lose:
        return f"\nPlayer wins with {type(player).__name__}!", 1
    elif type(opponent) in player.lose:
        return f"\nComputer wins with {type(opponent).__name__}!", 2
    else:
        return "\nDraw!", 0


def update_win_counter(winner, winner_statistics):
    if winner == 1:
        winner_statistics["Player"] += 1
    elif winner == 2:
        winner_statistics["Computer"] += 1
    else:
        winner_statistics["Draw"] += 1


def update_statistics(choice, statistics):
    choice_name = type(choice).__name__
    if choice_name not in statistics:
        statistics[choice_name] = 1
    else:
        statistics[choice_name] += 1


def save_statistics(statistics, name):
    link = name + ".json"
    with open(link, "w") as file:
        json.dump(statistics, file)


def load_statistics(name):
    link = name + ".json"
    try:
        with open(link, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def show_statistics(statistics):
    options = list(statistics.keys())
    counter = list(statistics.values())

    plt.bar(options, counter)
    plt.show()


def play_game():
    choices = [Rock(), Paper(), Scissors(), Lizard(), Spock()]

    print("1. Rock  2. Paper  3. Scissors  4. Lizard  5. Spock")
    player_choice = choices[int(input("Enter a number to choose: ")) - 1]
    computer_choice = choices[random.randint(0, 4)]

    print(f"Player chose {type(player_choice).__name__}")
    print(f"Computer chose {type(computer_choice).__name__}")

    result = determine_winner(player_choice, computer_choice)
    print(result[0])

    return player_choice, result[1]


def menu(name_winners, name_statistics):
    winner_statistics = load_statistics(name_winners)
    option_statistics = load_statistics(name_statistics)

    while True:
        print("1. Play Game  2. View Statistics  3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            game = play_game()
            player_choice = game[0]
            winner = game[1]
            update_statistics(player_choice, option_statistics)
            update_win_counter(winner, winner_statistics)
        elif choice == '2':
            show_statistics(option_statistics)
            show_statistics(winner_statistics)
        elif choice == '3':
            save_statistics(option_statistics, "statistics")
            res = requests.post("http://localhost:5000/upload_statistics", json=option_statistics)
            save_statistics(winner_statistics, "winners")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    name_winners = "winners"
    name_statistics = "statistics"
    menu(name_winners, name_statistics)
