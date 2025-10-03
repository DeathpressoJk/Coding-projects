# Make a simple rock paper scissors game 

# importing libraries:
import random 

# list of possible options:

options = {"rock", "paper", "scissors"} 

# user input:
user_input = input("Enter rock, paper or scissors: ").lower() 

#computer input:
computer_input = random.choice(list(options)) 

# print the computer choice: 
print(f"Computer chose: {computer_input}")

# print the user choice:
print(f"You chose: {user_input}")

# check for valid input: 
if user_input not in options:
    print("invalid input, please try again.")
    exit()

# check for a tie: 
if user_input == computer_input:
    print("It's a tie!")
    exit()

# check for a win or loss: 
if (user_input == "rock" and computer_input == "scissors") or \
    (user_input == "paper" and computer_input == "rock") or \
    (user_input == "scissors" and computer_input == "paper"):
    print("You win!")
else:
    print("You lose!")


