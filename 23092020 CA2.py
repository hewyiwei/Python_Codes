# Hew Yi Wei Group MA8

aStr = input ("Enter a string: ")
subStr = input ("Enter a substring: ")
subLen = len (subStr)
iCoun = -1

# print (subLen)

if subStr in aStr:

    print ("Yes.")

for n in aStr:

    iCoun += 1

    for m in subStr:

        if n == m:

            if subStr == aStr[iCoun:iCoun + subLen + 1]:

                print (aStr[iCoun:iCoun + subLen + 1])

                print (iCoun)

                break


        else:

            break

    

            

            

                

                

                



                    
