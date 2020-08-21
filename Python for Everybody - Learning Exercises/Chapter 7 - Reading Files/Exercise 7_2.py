# Write a program to prompt the user for a file name, then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:", pull apart the line to extract the floating-point number on the line.
# In addition, count these lines and compute the total of the spam confidence values from these line.
# Finally, compute and print the average spam confidence value when you reach the end of the file.

filename = input('Enter the name of a file: ') # Make sure to include the full directory, too!
fhand = open(filename)
count = 0
float_total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        space_index = line.find(' ')
        num_segment = line[space_index:len(line)]
        line_float = float(num_segment.strip())
        float_total = float_total + line_float
avg_confidence = float_total / count
print("Average spam confidence: " + str(avg_confidence))
