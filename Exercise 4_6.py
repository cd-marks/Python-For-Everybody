# Rewrite your pay computation program with time-and-a-half for overtime (Exercise 3.2).
# Create a function called computepay which takes two parameters (hours and rate)

try:
    hours = float(input('Enter hours worked this week: '))
    rate = float(input('Enter hourly pay rate: '))
    overtime_rate = rate * 1.5
    def computepay (hours, rate):
        if hours > 40 :
            pay = (40 * rate) + ((hours - 40) * (overtime_rate))
        else:
            pay = hours * rate
        return pay
    pay_value = str(computepay(hours, rate))
    print("This week's pay: $" + pay_value)
except:
    print('Error, please enter a numeric input')
