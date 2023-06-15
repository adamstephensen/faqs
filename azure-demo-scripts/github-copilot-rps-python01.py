# Write a rock, paper, scissors game 
# import random module
import random

# define main function that handles all the logic
def main():
    # set the variable to keep track of wins, losses, and ties
    wins = 0
    losses = 0
    ties = 0

    # set the variable for the number of times to play
    times = int(input("How many times do you want to play? "))

    # create a for loop to play the game the number of times the user entered
    for i in range(times):
        # call the get_user_input function to get the user's input
        user_input = get_user_input()
        # call the get_computer_input function to get the computer's input
        computer_input = get_computer_input()
        # call the get_winner function to get the winner of the round
        winner = get_winner(user_input, computer_input)
        # call the display_results function to display the winner of the round
        display_results(user_input, computer_input, winner)
        # call the update_wins_losses_ties function to update the wins, losses, and ties
        wins, losses, ties = update_wins_losses_ties(winner, wins, losses, ties)
    
    # call the display_final_results function to display the final results
    display_final_results(wins, losses, ties)

# define the get_user_input function that gets the user's input
def get_user_input():
    # get the user's input
    user_input = input("Enter rock, paper, or scissors: ")
    # return the user's input
    return user_input

# define the get_computer_input function that gets the computer's input
def get_computer_input():
    # create a list of the possible choices
    choices = ["rock", "paper", "scissors"]
    # get the computer's input
    computer_input = random.choice(choices)
    # return the computer's input
    return computer_input

# define the get_winner function that gets the winner of the round
def get_winner(user_input, computer_input):
    # create a dictionary of the possible choices and the winner
    winner_dict = {
        "rock": {
            "rock": "tie",
            "paper": "computer",
            "scissors": "user"
        },
        "paper": {
            "rock": "user",
            "paper": "tie",
            "scissors": "computer"
        },
        "scissors": {
            "rock": "computer",
            "paper": "user",
            "scissors": "tie"
        }
    }
    # get the winner of the round
    winner = winner_dict[user_input][computer_input]
    # return the winner of the round
    return winner

# define the display_results function that displays the winner of the round
def display_results(user_input, computer_input, winner):
    # display the user's input, computer's input, and the winner of the round
    print(f"User: {user_input}, Computer: {computer_input}, Winner: {winner}")

# define the update_wins_losses_ties function that updates the wins, losses, and ties
def update_wins_losses_ties(winner, wins, losses, ties):
    # if the winner is the user, increment the wins
    if winner == "user":
        wins += 1
    # if the winner is the computer, increment the losses
    elif winner == "computer":
        losses += 1
    # if the winner is a tie, increment the ties
    else:
        ties += 1
    # return the wins, losses, and ties
    return wins, losses, ties

# define the display_final_results function that displays the final results
def display_final_results(wins, losses, ties):
    # display the final results
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

# call the main function
main()

