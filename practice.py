import random



def player_details(player_num):
    name = input(f"Enter the name of Player {player_num}: ")
    return name

def choices(player_name):
    choices = {}
    for choice in ["stone", "paper", "scissors"]:
        my_choice = input(f"{player_name}, enter your choice for '{choice}': ").lower()
        if len(my_choice) == 1 or my_choice in ["stone", "paper", "scissors"]:
            choices[my_choice] = choice
        else:
            print("Please enter your choice correctly")
            return choices(player_name)
    return choices

def evaluate_choices(player1_choice, player2_choice, player1_name, player2_name):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'scissors' and player2_choice == 'paper') or \
         (player1_choice == 'paper' and player2_choice == 'stone') or \
         (player1_choice == 'stone' and player2_choice == 'scissors'):
        return f"{player1_name} has won this round!"
    else:
        return f"{player2_name} has won this round!"





def main():
    player1_name = player_details(1)
    player2_name = player_details(2)

    player1_choices = choices(player1_name)
    player2_choices = choices(player2_name)

    p1_wins = 0
    p2_wins = 0

    for round in range(1, 6):
        print(f"\nRound {round}:")

        player1_choice_key = input(f"{player1_name}, enter your choice: ").lower()
        player2_choice_key = input(f"{player2_name}, enter your choice: ").lower()
        
        player1_choice = player1_choices.get(player1_choice_key, None)
        player2_choice = player2_choices.get(player2_choice_key, None)
        
        if player1_choice is not None and player2_choice is not None:
            print(f"{player1_name}'s {player1_choices[player1_choice_key]} vs. {player2_name}'s {player2_choices[player2_choice_key]}")
            
            result = evaluate_choices(player1_choice, player2_choice, player1_name, player2_name)

            print(result)

            if result.startswith(player1_name):
                p1_wins += 1
            elif result.startswith(player2_name):
                p2_wins += 1
        else:
            print("Invalid choice. Please enter your choice")

    if p1_wins > p2_wins:
        print(f"\n{player1_name} won with {p1_wins} rounds")
    elif p2_wins > p1_wins:
        print(f"\n{player2_name} won with {p2_wins} rounds")
    else:
        print("\nIt's a tie")

if __name__ == "__main__":
    main()
