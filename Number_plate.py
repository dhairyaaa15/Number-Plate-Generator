from tkinter import *
from tkinter import messagebox
import random

#for exiting or closing whole window
def Exit_screen():
    exit = messagebox.askquestion("Do you really want to exit ?")
    if exit=="yes":
        root.destroy()
    else:
        messagebox.showinfo("Returning")

#title and geometry setting
root = Tk()
root.geometry("1280x720")
root.title("RTO")
mainlabel=Label(text=" WELCOME TO GUJARAT NUMBER PLATE GENERATOR ",font="Helvetica 20 bold",fg="grey",bd=10,relief=RIDGE)
mainlabel.pack(fill=X)

aboutframe=None
helpframe=None
menuframe=None
button_frame=None

#function for opening page to generate number plate
def menu_fun():
    global menuframe
    global button_frame
    if menuframe:
        menuframe.destroy()
    if button_frame:
        button_frame.destroy()

    menuframe=Frame(root,height=1080,width=350,bd=10,relief=SUNKEN)
    menuframe.pack(fill=X,side=TOP)

    #validation for first name
    def fn_valid():
        first=fn.get()
        if len(first)==0:
            msg.config(text="first name is must")
        else:
            try:
                if any(ch.isdigit() for ch in first):
                    msg.config(text="it cannot contain digit!")
                elif len(first)<=2:
                    msg.config(text="lenght is too small!")
                elif len(first)>15:
                    msg.config(text="Huge name!")
                else:
                    msg.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    #validation for last name
    def ln_valid():
        first=ln.get()
        if len(first)==0:
            msg1.config(text="last name is must")
        else:
            try:
                if any(ch.isdigit() for ch in first):
                    msg1.config(text="it cannot contain digit!")
                elif len(first)<=2:
                    msg1.config(text="lenght is too small!")
                elif len(first)>15:
                    msg1.config(text="Huge name!")
                else:
                    msg1.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    #validation for middle name
    def mn_valid():
        first=mn.get()
        if len(first)==0:
            msg2.config(text="middle name is must")
        else:
            try:
                if any(ch.isdigit() for ch in first):
                    msg2.config(text="it cannot contain digit!")
                elif len(first)<=2:
                    msg2.config(text="lenght is too small!")
                elif len(first)>15:
                    msg2.config(text="Huge name!")
                else:
                    msg2.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True

    #validation for phone number
    def ph_valid():
        first=phnum.get()
        if len(first)==0:
            msg3.config(text="phone number is must")
        else:
            try:
                if any(ch.isalpha() for ch in first):
                    msg3.config(text="it cannot contain alphabet!")
                elif len(first)<10:
                    msg3.config(text="must be of 10 numbers!")
                elif len(first)>10:
                    msg3.config(text="invalid number!")
                else:
                    msg3.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    #validation for pincode
    def pin_valid():
        first=a3.get()
        if len(first)==0:
            msg4.config(text="pincode is must")
        else:
            try:
                if any(ch.isalpha() for ch in first):
                    msg4.config(text="it cannot contain alphabet!")
                elif len(first)<6:
                    msg4.config(text="must be of 5 numbers!")
                elif len(first)>6:
                    msg4.config(text="invalid number!")
                else:
                    msg4.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    #validation for city
    def ct_valid():
        first=a4.get()
        if len(first)==0:
            msg5.config(text="city is must")
        else:
            try:
                if any(ch.isdigit() for ch in first):
                    msg5.config(text="it cannot contain digit!")
                elif first=="Ahemdabad" or first=="ahemdabad" or first=="Vadodara" or first=="vadodara" or first=="anand" or first=="Anand" or first=="Jamnagar" or first=="Jamnagar" or first=="Rajkot" or first=="rajkot":
                    msg5.config(text="")
                else:
                    msg5.config(text="no such city associated")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    #validation for company name
    def cm_valid():
        first=cmp.get()
        if len(first)==0:
            msg6.config(text="company name is must")
        else:
            try:
                if any(ch.isdigit() for ch in first):
                    msg6.config(text="it cannot contain digit!")
                elif len(first)<=2:
                    msg6.config(text="lenght is too small!")
                elif len(first)>12:
                    msg6.config(text="Huge name!")
                else:
                    msg2.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    #validation for model number
    def md_valid():
        first=mdl.get()
        if len(first)==0:
            msg7.config(text="company name is must")
        else:
            try:
                if any(ch.isdigit() for ch in first):
                    msg7.config(text="it cannot contain digit!")
                elif len(first)<=2:
                    msg7.config(text="lenght is too small!")
                elif len(first)>12:
                    msg7.config(text="Huge name!")
                else:
                    msg7.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    #aadhar validation
    def ad_valid():
        first=lin.get()
        if len(first)==0:
            msg8.config(text="aadharcard number is must")
        else:
            try:
                if any(ch.isalpha() for ch in first):
                    msg8.config(text="it cannot contain alphabet!")
                elif len(first)<12:
                    msg8.config(text="must be of 12 digits!")
                elif len(first)>12:
                    msg8.config(text="invalid number!")
                else:
                    msg8.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True
    
    def val_reset():
        msg.config(text="")
        msg1.config(text="")
        msg2.config(text="")
        msg3.config(text="")
        msg4.config(text="")
        msg5.config(text="")
        msg6.config(text="")
        msg7.config(text="")
        msg8.config(text="")

    #Main screen inputs
    display_frame=Frame(menuframe,height=300,width=500,bd=5,relief=RIDGE)
    display_frame.place(x=700,y=10)
    display_text=Text(display_frame,height=18,width=50)
    display_text.grid(row=0,column=0)

    detail_1 =Label(menuframe,text="1.) BASIC INFORMATION OF INDIVIDUAL:-",font="timesnewroman 12 bold")
    first_name =Label(menuframe,text="First name*",font="bold")
    last_name =Label(menuframe,text="Last name*",font="bold")
    middle_name =Label(menuframe,text="Middle name*",font="bold")
    phnumber =Label(menuframe,text="Phone number*",font="bold")
    address =Label(menuframe,text="Address:",font="timesnewroman 12 bold")
    ad1 =Label(menuframe,text="House number/House name",font="bold")
    ad2 =Label(menuframe,text="Area",font="bold")
    ad3 =Label(menuframe,text="Pincode*",font="bold")
    ad4 =Label(menuframe,text="City*",font="bold")

    detail_2 =Label(menuframe,text="2.) VEHICAL INFORMATION:-",font="timesnewroman 12 bold")
    company =Label(menuframe,text="Company*",font="bold")
    model =Label(menuframe,text="Model name*",font="bold")
    showroom_name =Label(menuframe,text="Showroom name",font="bold")
    licesnce_number =Label(menuframe,text="Aadharcard number*",font="bold")

    detail_1.grid(ipadx=5,ipady=2)
    first_name.grid(row=1,ipadx=5,ipady=2)
    last_name.grid(row=2,ipadx=5,ipady=2)
    middle_name.grid(row=3,ipadx=5,ipady=2)
    phnumber.grid(row=4,ipadx=5,ipady=2)
    address.grid(row=5,ipadx=5,ipady=2)
    ad1.grid(row=6,ipadx=5,ipady=2)
    ad2.grid(row=7,ipadx=5,ipady=2)
    ad3.grid(row=8,ipadx=5,ipady=2)
    ad4.grid(row=9,ipadx=5,ipady=2)
    detail_2.grid(row=10,ipadx=5,ipady=2)
    Label(menuframe,text="Which type of vehicle you own ?*",font="bold").grid(row=11,ipadx=5,ipady=2)

    fn=StringVar()
    ln=StringVar()
    mn=StringVar()
    phnum=StringVar()
    a1=StringVar()
    a2=StringVar()
    a3=StringVar()
    a4=StringVar()
    
    var=StringVar()
    cmp=StringVar()
    mdl=StringVar()
    sn=StringVar()
    lin=StringVar()

    fn_entry= Entry(menuframe,textvariable=fn,validate="focusout",validatecommand=fn_valid)
    msg=Label(menuframe,text="",fg="red")
    ln_entry= Entry(menuframe,textvariable=ln,validate="focusout",validatecommand=ln_valid)
    msg1=Label(menuframe,text="",fg="red")
    mn_entry= Entry(menuframe,textvariable=mn,validate="focusout",validatecommand=mn_valid)
    msg2=Label(menuframe,text="",fg="red")
    ph_entry= Entry(menuframe,textvariable=phnum,validate="focusout",validatecommand=ph_valid)
    msg3=Label(menuframe,text="",fg="red")
    a1_entry= Entry(menuframe,textvariable=a1)
    a2_entry= Entry(menuframe,textvariable=a2)
    a3_entry= Entry(menuframe,textvariable=a3,validate="focusout",validatecommand=pin_valid)
    msg4=Label(menuframe,text="",fg="red")
    a4_entry= Entry(menuframe,textvariable=a4,validate="focusout",validatecommand=ct_valid)
    msg5=Label(menuframe,text="",fg="red")
    cmp_entry= Entry(menuframe,textvariable=cmp,validate="focusout",validatecommand=cm_valid)
    msg6=Label(menuframe,text="",fg="red")
    mdl_entry= Entry(menuframe,textvariable=mdl,validate="focusout",validatecommand=md_valid)
    msg7=Label(menuframe,text="",fg="red")
    sn_entry= Entry(menuframe,textvariable=sn)
    lin_entry= Entry(menuframe,textvariable=lin,validate="focusout",validatecommand=ad_valid)
    msg8=Label(menuframe,text="",fg="red")

    fn_entry.grid(row=1,column=2)
    msg.grid(row=1,column=3)
    ln_entry.grid(row=2,column=2)
    msg1.grid(row=2,column=3)
    mn_entry.grid(row=3,column=2)
    msg2.grid(row=3,column=3)
    ph_entry.grid(row=4,column=2)
    msg3.grid(row=4,column=3)
    a1_entry.grid(row=6,column=2)
    a2_entry.grid(row=7,column=2)
    a3_entry.grid(row=8,column=2)
    msg4.grid(row=8,column=3)
    a4_entry.grid(row=9,column=2)
    msg5.grid(row=9,column=3)

    radio=Radiobutton(menuframe,text="Scooter",variable=var,value="Scooter",font="bold").grid(row=12,column=0,ipadx=5,ipady=2)
    radio=Radiobutton(menuframe,text="Bike",variable=var,value="Bike",font="bold").grid(row=12,column=1,ipadx=5,ipady=2)
    radio=Radiobutton(menuframe,text="Car",variable=var,value="Car",font="bold").grid(row=12,column=2,ipadx=5,ipady=2)
    radio=Radiobutton(menuframe,text="Truck",variable=var,value="Truck",font="bold").grid(row=12,column=3,ipadx=5,ipady=2)

    company.grid(row=13,ipadx=5,ipady=2)
    model.grid(row=14,ipadx=5,ipady=2)
    showroom_name.grid(row=15,ipadx=5,ipady=2)
    licesnce_number.grid(row=16,ipadx=5,ipady=2)

    cmp_entry.grid(row=13,column=2)
    msg6.grid(row=13,column=3)
    mdl_entry.grid(row=14,column=2)
    msg7.grid(row=14,column=3)
    sn_entry.grid(row=15,column=2)
    lin_entry.grid(row=16,column=2)
    msg8.grid(row=16,column=3)
    mand=Label(menuframe,text="Feilds with * are mandatory .",fg="red").grid(row=17,column=0)
        
