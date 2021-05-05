import tkinter as tk
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
stage = 1
stopped = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global stage, stopped
    stage = 1
    stopped = True
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfigure(timer, text="00:00")
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global stopped
    stopped = False
    if stage > 8:
        reset()
    elif stage % 2:
        window.lift()
        label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)
    elif stage == 8:
        window.lift()
        check_marks['text'] += "✔"
        label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)
    else:
        window.lift()
        check_marks['text'] += "✔"
        label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time_amt):
    global stage
    if stopped:
        return
    if time_amt == -1: 
        stage += 1
        start()
        return
    minutes, seconds = divmod(time_amt, 60)
    minutes = str(minutes)
    seconds = str(seconds)
    if len(minutes) == 1: minutes = "0" + minutes
    if len(seconds) == 1: seconds = "0" + seconds
    canvas.itemconfigure(timer, text=f"{minutes}:{seconds}")
    window.after(1000, countdown, time_amt - 1)        

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=500, height=450)
window.config(padx=110, pady=50,background=YELLOW)


label = tk.Label(text="Timer", font=(FONT_NAME, 30, 'bold'), foreground=GREEN, background=YELLOW)
label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(107, 130, text="00:00", fill="white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

startButton = tk.Button(text="Start", command=start)
startButton.grid(column=0, row=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)

resetButton = tk.Button(text="Reset", command=reset)
resetButton.grid(column=2, row=2)

window.mainloop()