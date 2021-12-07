# Hew Yi Wei Group MA8

import math

num = 3

den = 3

ansPower = 2

counter = 2

finalDen = 1

x = int (input ("Enter the angle (in radians): "))

while abs(ansPower) < 1e-8:

    for a in range (1, den + 1):
        den *= a

    if counter%2 == 0:
        finalDen = 0 - den

    counter += 1

    #print (den)


    ansPower += (x**num)/(finalDen)

    #print (ansPower)

    num += 2

    den += 2

    #print (den)

ansImport = math.sin(x)

if ansPower == ansImport:
    com = 'The two values are equal.'

else:
    com = 'The two values are not equal.'

print ('Power Series: sin({}) = {:.8f}'.format(x, ansPower))

print ('Python Library: sin({}) = {:.8f}'.format(x, ansImport))

print (com)
