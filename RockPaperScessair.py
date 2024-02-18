import tkinter as tk
from tkinter import messagebox
import random as r

class player :
    def __init__(self):
       
        self.score=0

    def play_game(self,player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = r.choice(choices)

        result =self.determine_winner(player_choice, computer_choice)
        sc=self.score

        messagebox.showinfo("    Result :   ", f"   Computer chose   {computer_choice} {result} \n {sc}")

    def determine_winner(self,player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock")or(player_choice == "Scissors" and computer_choice == "Paper"):
            self.score +=1
            return "You win!"
        else:
            self.score -= 1
            return "You lose!"
    def play(self):
        window = tk.Tk()
        window.title("Rock - Paper - Scissors  ")

        rock_button = tk.Button(window, text="  Rock  ", command=lambda: self.play_game("Rock"))
        paper_button = tk.Button(window, text="  Paper  ", command=lambda: self.play_game("Paper"))
        scissors_button = tk.Button(window, text="  Scissors  ", command=lambda: self.play_game("Scissors"))
        exit_button = tk.Button(window, text="  EXIT  ", command=window.destroy)

        rock_button.pack(pady=60)
        paper_button.pack(pady=60)
        scissors_button.pack(pady=60)
        exit_button.pack(pady=60)   

        window.mainloop()

p=player()
window = tk.Tk()
window.title("start menu Game")
start_button = tk.Button(window, text="  START  ", command=lambda: p.play())
exit_button = tk.Button(window, text="  EXIT  ", command=window.destroy)

start_button.pack(pady=60)
exit_button.pack(pady=60)   
window.mainloop()
   