
#Input networks/ set up stored info
#Constantly running
#Pings each network
#Records if down in log and console (time, date, network name)

import time
import pythonping
import datetime
import os
from pythonping import ping

networksPath = "Files/Networks.txt"
logPath = "Files/Log.txt"
tempPath = "Files/Temp.txt"

def inputFunc():
    global networksInput
    networksInput = input ("Input your networks separated by commas\n")
    networksInput = networksInput.split(",")
    linesLength2 = len(networksInput)
    count = 0
    file = open(networksPath,"w")
    while count < linesLength2:
        file.write(networksInput[count])
        file.write(",")
        count+=1
    file.close()

savedNetworks = open(networksPath,"r")
lines = savedNetworks.readlines()
linesLength = len(lines)
savedNetworks.close()
if linesLength == 0:
    inputFunc()
else:
    changeNetworksChoice = input("Would you like to change your current networks?\nEnter Yes or No\n")
    if changeNetworksChoice.lower() == "yes":
        inputFunc()

savedNetworks = open(networksPath,"r")
lines2 = savedNetworks.readlines()
lines2 = str(lines2)
lines2 = lines2.split(",")
lines2Length = len(lines2)
temp = lines2Length-1
lines2.remove(lines2[temp])
temp = lines2[0]
temp=temp.replace("[","")
temp=temp.replace("'","")
lines2[0]=temp
lines2Length = len(lines2)

x=False
while x == False:
    count = 0
    while count < lines2Length:
        tempFile = open(tempPath,"w")
        ping(lines2[count],verbose=True,out=tempFile)
        tempFile.close()
        tempFile = open(tempPath,"r")
        lines3 = tempFile.readlines()
        tempFile.close()
        print(lines3)
        print("\n")
        lines3Length = len(lines3)
        count2=0
        while count2 < lines3Length:
            if lines3[count2] == "Request timed out\n":
                logFile = open(logPath,"a")
                currentTime=str(datetime.datetime.now())
                temp = currentTime + " " + lines2[count] + " Request timed out" + "\n" + "\n"
                logFile.write(temp)
                logFile.close()
                count2+=1
            else:
                count2+=1
        count+=1
    time.sleep(10)