#number plate generator
    number_plate=StringVar()
    number_plate_label = Label(display_frame, text=" ",font="bold")
    number_plate_label.grid(row=8,column=0)
    
    def generate_number_plate():
        if not fn.get():
            messagebox.showwarning("Missing Field", "First name is required.")
            return
        elif not ln.get():
            messagebox.showwarning("Missing Field", "Last name is required.")
            return
        elif not mn.get():
            messagebox.showwarning("Missing Field", "Middle name is required.")
            return
        elif not phnum.get():
            messagebox.showwarning("Missing Field", "Phone number is required.")
            return
        elif not a3.get():
            messagebox.showwarning("Missing Field", "Pincode is required.")
            return
        elif not a4.get():
            messagebox.showwarning("Missing Field", "City is required.")
            return
        elif not cmp.get():
            messagebox.showwarning("Missing Field", "Company name is required.")
            return
        elif not mdl.get():
            messagebox.showwarning("Missing Field", "Model name is required.")
            return
        elif not lin.get():
            messagebox.showwarning("Missing Field", "Aadharcard number is required.")
            return
        

        if a4.get()=="Vadodara" or a4.get()=="vadodara":
            num1="GJ-06"
        elif a4.get()=="Ahemdabad" or a4.get()=="ahemdabad":
            num1="GJ-01"
        elif a4.get()=="Rajkot" or a4.get()=="rajkot":
            num1="GJ-03"
        elif a4.get()=="Jamnagar" or a4.get()=="jamnagar":
            num1="GJ-10"
        elif a4.get()=="Anand" or a4.get()=="anand":
            num1="GJ-23"

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        number_plate.set(num1 + "-" + random.choice(letters) + random.choice(letters) + "-" + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers))
        number_plate_label.config(textvariable=number_plate)
        return
        
    def display_text_data():
        display_text.insert(END,f"Name:\t{fn.get(),mn.get(),ln.get()}\n")
        display_text.insert(END,f"Phone number:\t{phnum.get()}\n")
        display_text.insert(END,f"City:\t{a4.get()}\n")
        display_text.insert(END,f"Aadharcard number:\t{lin.get()}\n")
        display_text.insert(END,f"Vehicle type:\t{var.get()}\n")
        display_text.insert(END,f"Company and Model :\t{cmp.get(),mdl.get()}\n")

    #reset and next button (frame and button settings)
    button_frame=Button(root,height=1080,width=350,bd=4,relief=SUNKEN)
    button_frame.pack(anchor="nw",side="top")

    def clear_all():
        fn_entry.delete(0,END)
        ln_entry.delete(0,END)
        mn_entry.delete(0,END)
        ph_entry.delete(0,END)
        a1_entry.delete(0,END)
        a2_entry.delete(0,END)
        a3_entry.delete(0,END)
        a4_entry.delete(0,END)
        cmp_entry.delete(0,END)
        mdl_entry.delete(0,END)
        sn_entry.delete(0,END)
        lin_entry.delete(0,END)

    def clear_display():
        display_text.delete("1.0","end")
        number_plate_label.destroy()

    def new1():
        number_plate_label = Label(display_frame, text=" ",font="bold")
        number_plate_label.grid(row=8,column=0)

    def getvals():
        if not fn.get() or not ln.get() or not mn.get() or not phnum.get() or not a3.get() or not a4.get() or not cmp.get() or not lin.get() or not mdl.get():
            print("inproper details")
        else:
            print("submited form succesfully....")
            with open("abc2.txt","+a") as f:
                f.write(f"{fn.get(),mn.get(),ln.get(),phnum.get(),a4.get(),var.get(),number_plate.get()}\n")


