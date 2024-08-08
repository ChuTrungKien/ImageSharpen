import tkinter as tk
root = tk.Tk()
root.minsize(width=500, height=300)
var = tk.StringVar()
var.set("Hey!? How are you doing?")
label = tk.Label(root, textvariable=var, fg="blue")
label.pack()

button = tk.Button(text="BUTTON")
button.pack()

root.mainloop()

