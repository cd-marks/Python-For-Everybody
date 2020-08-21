# Rewrite your grade program (Exercise 3.3) using a function called computegrade.
# computegrade should take a score as its parameter and return a grade as a string.

def computegrade (score):
    if score > 1.0:
        grade = "Bad Score"
    elif score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    elif score < 0.6:
        grade = "F"
    return grade
try: 
    score = float(input('Enter a score betweeen 0.0 and 1.0: '))
    grade_result = computegrade(score)
    print(grade_result)
except:
    print("Bad score")