#reset button 
    reset_but=Button(button_frame,text="RESET",height=2,width=20,font="serif 10 bold",bg="red",command=lambda:[clear_all(),clear_display(),val_reset(),new1()])
    reset_but.grid(row=0,column=1)

#submit button 
    sub_but=Button(button_frame,text="SUBMIT",height=2,width=20,font="serif 10 bold",bg="green",command=lambda:[display_text_data(),generate_number_plate(),getvals()])
    sub_but.grid(row=0,column=0)

#help desk 
def help():
    global helpframe
    if helpframe:
        helpframe.destroy()
    if menuframe:
        menuframe.destroy()
    if button_frame:
        button_frame.destroy()
    helpframe=Frame(root,height=1080,width=350,bd=10,relief=SUNKEN)
    helpframe.pack(fill=X,side=TOP)
    h1=Label(helpframe,text="HELP DESK",font="timesnewroman 24 bold")
    h1.pack(side=TOP)
    h2=Label(helpframe,text='''Welcome to the Help Desk for the Number Plate Generator Portal! We are here to assist you with
     \n any questions or  concerns you may have. Please take a moment to browse through the following lines
     \n to help address your queries:
     \nRemember, our goal is to ensure your satisfaction and help you maximize the functionality of the Number Plate Generator.
     \n Feel free to ask us anything you need; we're here to help!''',font="17")
    h2.pack(side=LEFT,padx=3,pady=4)

