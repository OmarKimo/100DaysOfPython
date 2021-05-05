import tkinter as tk

app = tk.Tk()
app.title("Mile to Km Converter")
app.config(padx=15, pady=15)
#app.minsize(width=280, height=125)

entry = tk.Entry(width=10)
entry.grid(column=1, row=0)

label1 = tk.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tk.Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = tk.Label(text="0")
label3.grid(column=1, row=1)

label4 = tk.Label(text="Km")
label4.grid(column=2, row=1)

def calculate():
    miles = entry.get()
    if not miles: 
        miles = 0
    else:
        miles = float(miles)
    label3.config(text=f"{round(miles * 1.6)}")

button = tk.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

app.mainloop()