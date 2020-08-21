# Take the following Python code that stores a string: str = 'X-DSPAM-Confidence: 0.8475 '
# Use find and string slicing to extract the portion of the string after the colon character.
# Then, use the float function to convert the extracted string into a floating point number. 

initial_string = 'X-DSPAM-Confidence: 0.8475 '
space_index = initial_string.find(' ')
num_extracted = initial_string[19:27]
final_string = float(num_extracted.strip())
print(final_string)
