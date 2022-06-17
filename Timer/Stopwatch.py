import time

starttime = time.time()
prevtime = starttime
lapNumber = 1
UserInput = ""
print("Timer Begins! \nPress Q and then press ENTER to stop the code")
#Press Q and then press ENTER to stop the code
while UserInput.lower() != "q" :
    UserInput=input()
    tempTime = time.time()
    print("Lap time : ",round(tempTime- prevtime,2))  #Prints Lap time
    print("Total time : ",round(tempTime - starttime,2))  #Prints Total time
    print("lap number :",lapNumber)
    lapNumber+=1
    prevtime = tempTime

print("="*25)
    