from tkinter import *
import threading
import time

root = Tk()
root.geometry("500x400")

def onn():
    ##threading.Timer(5.0, on).start()
    while True:
        print("hello")
        time.sleep(2)


def offf():
    exit()
    
buttonstart = Button(root, text="hello 2 sec", command=threading.Thread(target=onn).start())
button = Button(root, text="off", command=offf)
buttonstart.pack(pady=20)
button.pack(pady=20)
root.mainloop()
