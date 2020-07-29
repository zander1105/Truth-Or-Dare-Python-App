import tkinter as tk
from random import *
import datetime

now = datetime.datetime.now()
seed(now)

dares = ["Show your browsing history to the whole room",
"Test Dare 2",
"Test Dare 1",]

truths = ["What are your top three turn-ons",
"What is your biggest fear in a relationship",
"If you coud do anything illegal and not suffer consequences what would it be??",
"Who would you hook-up with for money"        
         
         
         
         ]

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
