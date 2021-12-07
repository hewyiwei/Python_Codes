# Hew Yi Wei Group MA8

tmath = 0
tphy = 0
studAvg = 0
mathAvg = 0
phyAvg = 0
studCount = 1

def studentGrade (ave):
    if ave < 50:
        grade = 'F'
    elif 50 <= ave < 60:
        grade = 'D'
    elif 60 <= ave <= 70:
        grade = 'C'
    elif 70 <= ave <= 80:
        grade = 'B'
    elif 80 <= ave <= 100:
        grade = 'A'
    
while True:
    
    print ("Student ", studCount)
    math = float (input ("Enter maths score: "))
    phy = float (input ("Enter physics score: "))

    if 0 > math > 100 or 0 > phy > 100:
        print ("Please print valid score.")
        continue
    
    tmath += math
    tphy += phy
    studCount += 1
    
    studAvg = (math + phy)/2

    if studAvg < 50:
        grade = 'F'
    elif 50 <= studAvg < 60:
        grade = 'D'
    elif 60 <= studAvg <= 70:
        grade = 'C'
    elif 70 <= studAvg <= 80:
        grade = 'B'
    elif 80 <= studAvg <= 100:
        grade = 'A'
    print ("Average: ", studAvg, "Grade: ", grade)

    more = str (input ("Any more students? "))

    if more == 'Y' or more == 'y':
        continue
    else:
        break

mathAvg = tmath/(studCount - 1)
phyAvg = tphy/(studCount - 1)

print ("Class average: Maths {}, Physics {}".format (mathAvg, phyAvg))
        

    

