# MA1008 CA2 Question A
# Counting people in four groups

seniors = 0  # initialise the number in the four groups
adults = 0
youths = 0
children = 0
total_age = 0   # total age of all the people, initialised to 0

while True: #Go round reading in ages
    while True:  # read the age, but repeat if age > 115
       age = int(input("Enter age of person: "))
       if age <= 115:
           break
       else:
           print("Age too large. Try again.")
    if age <= 0:
        break  # exit loop if age < 0
    
    if age >= 60:   # add according to group
        seniors += 1
    elif age >= 21:
        adults += 1
    elif age >= 11:
        youths += 1
    else:
        children += 1
        
    total_age += age

people = seniors+adults+youths+children
print("Input completed.")
print("Number of people: ", people)
print("Number of seniors: ", seniors)
print("Number of adults: ", adults)
print("Number of youths: ", youths)
print("Number of children: ", children)

average = total_age/people
print("The average person is at age {:5.2f}, ".format(average), end = "")

if average >= 60:   # catagorise
    print("senior.")
elif average >= 21:
    print("adult.")
elif average >= 11:
    print("youth.")
else:
    print("child.")
