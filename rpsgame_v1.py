import random

user_score = 0
cpu_score = 0

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")

    possibe_actions = ["rock","paper", "scissors"]
    computer_action = random.choice(possibe_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")ø

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            user_score += 1
            print("Rock smashes Scissors! You win!")
        else:
            cpu_score += 1
            print("Paper covers Rock! You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            user_score += 1
            print("Paper covers Rock! You win!")
        else:
            cpu_score += 1
            print("Scissors cuts Paper! You lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
            user_score += 1
            print("Scissors cuts Paper! You win!")
        else:
            cpu_score +=1
            print("Rock smashes Scissors! You Lose!")

    print(f"Score:\nUser: {user_score} CPU: {cpu_score}")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() !="y":
        break