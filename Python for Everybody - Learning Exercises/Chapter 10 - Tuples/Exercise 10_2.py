# Write a program similar to Exercise 10.1 which counts the distribution of the hour of the day for each email message.
#   - You can pull the hour from the "From" line by finding the time string and splitting it into two parts using the colon character.
#   - Once you've accumulated the counts for each hour, print the count, one-per-line, sorted by hour.

filename = input('Enter a file name: ')
fhand = open(filename)
counts = dict()
hour_list = list()

for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        continue
    elif line.startswith('From'):
        word_list = line.split()
        time_list = word_list[5]
        time_split = time_list.split(':')
        hour_list.append(time_split[0])

for hour in hour_list:
    counts[hour] = counts.get(hour, 0) + 1

sorted_count = sorted([(k, v) for k, v in counts.items()])
for k, v in sorted_count:
    print(k, v)
