counter = 0

newFile = input("Please enter thje name of the new file: ")

workFile = open(newFile, "w")

noOfCol = int(input("Please enter the number of columns: "))

for lines in range (128):
    if not chr(lines).isprintable():
        continue
    print("{:<5d}{:>5s}".format(lines ,chr(lines)), end = "   |  ", file=workFile)
    counter += 1
    if counter == noOfCol:
        print(file=workFile)
        counter = 0

workFile.close()


    
        
