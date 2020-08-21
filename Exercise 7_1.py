# Write a program to read through a file and print the contents of the file, line by line, all in upper case

filename = input('Enter the name of a file: ') # Make sure to include the full directory, too!
fhand = open(filename)
for line in fhand:
    line = line.rstrip()
    print(line.upper())