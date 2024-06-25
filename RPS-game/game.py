import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissor Game")
        self.root.geometry("400x400")

        self.rps = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
        self.track_list = []

        self.create_widgets()
        self.decorate()

    def decorate(self):
        self.titleLabel.config(width=21, height=2)

        self.root.configure(bg="light blue")
        # rock
        self.rockButton.config(width=8, height=2)
        self.rockButton.place(x=80, y=60)
        self.rockButton.configure(bg="darkgray")
        # paper
        self.paperButton.config(width=8, height=2)
        self.paperButton.place(x=170, y=60)
        # scissor
        self.scissorButton.config(width=8, height=2)
        self.scissorButton.place(x=260, y=60)
        self.scissorButton.configure(bg="orange")

        # labels
        self.titleLabel.place(x=70, y=0)
        self.titleLabel.config(font=("Arial Black", 14))
        self.titleLabel.config(bg="light blue")

        self.computerLabel.place(x=0, y=200)
        self.computerLabel.config(bg="Aqua")

        self.playerLabel.place(x=0, y=250)
        self.playerLabel.config(bg="Aqua")

        self.resultLabel.place(x=0, y=300)
        self.resultLabel.config(bg="#b8df10")  # bitter lemon green.

        self.show_history_button.place(x=165, y=350)
        self.show_history_button.config(bg="#9ACEEB")  # Cornflower Blue

    def create_widgets(self):
        self.titleLabel = tk.Label(self.root, text="Rock-Paper-Scissor", width=20)

        self.rockButton = tk.Button(self.root, text="Rock", command=lambda: self.play_game(1, "Rock"))

        self.paperButton = tk.Button(self.root, text="Paper", command=lambda: self.play_game(2, "Paper"))

        self.scissorButton = tk.Button(self.root, text="Scissor", command=lambda: self.play_game(3, "Scissor"))

        self.computerLabel = tk.Label(self.root, text="Computer: ", width=60)

        self.playerLabel = tk.Label(self.root, text="Player: ", width=60)

        self.resultLabel = tk.Label(self.root, text="Result", width=60)

        self.show_history_button = tk.Button(self.root, text="Show History", command=self.show_history)

    def hide_widgets(self):
        for widget in self.root.winfo_children():
            widget.place_forget()

    def show_widgets(self):
        self.decorate()

    def play_game(self, user, rps_value):
        computer = random.randint(1, 3)
        self.playerLabel.config(text=f"Player: {rps_value}")
        c = self.rps.get(computer)
        self.computerLabel.config(text=f"Computer: {c}")
        if user == computer:
            self.resultLabel.config(text="It's a Tie")
            self.track_list.append("Tie")
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            self.resultLabel.config(text="Player Wins")
            self.track_list.append("Won")
        else:
            self.resultLabel.config(text="Computer Wins")
            self.track_list.append("Lose")

    def show_history(self):
        self.hide_widgets()
        self.history_window = HistoryWindow(self.root, self.track_list, self)

class HistoryWindow:
    def __init__(self, root, history, parent):
        self.root = root
        self.history = history
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root, bd=0, highlightthickness=0, relief= 'flat')
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.listbox.config(font=(10))
        self.listbox.pack(pady=5)
        self.listbox.config(bg="black", fg="white")
        
        if not self.history:
            self.listbox.insert(tk.END, "Empty!")
        for i in self.history:
            self.listbox.insert(tk.END, i)
        self.back_button = tk.Button(self.root, text="Back", command=self.back)
        self.back_button.pack()
        self.back_button.config(bg="gray")

    def back(self):
        self.clear_widgets()
        self.parent.show_widgets()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

# if __name__ == "__main__":
#     root = tk.Tk()
#     RockPaperScissorsGame(root)
    # root.mainloop()