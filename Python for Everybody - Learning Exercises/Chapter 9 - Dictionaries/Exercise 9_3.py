# Write a program to read through a mail log (mbox-short.txt)
# Build and print a histogram using a dictionary to count how many messages have come from each email address.

filename = input('Enter a file name: ')
fhand = open(filename)
counts = dict()
email_list = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        continue
    elif line.startswith('From'):
        word_list = line.split()
        email_list.append(word_list[1])
for email in email_list:
    counts[email] = counts.get(email, 0) + 1
print(counts)
