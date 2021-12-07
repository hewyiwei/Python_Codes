#HEW YI WEI MA08

counter = {}


while True:
    
    oFile = input("Please enter the file you want to open: ")

    try:
        myFile = open(oFile, "r")
        break

    except FileNotFoundError:
        print("File not found, try again.")

while True:
    
    nFile = input("Please enter the file you want to create: ")

    try:
        newFile = open(nFile, "w")
        break

    except FileNotFoundError:
        print("File not found, try again.")

lines = myFile.readlines()

for line in lines:
    words = line.split()
    for word in words:
        letterCount = len(word)
        for letter in word:
            if not letter.isalnum():
                letterCount -= 1
        if letterCount in counter:
            counter.update({letterCount:counter[letterCount] + 1})
        else:
            counter.update({letterCount:1})

print("Word Length    Word Count", file=newFile)
for a in sorted(counter):
    print("    ", a,"   ", "\t", counter[a], file=newFile)

myFile.close()
newFile.close()
        
        
