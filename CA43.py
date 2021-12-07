#Hew Yi Wei MA08

i = 0
f = 0
e = 0

while True:
    
    oFile = input ("Please enter the name of the file to open: ")

    try:
        inFile = open(oFile, "r")
        break

    except FileNotFoundError:
        print ("Please try again.")

while True:
    
    cFile = input ("Please enter the name of the file to create: ")

    try:
        outFile = open(cFile, "w")
        break

    except FileNotFoundError:
        print ("Please try again.")
        
#lines = inFile.readlines()

for line in inFile:
    values = line.split(",")
    for value in values:
        try:
            testVal = float(value)
            testNum = value.split(".")
            
            if testNum[1] == "0":
                i += 1
            else:
                f += 1
        except ValueError:
            e += 1
        

outFile.write("Number of Integers: {}\nNumber of Float: {}\nNumber of Errors: {}".format(i, f, e))

inFile.close()
outFile.close()

            

