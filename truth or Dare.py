import tkinter as tk
from random import *
import datetime

now = datetime.datetime.now()
seed(now)

dares = [" Test Dare 3",
"Test Dare 2",
"Test Dare 1",]

truths = ["Test Question 3",
"Test Question 2",
"Test Qestion",]

def dare():
    dareoutput = choice(dares)
    print(dareoutput)

def truth():
    truthoutput = choice(truths)
    print(truthoutput)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="Truth",
                   fg="red",
                   command=truth)
button.pack(side=tk.LEFT)
DareButton = tk.Button(frame,
                   text="Dare",
                   command=dare)
DareButton.pack(side=tk.LEFT)

root.mainloop()
