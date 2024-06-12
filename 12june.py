'''
import tkinter as tk

root = tk.Tk()
root.title('Entry Fields Example')

tk.Label(root, text='First Name').grid(row=0, column=0)
tk.Label(root, text='Last Name').grid(row=1, column=0)

fn = tk.Entry(root)
ln = tk.Entry(root)
fn.grid(row=0, column=1)
ln.grid(row=1, column=1)

root.mainloop()
'''
'''
import tkinter as tk

root = tk.Tk()
root.title('Checkboxes Example')

var1 = tk.IntVar()
tk.Checkbutton(root, text='Female', variable=var1).grid(row=0, sticky='w')

var2 = tk.IntVar()
tk.Checkbutton(root, text='Male', variable=var2).grid(row=1, sticky='w')

root.mainloop()
'''
'''
import tkinter as tk

root = tk.Tk()
root.title('Radio Buttons Example')

v = tk.IntVar()
tk.Radiobutton(root, text='Option A', variable=v, value=1).grid(row=0, column=0)
tk.Radiobutton(root, text='Option B', variable=v, value=2).grid(row=1, column=0)

root.mainloop()
'''
'''
import tkinter as tk

def on_submit():
    print("Welcome to Ziyaad sir's bootcamp")

root = tk.Tk()
root.title('Button Example')

btn = tk.Button(root, text='Submit', command=on_submit)
btn.grid(row=0, column=0, pady=10)

root.mainloop()
'''
