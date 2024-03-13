year1=int(input("Enter a start year(Ex: 2002):"))
month1=int(input("Enter a start month(Ex: 08):"))
day1=int(input("Enter a start day(Ex: 13):"))

year2=int(input("Enter a end year(Ex: 2002):"))
month2=int(input("Enter a end month(Ex: 08):"))
day2=int(input("Enter a end day(Ex: 13):"))

if year1>year2:
    print("invalid date (The begining date year is after the end date year)")
elif year1==year2 and month1>month2:
    print("invalid date (The begining date month is after the end date month)")
elif  year1==year2 and month1>month2 and day1>day2:
    print("invalid date (The begining date day is after the end date day)")
else:
    print("Correct dates!") 