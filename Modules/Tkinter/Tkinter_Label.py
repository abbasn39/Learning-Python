from tkinter import *

# Label is an area widget that holds text and or image within a window

window2=Tk()

art= PhotoImage(file="lion.png")

label1=Label(window2,                       # Initializes a Label named 'Label1' inside 'window2'
             text="Hello World",            # Defines the text inside label1
             font=("Arial", 20, "bold"),    # Defines the font of text font=("font_name",size integer,"style")
             foreground="white",            # Font Color can be also written as 'fg', also takes hex value
             background="green",            # Background color for label1
             relief="raised",               # border style
             borderwidth=10,                # border width
             padx=70,                       # Adds padding to x-axis from text to border
             pady=10,                       # Adds padding to y-axis from text to border
             image=art, compound="bottom"   # Adds an image at the bottom of label1
             )



label1.pack()
#label1.place(x=0,y=0)                      # Used to place the label at coordinates(0,0)
                                            # from top right corner

window2.mainloop()