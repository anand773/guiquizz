from tkinter import *
import time

mincount = 120
def clock():
    hour = time.strftime("%I")
    minu = time.strftime("%M")
    secc = time.strftime("%S")
    am_pm = time.strftime("%p")
    my_label.config(text=hour+":"+minu+":"+secc+" "+am_pm)
    my_label1.config(text="left time: {}".format(mincount))
    my_label.after(1000,clock)
    #my_label.after(10000,chcounter)

def chcounter():
    global mincount
    my_label1.config(
        text="left time: {}".format(mincount)
    ) 
    my_label.after(10000,chcounter)   
    mincount -= 1

root = Tk()
root.title="Tktimer3"
root.geometry("500x400")

my_label = Label(root, text="Old Text", font=("Helvetica",24), fg="green", bg="black")
my_label.pack(pady=20)
my_label1 = Label(root, text="Min left", font=("Helvetica", 24) )
my_label1.pack(pady=20)

clock()
chcounter()
root.mainloop()