from ast import Break
from tkinter import *
from tkinter import ttk,messagebox
import time
from turtle import color

root= Tk()
hour=StringVar()
minute=StringVar()
second=StringVar()
root.title = "Timer"
root.geometry('{}x{}'.format(500, 250))
Progressbar = ttk.Progressbar()
Progressbar.pack(fill=X)
frameFiller= Frame(root,width=500,height=50)
frameFiller.pack()
frameX= Frame(root,width=500)
frameX.pack()

tbhours = Entry(frameX,font=('Arial',48,'bold'),width=2,textvariable=hour,justify='center')
tbhours.pack(side=LEFT)
tbhours.insert(0,0)
label1 = Label(frameX, text="  :  ")
label1.pack(side=LEFT)
tbminutes = Entry(frameX,font=('Arial',48,'bold'),width=2,textvariable=minute,justify='center')
tbminutes.pack(side=LEFT)
tbminutes.insert(0,0)
label2 = Label(frameX, text="  :  ")
label2.pack(side=LEFT)
tbseconds = Entry(frameX,font=('Arial',48,'bold'),width=2,textvariable=second,justify='center')
tbseconds.pack(side=LEFT)
tbseconds.insert(0,0)
frame2=Frame(root,bg="BLACK",width=500,height=100)
frame2.pack(side=BOTTOM)

def countdowntimer():
    if StartBtn["bg"] == "Green":
        

        #try:
        if hour.get().isdigit() and minute.get().isdigit() and second.get().isdigit():
            
            TotalSeconds = int(hour.get())*3600 +  int(minute.get())*60 + int(second.get())
            TotalSecondsSaved = TotalSeconds
            progressVal=0
            tbhours.config (state= "disabled")
            tbminutes.config (state= "disabled")
            tbseconds.config (state= "disabled")
            StartBtn.config(bg="Yellow",text="Pause Timer")
                    
            #except:
                #print("Please input the right value")

            while TotalSeconds>=0 and StartBtn["bg"]=="Yellow" :
                mins,secs = divmod(TotalSeconds,60)
                hours=0
                hours,mins = divmod(mins,60)
                hour.set("{0:1d}".format(hours))
                minute.set("{0:1d}".format(mins))
                second.set("{0:1d}".format(secs))
                Progressbar['value'] =progressVal*100/TotalSecondsSaved             
                root.update()
                if (TotalSeconds == 0):

                    tbhours.config (state= "normal")
                    tbminutes.config (state= "normal")
                    tbseconds.config (state= "normal")
                    StartBtn.config(bg="Green",text="Start Timer") 
                    messagebox.showinfo("Time Countdown", "Time's up ")               
                # after every one sec the value of temp will be decremented
                # by one
                TotalSeconds -= 1
                time.sleep(1)
                progressVal+=1


        else:
            messagebox.showinfo("Error","Please input the right value")
    else:
            StartBtn.config(bg="Green",text="Start Timer")    
            tbhours.config (state= "normal")
            tbminutes.config (state= "normal")
            tbseconds.config (state= "normal")
              

StartBtn = Button(frame2,text="Start Timer",bg="Green",command=countdowntimer)
StartBtn.pack(fill=BOTH,expand=True,ipadx=500,ipady=15)



root.mainloop()