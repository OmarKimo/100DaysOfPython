import tkinter as tk

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, background=THEME_COLOR)
        
        self.score_label = tk.Label(self.window, text="Score: 0", foreground="white", font=("Arial", 10, "bold"), background=THEME_COLOR, highlightthickness=0, pady=10)
        self.score_label.grid(row=1, column=2)

        self.canvas = tk.Canvas(self.window, width=300, height=250)
        self.text_container = self.canvas.create_text(150, 125, width=280, justify="center", font=("Arial", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)
        
        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(self.window, image=true_image, highlightthickness=0, command= lambda: self.check_answer("True"))
        self.true_button.grid(row=3, column=1)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(self.window, image=false_image, pady=30, highlightthickness=0, command= lambda: self.check_answer("False"))
        self.false_button.grid(row=3, column=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        self.score_label["text"] = f"Score: {self.quiz.score}"
        if self.quiz.can_ask():
            self.canvas.itemconfig(self.text_container, text=self.quiz.ask())
        else:
            self.finish()

    def check_answer(self, answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.next_question)
        
    def finish(self):
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        self.canvas.itemconfig(self.text_container, text=f"You've reached the end of quiz.\nYour final score is: {self.quiz.score}/{self.quiz.cur_q}")