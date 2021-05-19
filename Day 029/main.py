import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator(n_char=10, n_num=4, n_sym=4):
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars += chars.upper()
    nums = "0123456789"
    syms = "!#$%^&*()-_=/+][}{><:;~"

    password = (
        random.choices(chars, k=n_char)
        + random.choices(nums, k=n_num)
        + random.choices(syms, k=n_sym)
    )
    random.shuffle(password)
    password = "".join(password)
    print(password)
    pass_text.delete(0, tk.END)
    pass_text.insert(0, password)
    pass_text.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = pass_text.get()

    if not (website and email and password):
        messagebox.showwarning(
            title="Warning", message="Please don't leave any fields empty!"
        )
        return

    if not messagebox.askyesno(
        title=website, message=f"Email: {email}\nPassword:{password}\nIs this ok?"
    ):
        return
    with open("auth_data.txt", "w+") as f:
        f.write(f"{website} | {email} | {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
bg = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=bg)
canvas.grid(column=2, row=1)

website_label = tk.Label(text="Website:")
website_label.grid(column=1, row=2)

website_text = tk.Entry(width=35)
website_text.grid(column=2, row=2, columnspan=2)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=1, row=3)

email_text = tk.Entry(width=35)
email_text.grid(column=2, row=3, columnspan=2)

pass_label = tk.Label(text="Password:")
pass_label.grid(column=1, row=4)

pass_text = tk.Entry(width=21)
pass_text.grid(column=2, row=4)

generate_but = tk.Button(text="Generate Password", command=generator)
generate_but.grid(column=3, row=4)

add_but = tk.Button(text="Add", width=36, command=save)
add_but.grid(column=2, row=5, columnspan=2)

window.mainloop()