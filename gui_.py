from tkinter import *
from tkinter import messagebox
import random
def no():
    messagebox.showinfo(' ','Thanks bro')
    quit()

def motionmouse(event):
    btnYes.place(x=random.randint(0,500),y=random.randint(0,500))

root=Tk()
root.geometry('500x500')
#root.resizable(width=False,height=False)
root['bg']='#aa22aa'
label=Label(root,text='Are you guy', font='Arial 20 bold', bg='white').grid(row=2,column=10)
l=Label(root,text="hello" ,font="Calibri 20 bold")

#label.pack()
btnYes=Button(root,text='No',font='Arial 20 bold')
btnYes.place(x=170,y=100)
btnYes.bind('<Enter>', motionmouse)

btnNo=Button(root,text='yes', font='Arial 20 bold' ,command=no)
btnNo.place(x=350,y=100)
root.mainloop()
