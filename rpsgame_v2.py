import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

# def get_user_selection():
#     user_input = input("Enter a choice (rock[1], paper[2], scissors[3]): ")
#     selection = int(user_input)
#     action = Action(selection)
#     return action

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selction():
    selection = random.randint(1, len(Action))
    action = Action(selection)
    return action

def get_score(n):
    user_score = 0
    cpu_score = 0
    if n == 1:
        user_score += 1
    elif n == 2:
        cpu_score += 1
    print(f"User: {user_score} CPU: {cpu_score}")
      
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            get_score(1)
            # user_score += 1
            print("Rock smashes Scissors! You win!")
        else:
            get_score(2)
            # cpu_score += 1
            print("Paper covers Rock! You lose!")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            get_score(1)
            # user_score += 1
            print("Paper covers Rock! You win!")
        else:
            get_score(2)
            # cpu_score += 1
            print("Scissors cuts Paper! You lose!")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            get_score(1)
            # user_score += 1
            print("Scissors cuts Paper! You win!")
        else:
            get_score(2)
            # cpu_score +=1
            print("Rock smashes Scissors! You Lose!")
    
while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[1, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selction()
    determine_winner(user_action, computer_action)
    get_score()
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")

#     possibe_actions = ["rock","paper", "scissors"]
#     computer_action = random.choice(possibe_actions)

#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             user_score += 1
#             print("Rock smashes Scissors! You win!")
#         else:
#             cpu_score += 1
#             print("Paper covers Rock! You lose!")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             user_score += 1
#             print("Paper covers Rock! You win!")
#         else:
#             cpu_score += 1
#             print("Scissors cuts Paper! You lose!")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             user_score += 1
#             print("Scissors cuts Paper! You win!")
#         else:
#             cpu_score +=1
#             print("Rock smashes Scissors! You Lose!")

#     print(f"Score:\nUser: {user_score} CPU: {cpu_score}")
#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() !="y":
#         break