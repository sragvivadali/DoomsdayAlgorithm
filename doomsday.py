isLeapYear = False
isJulian = False

importantDates = [[3, 4], [0, 1], 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

date = input("Insert Date in MM/DD/YYYY format: ")

month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:])

if year < 1584:
    isJulian = True

if year % 4 == 0:
    isLeapYear = True

c = int(year / 100)
y = int(year % 100)

if not isJulian:
    anchor = ((5 * (c % 4)) % 7 + 2) % 7
else: 
    anchor = (6 * c) % 7

startDate = ((int(y / 12) + (y % 12) + int((y % 12) / 4)) % 7 + anchor) % 7

if month == 1 or month == 2:
    if isLeapYear:
        doomsday = importantDates[month - 1][1]
    else:
        doomsday = importantDates[month - 1][0]
else:
    doomsday = importantDates[month - 1]

dayDifference = day - doomsday

dayOfWeek = (startDate + dayDifference) % 7

print(f"The day of the week is {daysOfWeek[dayOfWeek]}.")
