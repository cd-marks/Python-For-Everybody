# Build on Exercise 9.3 to figure out who has the most messages in the mbox-short.txt file.
# After all the data has been created, look through the dictionary using a maximum loop
# Find who has the most messages and print how many messages that person has.

filename = input('Enter a file name: ')
fhand = open(filename)
counts = dict()
email_list = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        continue
    elif line.startswith('From'):
        line_list = line.split()
        email_list.append(line_list[1])

for email in email_list:
    counts[email] = counts.get(email, 0) + 1

max_person = None
max_amount = None
for person,amount in counts.items():
    if max_amount is None or amount > max_amount:
        max_person = person
        max_amount = amount

print (max_person, max_amount)