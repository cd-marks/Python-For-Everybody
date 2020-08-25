# Write a program to prompt the user to enter a file name and look for lines of the form "New Revision: 39772".
#   - Extract the number from each of the lines using a regular expression and the findall() method.
#   - Compute the average of the numbers and print this average as an integer

import re
import statistics

number_list = list()

filename = input('Enter the name of a text file: ')
fhand = open(filename)

for line in fhand:
    line = line.rstrip()
    exp_result = re.findall('New Revision: ([0-9]+)', line)
    if len(exp_result) != 1:
        continue
    extracted_num = int(exp_result[0])
    number_list.append(extracted_num)

avg_result = statistics.mean(number_list)
print(int(avg_result))