## Tkniter grid system
# https://www.pythontutorial.net/tkinter/tkinter-grid/
import tkinter as tk
from tkinter import ttk ## ttk Theamed Tkinter widgets new widgets

import time
import mysql.connector
import random

# root windows
root = tk.Tk()
root.title("Quiz Program")
root.geometry("500x350") ## width x height
root.resizable(0,0)

# configure the grid
root.columnconfigure(0,weight=1) # 0th column width weigtage = 1
root.columnconfigure(1,weight=3) # 1th column width weigtage = 3 times of the col 0

## define command binding functions
def btnlogin_clicked():
    print('btnlogin clicked')


# populate the windows

# username
username_label = ttk.Label(root,text="User Name :")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
## The sticky option specifies which edge of the cell the widget should stick to.
# W West or Left Center ref: the link placed at top of file

username_entry  = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.W, padx=5,pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login",command=btnlogin_clicked)
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
##login_button.pack() #This geometry manager organizes widgets in blocks before placing them in the parent widget.
## not need as it is already packed by grid geometry manager


if __name__ == "__main__":
    # start the window show
    root.mainloop()