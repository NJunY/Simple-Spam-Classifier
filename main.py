import tkinter as tk
from PIL import Image, ImageTk
import pickle
from tkinter import messagebox

def check(event):
    with open('model_pickle', 'rb') as file:
        mp = pickle.load(file)
    text = entry.get()
    ans = mp.predict([text])
    x = "Yes" if ans[0] == 1 else "No"
    messagebox.showinfo(title="Scam?", message=x)

window = tk.Tk()

#title
window.title("Simple Span Classifier")

img = ImageTk.PhotoImage(Image.open("banner.png"))
panel = tk.Label(window,
                 image=img,
                 bg="white")
panel.pack()

#Input
entry = tk.Entry(fg="black",
                 bg="white",
                 width=50)
entry.pack()

#Button
button = tk.Button(text="Click Me!",
                   width=20,
                   height=5)
button.pack()
button.bind('<Button-1>', check)

window.mainloop()
