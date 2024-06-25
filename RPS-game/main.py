import tkinter as tk
from game import RockPaperScissorsGame

class InstructionWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissor Instructions")
        self.root.configure(bg='gray')
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.root, text=self.get_instructions(), bg="#008970", wraplength=380)
        self.play_button = tk.Button(self.root, text="Play", width=20, command=self.play, bg="#99eedf")

    def layout_widgets(self):
        self.instruction_label.pack(padx=10, pady=10)
        self.play_button.pack(pady=10)

    def get_instructions(self):
        return (
            "How to Play:\n"
            "Click a button: Rock, Paper, or Scissors.\n"
            "The computer will randomly choose its hand sign.\n"
            "The winner is determined based on the classic rules (Rock crushes Scissors, Paper covers Rock, Scissors cuts Paper).\n"
            "Ties: If you and the computer choose the same sign, it's a tie! Just play again.\n"
            "Good luck!"
        )

    def play(self):
        self.root.destroy()  # Destroy the instruction window
        game_root = tk.Tk()  # Create a new root for the game
        RockPaperScissorsGame(game_root)  # Initialize the game window
        game_root.mainloop()  # Start the game mainloop

if __name__ == "__main__":
    root = tk.Tk()
    InstructionWindow(root)
    root.mainloop()
