import tkinter as tk
from tkinter import ttk

def calc():

    num = number.get()
    output = float(num) * 1.61
    output2.set(output)


root = tk.Tk()
root.geometry('300x150')

# title text
label = tk.Label(root, text='Miles to Km converter', font= ('arial', 14, 'bold', 'italic'))
label.pack()

# INput frame for components
inframe = ttk.Frame()
number = tk.IntVar()

entry = ttk.Entry(inframe, textvariable= number)
button = ttk.Button(inframe, text= 'Convert', command= calc)

inframe.pack(pady=15)
entry.pack(side='left', padx=14)
button.pack(side='left')

# output frame
output2 = tk.IntVar()

label2 = ttk.Label(root, textvariable=output2)
label2.pack()



root.mainloop()
