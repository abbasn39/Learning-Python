from tkinter import *

count=0                             # Initialize a variable
def counter():
    global count                    # make the variable global so we can use inside function
    count += 1
    print(count)                    # This will print the 'count' variable on console
    label.config(text=count)        # This will print on the label inside the window

def reset():
    global count
    count=0
    print(count)
    label.config(text=count)

def count_back():
    global count
    count -=1
    print(count)
    label.config(text=count)

window_button = Tk()                # Initializing a Window
window_button.title("Counter")

count_button=Button(window_button,text='Press me to count')     # Initializing a button
count_button.config(command=counter)                            # Integrating a command which is to callback function
                                                                # called 'counter'
count_button.config(font=("Arial",20,"italic"))

count_button.pack()

label=Label(window_button,text=count,                           # Initializing a Label and setting its text to
                                                                # variable 'count' (line 2)
            font=('Monospace',50,"bold"))
label.pack()

reset_button=Button(window_button, text="reset counter",font=('Arial',10,"bold"))
reset_button.config(command=reset)
reset_button.pack(side="right")

count_back_button = Button(window_button, text="count back",font=('Arial',10,"bold"))
count_back_button.config(command=count_back)
count_back_button.pack(side="left")

window_button.mainloop()
