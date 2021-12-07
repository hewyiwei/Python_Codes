# MA1008 CA 2 Question D
# Print the calendar of a specific month
# This programs does more than required by the question - it asks for the
# month from the user and then works out the number of days before printing
# instead assuming the number of days is known

# define the number of days in the different months in a list
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input("The month: "))
weekday = int(input("Which day of the week is the first of the month? "))

# first print the days in the week, with 5 character spaces for each day
print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")

# print leading spaces in first row, 5 per day
print("     "*(weekday-1), end = "")

days_in_month = month_days[month-1]
for i in range(1, days_in_month+1):  # go through each day
    print(" {:>2d}  ".format(i), end = "") # print the day, right justified
                                           # be careful with the number of spaces
    if (i+weekday-1)%7 == 0:   # new line after the 7th column
       print()
