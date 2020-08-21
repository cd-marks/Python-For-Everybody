# Rewrite your pay program (Exercise 3.1) using try and except so that your program handles non-numeric input gracefully.
# If a user enters a non-numeric input, print a message and exit the program.

try:
    hours = float(input('Enter hours worked this week: '))
    rate = float(input('Enter hourly pay rate: '))
    overtime_rate = rate * 1.5
    if hours > 40 :
        pay = str((40 * rate) + ((hours - 40) * (overtime_rate)))
    else:
        pay = str(hours * rate)
    print("This week's pay: $" + pay)
except:
    print('Error, please enter a numeric input')
