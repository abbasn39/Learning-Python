from tkinter import *


window1= Tk()                           # instant of a window in initialized

window1.geometry("500x500")             # set dimensions of the window

window1.title("Muhammad Abbas")         # Changes the title of the window

icon=PhotoImage(file="lion.png")        # Converts image format into Tkinter readable format
window1.iconphoto(True, icon)    # Set the window icon image to the selected image in the previous line

window1.config(background="green")      # Change the color of the window,
                                        # can also be replaced by a hex value eg background="#6f7d8f"




window1.mainloop()                      #This will show a window on the screen
