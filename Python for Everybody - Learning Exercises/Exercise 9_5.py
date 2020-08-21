# Build upon Exercise 9.3 by building and printing a dictionary based on the email domain name, rather than the entire email address that each message was sent from.

filename = input('Enter a file name: ')
fhand = open(filename)
counts = dict()
domain_list = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        continue
    elif line.startswith('From'):
        word_list = line.split()
        email_list = word_list[1]
        domain_split = email_list.split('@')
        domain_list.append(domain_split[1])
for domain in domain_list:
    counts[domain] = counts.get(domain, 0) + 1
print(counts)