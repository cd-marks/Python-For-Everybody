# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print the total, count and average of the numbers entered.
# If the user enters anything other than a number, detect their mistake using try and except... 
# to print an error message and skip to the next number

count = 0
current_sum = 0
while True:
    current_value = input('Enter an integer: ')
    if current_value == 'done':
        break
    try:
        current_value = int(current_value)
    except:
        print("Invalid Input")
        continue
    count = count + 1
    current_sum = current_sum + current_value
average = current_sum / count
print(current_sum, count, average)
    
