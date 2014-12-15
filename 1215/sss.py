import os

shpPath= r"C:\Users\Administrator\Desktop\thesis"


print "************************HT*****************************"
add=[]
for r,ds,fs in os.walk(shpPath):
    for f in fs:
        print f[3:-4]
#os.startfile(shpPath)
