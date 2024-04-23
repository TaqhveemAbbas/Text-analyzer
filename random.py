import random
import tkinter as tk
from tkinter import messagebox

def generate_winner(participants):
    if participants:
        winner = random.choice(participants)
        messagebox.showinfo("Winner", f"The winner of this tournament is: {winner}")
    else:
        messagebox.showinfo("No Participants", "Please add participants")

def on_generate_winner():
    participants = entry_participants.get("1.0", tk.END).splitlines()
    participants = [participant.strip() for participant in participants if participant.strip()]
    generate_winner(participants)

window = tk.Tk()
window.title("Winner")

label_participants = tk.Label(window, text="Participants")
label_participants.pack()

entry_participants = tk.Text(window, height=15, width=30)
entry_participants.pack()

button_generate = tk.Button(window, text="Generate Winner", command=on_generate_winner)
button_generate.pack()

window.mainloop()
