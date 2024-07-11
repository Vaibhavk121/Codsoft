import tkinter as tk
from tkinter import messagebox
import random


def determine_winner(user_choice, autochoice):
    if user_choice == autochoice:
        return "tie"
    elif (user_choice == "rock" and autochoice == "scissors") or \
         (user_choice == "scissors" and autochoice == "paper") or \
         (user_choice == "paper" and autochoice == "rock"):
        return "user"
    else:
        return "computer"

#choice selection
def user_choice(choice):
    autochoice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(choice, autochoice)
    
    if result == "user":
        result_text.set("You win!")
        scores['user'] += 1
    elif result == "computer":
        result_text.set("You lose!")
        scores['computer'] += 1
    else:
        result_text.set("It's a tie!")
    
    user_choice_text.set(f"Your choice: {choice.capitalize()}")
    autochoice_text.set(f"Computer's choice: {autochoice.capitalize()}")
    score_text.set(f"Scores - You: {scores['user']} Computer: {scores['computer']}")

#reset the game
def reset_game():
    scores['user'] = 0
    scores['computer'] = 0
    user_choice_text.set("")
    autochoice_text.set("")
    result_text.set("")
    score_text.set(f"Scores - You: {scores['user']} Computer: {scores['computer']}")

#start of the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.resizable(False, False)

# Load images
rock_img = tk.PhotoImage(file="Images/rock.png").subsample(50,50)
paper_img = tk.PhotoImage(file="Images/hand.png").subsample(6,6)
scissors_img = tk.PhotoImage(file="Images/scissors.png").subsample(6,6)

# Initialize scores
scores = {'user': 0, 'computer': 0}

# Create StringVars for dynamic text
user_choice_text = tk.StringVar()
autochoice_text = tk.StringVar()
result_text = tk.StringVar()
score_text = tk.StringVar(value=f"Scores - You: {scores['user']} Computer: {scores['computer']}")

# Create UI elements
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14)).pack(pady=10)

btn_frame = tk.Frame(frame)
btn_frame.pack(pady=10)
tk.Button(btn_frame, image=rock_img, command=lambda: user_choice("rock")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, image=paper_img, command=lambda: user_choice("paper")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, image=scissors_img, command=lambda: user_choice("scissors")).pack(side=tk.LEFT, padx=5)

tk.Label(frame, textvariable=user_choice_text, font=("Helvetica", 12)).pack(pady=5)
tk.Label(frame, textvariable=autochoice_text, font=("Helvetica", 12)).pack(pady=5)
tk.Label(frame, textvariable=result_text, font=("Helvetica", 16)).pack(pady=10)
tk.Label(frame, textvariable=score_text, font=("Helvetica", 12)).pack(pady=5)

tk.Button(frame, text="Reset Game", command=reset_game, font=("Helvetica", 12)).pack(pady=10)

# Start the main loop
root.mainloop()
