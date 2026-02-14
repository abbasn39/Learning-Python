# Entry Widget: It is a text box that accepts single line of user input

from tkinter import *

def submit():
    name=entry.get()
    print(name)

def delete():
    entry.delete(0, END)    #deletes everything in the entry box

def backspace():
    entry.delete(len(entry.get())-1,END)

window=Tk()

entry=Entry(window)                         # Assigns entry box to 'window'
entry.config(font=('Arial',30,"bold"),      # Set font of the entry widget box
             bg='black',                    # set background color
             fg='green')                    # set foreground(text) color
#entry.insert(0,'default')                   # sets a default text that appears when the program is executed
                                            # '0' is the index and 'default' is the text that will appear

#entry.config(state="disabled")
entry.config(width=10)
#entry.config(show="*")

submit_button=Button(window,text="Submit",command=submit)
submit_button.pack(side="right")

delete_button=Button(window,text="delete",command=delete)
delete_button.pack(side="right")

backspace_button=Button(window,text="backsapce",command=backspace)
backspace_button.pack(side="right")

entry.pack()

window.mainloop()