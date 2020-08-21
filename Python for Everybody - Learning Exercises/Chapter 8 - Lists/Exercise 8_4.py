# Write a program to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in the list. IF the word is not in a list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

unique_words = []
filename = input('Enter the name of a file: ') # Make sure to include the full directory, too!
fhand = open(filename)
for line in fhand:
    line = line.rstrip()
    # line = line.lower()
    line_list = line.split()
    for word in line_list:
        if word not in unique_words:
            unique_words.append(word)
unique_words.sort()
print(unique_words)
            
