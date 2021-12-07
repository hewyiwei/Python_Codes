# Hew Yi Wei Group MA8

peopleCounter = 1
sen = 0
adu = 0
you = 0
chi = 0
totalAge = 0
aveAge = 0
aveCat = 0

while True:

    while True:

        age = int (input ("Enter age of Person {}: ".format(peopleCounter)))

        if age <= 115:

            break

        else:

            print ("Invalid age. Please try again.")

    if age < 0:

        print ("Input completed.")
        break

    elif age >= 60:

        sen += 1

    elif 21 <= age <= 59:

        adu += 1

    elif 11 <= age <= 20:

        you += 1

    elif age < 11:

        chi += 1

    totalAge += age
    peopleCounter += 1

aveAge = totalAge/(peopleCounter-1)

if aveAge >= 60:

    aveCat = "Senior"

elif 21 <= aveAge <= 59:

    aveCat = "Adult"

elif 11 <= aveAge <= 20:

     aveCat = "Youth"

elif aveAge < 11:

     aveCat = "Child"

print("Number of people: ", peopleCounter-1)
print("Number of Seniors: ", sen)
print("Number of Adults: ", adu)
print("Number of Youths: ", you)
print("Number of Children: ", chi)
print("The average person is at age {:.2f}, {}".format(aveAge, aveCat))
