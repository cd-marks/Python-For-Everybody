# Write a program that categorizes each mail message by which day of the week the commit was done (using mbox-short.txt).
# To do this, look for lines that start with "From", then look for the third word and keep a running count of each day of the week on each line.
# At the end of the program, print out the contents of the dictionary (order does not matter)

filename = input('Enter a file name: ')
fhand = open(filename)
counts = dict()
day_list = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        continue
    elif line.startswith('From'):
        line_list = line.split()
        day_list.append(line_list[2])
for day in day_list:
    counts[day] = counts.get(day, 0) + 1
print(counts)