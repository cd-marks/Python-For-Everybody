# Write a program to read through mail box data (using mbox-short.txt).
# When you find a line that starts with "From", split the line into words using the split function.
# (We are interested in who sent the message, which is the second word on the "From" line)
# Parse the From line and print out the second word for each "From" line.
# Then, count and print the number of "From" (not "From:") lines.

filename = input('Enter the name of a file: ') # Make sure to include the full directory, too!
fhand = open(filename)
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        count = count + 1
        line_list = line.split()
        print(line_list[1])
print("There were " + str(count) + " lines in the file with From as the first word")