fi = open("05-23-2020.csv","r")
fi.readline() # skip over first title line
datarows = fi.readlines()
fi.close()

fo = open("totaldead.txt","w")

total= 0

for line in datarows:
    templist = line.split(",")
    a= templist[8]
    a= float(a)
    a= int(a)
    total= total +(a)
    a= 0
       
fo.write (str(total))
 
     
fo.close()