# Rewrite your pay computation program (Exercise 2.3) to give the employee 1.5 times the hourly rate for hours worked above 40 hours

hours = float(input('Enter hours worked this week: '))
rate = float(input('Enter hourly pay rate: '))
overtime_rate = rate * 1.5
if hours > 40 :
    pay = str((40 * rate) + ((hours - 40) * (overtime_rate)))
else:
    pay = str(hours * rate)
print("This week's pay: $" + pay)