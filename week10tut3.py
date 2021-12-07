for reciA in range (-10,11):
    if reciA == 0:
        print ("Infinity")
    else:
        print(round(1/reciA, 2))

print()

for reciB in range (-10,11):
    try:
        print(round(1/reciB, 2))
    except ZeroDivisionError:
        print ("Infinity")
        
