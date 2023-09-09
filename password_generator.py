import tkinter as tk
import string
import random
from tkinter import ttk

root = tk.Tk()
font = ("Calibre", 40)
font1 = ("Calibre", 15)
font2 = ("Calibre", 17)

def change(event):
    checkbox=event.widget
    current=checkbox.get()
    checkbox.set(not current)

    

def generator():
    leng=int(slide.get())
    selected_char=''

    if use_digits.get():
        selected_char+=string.digits
    if use_letters_lower.get():
        selected_char+=string.ascii_lowercase
    if use_letters_upper.get():
        selected_char+=string.ascii_uppercase
    if use_punct.get():
        selected_char+=string.punctuation

    if not selected_char:
        password_display.config(text="select atleast one character type",fg="black",font=font2)
        password_strength.config(text="")
    else:
        if leng==0:
            password_display.config(text="Select length",fg="purple",font=font2)
            password_strength.config(text="")
        elif leng<6:
            password_strength.config(text="Weak Password",fg="red",font=font2)
            password=''.join(random.choice(selected_char) for _ in range(leng))
            password_display.config(text=password)
        elif 6<=leng<=11:
            password_strength.config(text="Fair Password",fg="orange",font=font2)
            password=''.join(random.choice(selected_char) for _ in range(leng))
            password_display.config(text=password)
        elif 12<=leng<=16:
            password_strength.config(text="Good Password",fg="blue",font=font2)
            password=''.join(random.choice(selected_char) for _ in range(leng))
            password_display.config(text=password)
        else:
            password_strength.config(text="Strong Password",fg="yellow",font=font2)
            password=''.join(random.choice(selected_char) for _ in range(leng))
            password_display.config(text=password)

    


use_letters_lower=tk.BooleanVar()
use_letters_upper=tk.BooleanVar()
use_digits=tk.BooleanVar()
use_punct=tk.BooleanVar()

label = tk.Label(root, text="Random Password Generator", font=font, fg="white",bg="light green")

slide = tk.Scale(root, variable='Length', orient='horizontal', length=300, width=10, fg="red",bg="light green")
slide['to'] = 30
slide['from'] = 0.0

label1 = tk.Label(root, text="Length",font=font2, fg="brown",bg="light green")

style=ttk.Style()
style.configure("Custom.TCheckbutton",bg="light green",fg="white",font=font1)

Checkbox1 = ttk.Checkbutton(root, text="Uppercase letters(eg.ABC)", variable=use_letters_upper, style="Custom.TCheckbutton")
Checkbox2 = ttk.Checkbutton(root, text="Lowercase letters(eg.abc)",  variable=use_letters_lower,  style="Custom.TCheckbutton")
Checkbox3 = ttk.Checkbutton(root, text="Symbols (eg.@#$%^&*!)",  variable=use_punct,  style="Custom.TCheckbutton")
Checkbox4 = ttk.Checkbutton(root, text="Digits (eg.123)",  variable=use_digits,  style="Custom.TCheckbutton")

button = tk.Button(root, text="Generate",command=generator,font=font1, borderwidth=0, highlightthickness=0,bg="orange",fg="white",activebackground="yellow",padx=10,pady=7)

password_display=tk.Label(root,text="", wraplength=300,font=font1, fg="white",bg="light green")

password_strength=tk.Label(root,text="",font=font1, fg="white",bg="light green")

label.pack()
Checkbox1.place(x=400, y=500)
Checkbox2.place(x=900, y=500)
Checkbox3.place(x=400, y=600)
Checkbox4.place(x=900, y=600)
button.place(x=750, y=300)
slide.place(x=650, y=400)
label1.place(x=750,y=450)
password_display.place(x=650, y=200)
password_strength.place(x=700, y=100)

root.config(bg='light green')
root.mainloop()