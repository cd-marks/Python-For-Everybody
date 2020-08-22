# Write a program that reads a file and prints the letters in decreasing order of frequency.
#   - Convert all the input to lower case and only count the letters a-z.
#   - Do not count spaces, digits, punctuation or anything other than the letters a-z.

filename = input('Enter a file name: ')
fhand = open(filename)
counts = dict()

words = fhand.read()
words = words.lower()

letter_list = list()
for i in words:
    if i.isalpha() == True:
        letter_list.append(i)

for letter in letter_list:
    counts[letter] = counts.get(letter, 0) + 1

sorted_count = sorted([(v, k) for k, v in counts.items()], reverse=True)
for v, k in sorted_count:
    print(k, v)
