from tkinter import *

count=0                             # Initialize a variable
def counter():
    global count                    # make the variable global so we can use inside function
    count += 1
    print(count)                    # This will print the 'count' variable on console
    label.config(text=count)        # This will print on the label inside the window


window_button = Tk()                # Initializing a Window

count_button=Button(window_button,text='Press me to count') # Initializing a button
count_button.config(command=counter)
count_button.config(font=("Arial",20,"italic"))                         # Integrating a command which is to callback function
                                                            # called 'counter'

label=Label(window_button,text=count,
            font=('Monospace',50,"bold"))          # Initializing a Label and setting its text to
                                                            # variable 'count' (line 2)

label.pack()
count_button.pack()


window_button.mainloop()
