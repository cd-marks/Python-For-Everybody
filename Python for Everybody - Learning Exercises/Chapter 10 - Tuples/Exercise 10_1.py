# Revise a previous program (Exercise 9.3) as follows:
#   - Read and parse lines beginning with "From" and pull out the addresses from each line.
#   - Count the number of messages from each person using a dictionary.
#   - After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
#   - Then, sort the list in reverse order and print out the person who has the most commits.

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

sorted_count = sorted([(v, k) for k, v in counts.items()], reverse=True)
for v, k in sorted_count [0:1]:
    print(k, v)
