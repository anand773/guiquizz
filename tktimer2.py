from tkinter import *
import threading

root = Tk()

def on():
    threading.Timer(5.0, on).start()
    print("hello")

def off():
    exit()
    
buttonstart = Button(root, text="on", command=on)
button = Button(root, text="off", command=off)
buttonstart.pack()
button.pack()
root.mainloop()
