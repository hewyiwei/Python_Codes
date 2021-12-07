# Hew Yi Wei Group MA8

count = 0

day = int (input ("Which day of the week is the first of the month? "))

print ("The calendar: ", "Mon   Tue   Wed   Thu   Fri   Sat   Sun", sep = '\n')

print ("      " * (day - 1), end = '')

count += (day - 1)

for date1 in range (1, (8 - count)):

    print (date1, end = '     ')

print ()

for date2 in range ((8-count), (8-count)+7):

    print (date2, end = '     ')
        
print ()

for date3 in range ((8-count)+7, (8-count)+7+7):

    print (date3, end = '     ')

print ()

for date4 in range ((8-count)+7+7, (8-count)+7+7+7):

    print (date4, end = '     ')

print ()

for date5 in range ((8-count)+7+7+7, (8-count)+7+7+7+7):

    if date5 > 30:

        break

    print (date5, end = '     ')
