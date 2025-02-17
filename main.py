import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("1920x1080")
window.config(bg="lightblue")

# Game options and variables
options = ("rock", "paper", "scissors")
player_choice = None
computer_choice = None

# Function to handle game logic
def play(player_choice):
    global computer_choice
    computer_choice = random.choice(options)
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose {player_choice.capitalize()}, Computer chose {computer_choice.capitalize()}. {result}")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    result_label.config(text="Make your choice!")

# Create a label for the title
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20), bg="lightblue")
title_label.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(window, text="Make your choice!", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

# Create buttons for user choices
rock_button = tk.Button(window, text="Rock", command=lambda: play("rock"), font=("Arial", 14))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", command=lambda: play("paper"), font=("Arial", 14))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play("scissors"), font=("Arial", 14))
scissors_button.pack(pady=5)

# Create a button to play again
play_again_button = tk.Button(window, text="Play Again", command=play_again, font=("Arial", 14))
play_again_button.pack(pady=20)

# Run the window's main loop
window.mainloop()











