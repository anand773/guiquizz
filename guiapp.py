## gui app for quiz program
import tkinter as tk
window = tk.Tk()


def user_login_event(event):
    print(" You rang the Doorbell !")

window.title("Quiz Program")
window.geometry("300x200")

mylabel = tk.Label(text = "Quiz program ")
mylabel.grid(column=1,row=1)

button_name = tk.Button(window, text = "User Login")
button_name.grid(column=2,row=2)
button_name.bind("<Button-1>",user_login_event) #The first parameter <Button-1> is the left click short key of the mouse. When you left-click the button with the mouse, then the event occurs. The second parameter is the name of the event function.





# start the application
window.mainloop()