'''
from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

button = Button(frame, text='Geek')
button.pack()


root.mainloop()
'''
'''
from tkinter import *

root = Tk()
root.title("Simple Tkinter Example")
root.geometry('400x400')

text = Entry(root, width=30, bg='White')
text.pack(pady=10)

def update_text(language):
    text.delete(0, END)
    text.insert(0, language)

def create_button(lang):
    return Button(root, text=lang, command=lambda: update_text(lang))

languages = ["Python", "Java", "R", "JavaScript"]
for lang in languages:
    btn = create_button(lang)
    btn.pack(pady=10)

root.mainloop()

'''
'''
import tkinter as tk

root = tk.Tk()
root.title('Shuffled Tkinter App')

tk.Label(root, text='Username').grid(row=0)
tk.Label(root, text='Password').grid(row=1)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

gender1 = tk.IntVar()
tk.Checkbutton(root, text='Female', variable=gender1).grid(row=2, sticky='w')
gender2 = tk.IntVar()
tk.Checkbutton(root, text='Male', variable=gender2).grid(row=3, sticky='w')
root.mainloop()
'''