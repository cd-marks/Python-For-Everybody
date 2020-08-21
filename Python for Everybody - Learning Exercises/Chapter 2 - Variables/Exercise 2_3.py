# Problem: Write a program to prompt the user for hours and rate per hour to compute gross pay

hours = float(input('Enter hours worked this week: '))
rate = float(input('Enter hourly pay rate: '))
pay = str(hours * rate)
print("This week's pay: $" + pay)
