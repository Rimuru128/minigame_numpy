import tkinter as tk
from tkinter import messagebox
import numpy as np

class MathGame:
    def __init__(self, master):
        self.master = master
        master.title("🧠 NumPy Math Game")
        master.geometry("400x300")
        master.configure(bg="#f0f8ff")

        self.score = 0
        self.round = 0
        self.total_rounds = 5

        self.question_label = tk.Label(master, text="", font=("Arial", 18), bg="#f0f8ff")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=("Arial", 16))
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer, font=("Arial", 14), bg="#add8e6")
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(master, text="", font=("Arial", 14), bg="#f0f8ff")
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=("Arial", 14), bg="#f0f8ff")
        self.score_label.pack()

        self.next_question()

    def generate_question(self):
        operations = ['+', '-', '*', '/']
        op = np.random.choice(operations)
        num1 = np.random.randint(1, 100)
        num2 = np.random.randint(1, 20)

        if op == '/':
            num1 = num1 * num2
            question = f"{num1} {op} {num2}"
            answer = round(num1 / num2, 2)
        elif op == '+':
            question = f"{num1} {op} {num2}"
            answer = num1 + num2
        elif op == '-':
            question = f"{num1} {op} {num2}"
            answer = num1 - num2
        elif op == '*':
            question = f"{num1} {op} {num2}"
            answer = num1 * num2

        return question, answer

    def next_question(self):
        if self.round >= self.total_rounds:
            messagebox.showinfo("Game Over", f"Your final score: {self.score}/{self.total_rounds}")
            self.master.destroy()
            return
        self.round += 1
        self.current_question, self.correct_answer = self.generate_question()
        self.question_label.config(text=f"Q{self.round}: {self.current_question}")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        try:
            user_answer = float(self.answer_entry.get())
            if abs(user_answer - self.correct_answer) < 0.01:
                self.feedback_label.config(text="✅ Correct!", fg="green")
                self.score += 1
            else:
                self.feedback_label.config(text=f"❌ Wrong! Correct: {self.correct_answer}", fg="red")
        except ValueError:
            self.feedback_label.config(text="⚠️ Please enter a valid number.", fg="orange")

        self.score_label.config(text=f"Score: {self.score}")
        self.master.after(1500, self.next_question)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
