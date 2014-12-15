
txtpath1=r"a.txt"
txtpath2=r"b.txt"
txtpath3=r"c.txt"
txtpath4=r"d.txt"

fpa=open(txtpath1)
fpb=open(txtpath2)
fpc=open(txtpath3)
fpd=open(txtpath4,"w")

#test

arrD=[]
for kkk in range(50):
    arrD.append(0)

def WriteD():
    for kkkk in arrD:
        fpd.write(str(kkkk))
        fpd.write(" ")
    fpd.write("\n")

arrC=[]
for linec in fpc.readlines():
    arrC.append(linec.replace("\n",""))

arrB=[]
for lineb in fpb.readlines():
    arrB.append(lineb.replace("\n",""))

for linea in fpa.readlines():
    flag=True
    linea=linea.replace("\n","")
    for i in range(len(arrB)):
        if arrB[i]==linea:
            print linea
            print arrB[i]
            print arrC[i]
            flag=False
            fpd.write(linea)
            fpd.write("\n")
            fpd.write(arrC[i])
            fpd.write("\n")
    if flag:
        print linea
        fpd.write(linea)
        fpd.write("\n")
        WriteD()
        
print "Done!"
fpa.close()
fpb.close()
fpc.close()
fpd.close()
