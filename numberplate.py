from tkinter import *

new_root = Tk()
#size of window
new_root.geometry("900x800")
new_root.minsize(300,500)
new_root.maxsize(900,9000)
new_root.title("Number plate generator")

#label
label1=Label(text=" WELCOME TO GUJARAT NUMBER PLATE GENERATOR ",bg="black",fg="white",font=("comicsansms",24,"bold"),borderwidth=2,relief=SUNKEN)
label1.grid(row=0)

#frame
f1=Frame(new_root,bg="grey",borderwidth=3,relief=SUNKEN)
f1.grid(column=0)

#menubar
menu=Label(f1,text="Menu Bar")
menu.grid(row=0,column=0)

user =Label(new_root,text="Username")
password =Label(new_root,text="Password")
user.grid(row=1)
password.grid(row=2)

uservalue=StringVar()
passvalue=StringVar()

userentry= Entry(new_root,textvariable=uservalue)
passentry= Entry(new_root,textvariable=passvalue)

userentry.grid(row=1,column=2)
passentry.grid(row=2,column=2)

new_root.mainloop()