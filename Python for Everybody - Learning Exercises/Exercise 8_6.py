# Rewrite the program that prompts the user for a list of numbers and prints the max and min of those numbers when the user enters "done" (Exercise 5.2)
# Write the program such that the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

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
max_value = str(max(values))
min_value = str(min(values))
print("Maximum: " + max_value)
print("Minimum: " + min_value)