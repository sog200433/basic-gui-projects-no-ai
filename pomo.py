from tkinter import *
from datetime import *
import time
from tkinter import messagebox



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #




class Pomodoro:
    def __init__(self):
        self.window=Tk()
        self.window.title("Pomodoro Timer")
        self.window.geometry("500x500")
        self.window.config(bg="black")
        

        #create the values of the minutes and seconds string vars 


        #then we want to set them to empty zero
     


        name=Label(self.window,text="Pomodoro Timer",fg="red",bg="black",font=("arial",30))
        name.pack(pady=10)
        self.canvas=Canvas(width=200,height=250,highlightthickness=0,bg="black")
        self.tomatato_img=PhotoImage(file="tomato.png")
        self.canvas.create_image(100,120,image=self.tomatato_img)
        self.timer_text=self.canvas.create_text(95,140,text="00:00",font=("arial",15))
        self.canvas.pack(pady=25)
        start=Button(self.window,text="start",fg="white",bg="red",font=("arial",15),width=6,height=3,command=self.start_time)
        start.place(x=80,y=360)
        reset=Button(self.window,text="Reset",fg="white",bg="red",font=("arial",15),width=6,height=3,command=self.reset)
        reset.place(x=350,y=360)
        self.check_mark=Label(self.window,text=None)
        self.check_mark.place(x=240,y=370)
        self.window.mainloop()
    def reset(self):
        self.window.after_cancel(timed_down)
        self.canvas.itemconfig(self.timer_text,text="00:00")
        
      
      
    def start_time(self,time_now=1500):
        global timed_down
        new_text=''
        if time_now>-1:
            min,sec=divmod(time_now,60)
            new_val=f"{min:02d}:{sec:02d}"
            self.canvas.itemconfig(self.timer_text,text=new_val)
            timed_down=self.window.after(1000,self.start_time,time_now-1)
        elif time_now==0:
            new_text+="✅"
            self.check_mark.config(text=new_text)
            
        else:
            messagebox.showinfo("timer","time is up ")
         
      


        
   


Pomodoro()