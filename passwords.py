from tkinter import *
from tkinter import ttk

from tkinter import messagebox




class password:
    def __init__(self):
        self.window=Tk()
        self.window.config(background="black")
        self.window.title("Password Manager")
        self.window.geometry("700x700")


        canvas=Canvas(width=200,height=200,highlightthickness=0,background="black")
        img=PhotoImage(file="logo.png")
        canvas.create_image(80,120,image=img) 
        canvas.grid(row=0,column=1,pady=10)
        web=Label(self.window,text="Website:",font=("arial",20),fg="red",bg="black",highlightthickness=0)
        web.grid(row=1,column=0,pady=10,padx=10)
        self.webentry=Entry(self.window,border=3,font=("arial",20),highlightthickness=3,highlightcolor="red")
        self.webentry.grid(row=1,column=1,pady=10)
        self.email=Label(self.window,text="Email/Username:",font=("arial",20),fg="red",bg="black",highlightthickness=0)
        self.email.grid(row=2,column=0,pady=10)
        self.email_entry=Entry(self.window,border=3,font=("arial",20),highlightthickness=2,highlightcolor="red")
        self.email_entry.grid(row=2,column=1,pady=10)
        row3frame=Frame(self.window,highlightthickness=0,background="black",width=500,height=100)
        self.password=Label(row3frame,text="Password:",font=("arial",20),fg="red",bg="black",padx=10,highlightthickness=0)
        self.password.grid(row=0,column=0,padx=20)
        self.password_entry=Entry(row3frame,border=3,font=("arial",20),text=" ",highlightthickness=2,highlightcolor="red",width=10)
        self.password_entry.grid(row=0,column=1,padx=8,sticky="w")
        generate=Button(row3frame,text="Generate Password",command=self.Saveas,width=17,bg="red",fg="black",font=("arial",15))
        generate.grid(row=0,column=2,padx=10,sticky="w")
        row3frame.grid(row=3,columnspan=3)
        self.window.mainloop()
    def Saveas(self):
        
        with open("passwordsaving.txt","a") as pw:
            information=f"[Website:{self.webentry.get()}, Email:{self.email_entry.get()} ,Password:{self.password_entry.get()}]"
            while True:
                print("the file is not empty")
                pw.write(information)
                print("the file has been filled with your password")
                messagebox.showinfo("Password  succesfully added",information)
                break
            self.webentry.delete(0,"end")  
            self.email_entry.delete(0,"end") 
            self.password_entry.delete(0,"end")

        
        
        
password()
                                                                           