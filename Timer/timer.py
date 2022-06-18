import time
import datetime

h= input("Enter Hours   :")
while h!= "" and not h.isdigit() :     h= input("Please Enter valid Hours \nEnter Hours   :")
m= input("Enter Minutes :")
while m!= "" and not m.isdigit() :     m= input("Please Enter valid Minutes \nEnter Minutes :")
s= input("Enter Seconds :")
while s!= "" and not s.isdigit() :     s= input("Please Enter valid Seconds \nEnter Seconds :")
if h=="":h=0
if m=="":m=0
if s=="":s=0

def countDown(h,m,s):
    totalSeconds = h*3600 + m*60 + s
    while totalSeconds>0:
        timer = datetime.timedelta(seconds=totalSeconds)
        print(timer,end="\r")
        time.sleep(1)
        totalSeconds-=1

    print("Time is up!!!")



countDown(int(h),int(m),int(s))