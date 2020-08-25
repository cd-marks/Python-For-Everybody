# Write a program to simulate the operation of the grep command in Linux.
#   - Ask the user to enter a regular expression
#   - Count the number of lines that matched the regular expression they entered

import re

count = 0
filename = input('Enter the file name mbox.txt: ')
reg_express = input('Enter a regular expression: ')
fhand = open(filename)

for line in fhand:
    line = line.rstrip()
    exp_result = re.findall(reg_express, line)
    if len(exp_result) != 1:
        continue
    count = count + 1

print("mbox.txt had " + str(count) + " lines that matched " + reg_express)