#about 
def about():
    global aboutframe
    if aboutframe:
        aboutframe.destroy()
    if menuframe:
        menuframe.destroy()
    if button_frame:
        button_frame.destroy()
    if helpframe:
        helpframe.destroy()
    aboutframe=Frame(root,height=1080,width=350,bd=10,relief=SUNKEN)
    aboutframe.pack(fill=X,side=TOP)
    abt1=Label(aboutframe,text='''Welcome to the Number Plate Generator Portal! I Dhairya Chawda and Mandar Nikam from Baroda tried
      \nto create this small mini project for our submisson .This was a crazy and a great opportunity
      \nfor us to try something new from zero Knowledge in this module.But still we were able to create 
      \nthis gui within 4 working days.Thank youu !!''',font="17")
    abt1.pack(side=LEFT,padx=3,pady=4)

def del_help_about():
    if helpframe:
        helpframe.destroy()
    if aboutframe:
        aboutframe.destroy()

def del_abt():
    if aboutframe:
        aboutframe.destroy()


#frames of left and right
mainframe=Frame(root,highlightbackground="black",highlightthickness=4,borderwidth=5,relief=SUNKEN)
mainframe.pack(fill=Y,side=LEFT)

#buttons on left side
menu_but=Button(mainframe,text="Menu",height=2,width=25,command=lambda:[menu_fun(),del_help_about()])
menu_but.grid(row=0,column=0)

help_but=Button(mainframe,text="Help?",height=2,width=25,command=lambda:[help(),del_abt()])
help_but.grid(row=1,column=0)

about_but=Button(mainframe,text="About",height=2,width=25,command=about)
about_but.grid(row=2,column=0)

exit_but=Button(mainframe,text="Exit",height=2,width=25,command=Exit_screen)
exit_but.grid(row=3,column=0)

root.mainloop()
