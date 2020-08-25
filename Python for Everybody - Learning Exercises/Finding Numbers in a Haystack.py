# Write a program to read through and parse a file with text and numbers.
#   - Extract all the numbers in the file and compute their sum

import re

number_list = list()
count = 0

filename = input('Enter the name of a text file: ')
fhand = open(filename)

for line in fhand:
    line = line.rstrip()
    exp_result = re.findall('[0-9]+', line)
    if len(exp_result) == 0:
        continue
    count = count + 1
    for num in exp_result:
        number_list.append(int(num))

num_sum = sum(number_list)
print(num_sum)