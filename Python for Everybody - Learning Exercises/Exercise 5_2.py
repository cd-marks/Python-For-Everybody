# Write a program based on the same funcationality as Exercise 5.1, except it prints both the maximum and minimum numbers instead of the average

count = 0
num_sum = 0
values = []
while True:
    current_value = input('Enter an integer: ')
    if current_value == 'done':
        break
    try:
        current_value = int(current_value)
    except:
        print("Invalid Input")
        continue
    values.append(current_value)
    num_sum = num_sum + current_value
    count = count + 1
count = str(count)
num_sum = str(num_sum)
min_value = str(min(values))
max_value = str(max(values))
print("The amount of individual numbers entered is "+ count)
print("The sum of these numbers is " + num_sum) 
print("The minimum value is " + min_value)
print("The maximum value is " + max_value)
