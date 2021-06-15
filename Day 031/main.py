import csv
import tkinter as tk
import pandas
import random

after_id = None

def toBack():
    canvas.itemconfig(image_container, image=back_img)
    canvas.itemconfig(text1_container, text="English")
    canvas.itemconfig(text2_container, text=french_dict[current_word])

def toFront():
    global after_id
    canvas.itemconfig(image_container, image=front_img)
    canvas.itemconfig(text1_container, text="French")
    canvas.itemconfig(text2_container, text=current_word)
    after_id = window.after(4000, toBack)

def on_false():
    global after_id
    window.after_cancel(after_id)
    global current_word
    current_word = random.choice(list(french_dict.keys()))
    toFront()
    #print("image1 clicked")

def on_true():
    global after_id
    window.after_cancel(after_id)
    global current_word
    french_dict.pop(current_word)
    current_word = random.choice(list(french_dict.keys()))
    toFront()
    #print("image2 clicked")

words = None
try:
    words = pandas.read_csv("Day 031/data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("Day 031/data/french_words.csv")

french_dict = {row.French:row.English for _, row in words.iterrows()}
#english_dict = {row.English:row.French for _, row in words.iterrows()}
current_word = random.choice(list(french_dict.keys()))

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
    
canvas = tk.Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = tk.PhotoImage(file="Day 031/images/card_front.png")
back_img = tk.PhotoImage(file="Day 031/images/card_back.png")
image_container = canvas.create_image(400, 263, image=front_img)
text1_container = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
text2_container = canvas.create_text(400, 263, text=current_word, font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

img1 = tk.PhotoImage(file="Day 031/images/wrong.png")
b1 = tk.Button(window, image=img1, command=on_false, background=BACKGROUND_COLOR, highlightthickness=0)
b1.grid(row=2,column=1)

img2 = tk.PhotoImage(file="Day 031/images/right.png")
b2 = tk.Button(window, image=img2, command=on_true, background=BACKGROUND_COLOR, highlightthickness=0)
b2.grid(row=2,column=2)

after_id = window.after(4000, toBack)

window.mainloop()

# save unknown words to words_to_learn.csv
df = pandas.DataFrame({"French": list(french_dict.keys()), "English": list(french_dict.values())})
#print(df)
df.to_csv("Day 031/data/words_to_learn.csv", index=False)
#print("finished")