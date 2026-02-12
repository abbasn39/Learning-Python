from tkinter import *

def hello():
    print("Hello Friends")

window3=Tk()                                    # creates a window

button1=Button(window3, text="Add one!!")    # creates a button that says 'Add one!!!'

button1.config(command=hello)                   # performs callback of a function in this case 'hello'

button1_image=PhotoImage(file='lion.png')

button1.config(font=("ink free", 20,"bold"),    # set font, font size, font style
               background="red",                # sets color of button background, not pressed
               foreground="black",              # sets color of font, not pressed
               activebackground="green",        # sets color of button when pressed
               activeforeground="yellow",       # sets color of button's text when pressed
               image=button1_image,
               compound="bottom",
               )


#button1.config(state="disabled")               #This disables the button and prevents it from being pressed.

button1.pack()
window3.mainloop()