from tkinter import *
#Picture_adjustments
import sys
import os

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return filename
#Functions

def submit():

    input_date=enter.get()
    print(input_date)
    try:
        date=int(input_date)
        if date == 28 :
            label2.config(text="Happy Birthday Nigga")
            label3.pack()
            label4.pack_forget()
            label5.pack_forget()
        elif date == 29 :
            label2.config(text="Happy Birthday Nigga")
            label3.pack()
            label4.pack_forget()
            label5.pack_forget()
        else:
            label2.config(text="What the fuck bitch? Your mom didn't tell you when you were born?")
            label4.pack()
            label3.pack_forget()
            label5.pack_forget()
    except ValueError:
        label2.config(text="How fucking thick in the head are you? I asked for a number HOE")
        label5.pack()
        label3.pack_forget()
        label4.pack_forget()
#Functions


#Window
window=Tk()

window.title("For my Nigga")



#Frame_open
Frame=Frame(window)
Frame.pack()
#Frame_close

#Label1_open
label1=Label(Frame,text="What date of february were you born on(1-29)")
label1.config(font=("Calibri",15))
label1.pack(side="left")
#Label1_close





#Submit_open
submit=Button(Frame,text="Submit",command=submit)

submit.config(font=("calibri",15))

submit.pack(side="right")
#Submit_close


#Entry_open
enter=Entry(Frame)


enter.config(font=("Calibri",20))
enter.config(bg="white")
enter.config(fg="black")

enter.pack(ipadx=10)
#Entry_close


#Label2_open
label2=Label(window,text=enter.get())
label2.config(font=("Calibri",15))
label2.config(pady=20)
label2.pack(side="bottom")
#Label2_close

#Label3_open
hbd=PhotoImage(file=resource_path("hbday.png"))
label3=Label(window,image=hbd)
label3.config(compound="bottom")
#Label3_close


#Label4_open
confused=PhotoImage(file=resource_path("confused.png"))
label4=Label(window,image=confused)
label4.config(compound="bottom")
#Label4_close

#Label5_open
spongebob=PhotoImage(file=resource_path("spongebob.png"))
label5=Label(window,image=spongebob)
label5.config(compound="bottom")
#Label5_close
window.mainloop()
#Window