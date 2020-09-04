def arithmetic_arranger(problems, solve = False):
    # Set up blank variables
    line1_list = list()
    line2_list = list()
    line3_list = list()
    line4_list = list()
    arranged_problems = ''

    # Checks if the number of problems entered is greater than 5
    if len(problems) > 5:
        return("Error: Too many problems.")

    for eq in problems:
        # Split each item in the problems list into its individual parts
        #   -> Operand 1, Operator and Operand 2
        eq_split = eq.split()

        # Checks if the problem contains non-numeric characters
        if eq_split[0].isnumeric() == False or eq_split[2].isnumeric() == False:
            return("Error: Numbers must only contain digits.")

        operand1 = eq_split[0]
        operator = eq_split[1]
        operand2 = eq_split[2]

        # Checks if an operator other than '+' or '-' is used
        if operator not in ('+', '-'):
            return ("Error: Operator must be '+' or '-'.")

        # Calculate the length of each operand
        operand_length1 = len(operand1)
        operand_length2 = len(operand2)
        
        # Checks if either the first or second operand is greater than 4 digits
        if operand_length1 > 4 or operand_length2 > 4:
            return("Error: Numbers cannot be more than four digits.")
        
        # Find the length of the longest operand; add 2 to account for operator and requirement of one space placed between the operator and largest operand
        eq_length = max(operand_length1, operand_length2) + 2

        # Arrange each problem vertically, separated by line
        # 4 spaces added to the end of each line to satisfy formatting requirement 
        eq_line1 = str.rjust(operand1, eq_length)
        eq_line2 = operator + str.rjust(operand2, eq_length-1)
        eq_line3 = ('-' * eq_length)
        

        # Append each line of each individual problem into a list
        line1_list.append(str(eq_line1))
        line2_list.append(str(eq_line2))
        line3_list.append(str(eq_line3))
       
        # If an argument is passed to calculate the solution to each problem,
        # perform the calculation and add the result to a list
        if solve == True:
            if operator == '+':
                solution = str(int(operand1) + int(operand2))
            elif operator == '-':
                solution = str(int(operand1) - int(operand2))
            eq_line4 = str.rjust(solution, eq_length)
            line4_list.append(str(eq_line4))


    # Adds the required formatting (4 spaces in between each problem) and stores the
    # full collection of vertically arranged problems
    line1 = (' '*4).join(line1_list)
    line2 = (' '*4).join(line2_list)
    line3 = (' '*4).join(line3_list)
    arranged_problems = line1 + '\n' + line2  + '\n' + line3
    
    # If an argument is passed to calculate the solution to each problem, display
    # the solutions below the dashed line
    if solve == True and len(line4_list) > 0:
        line4 = (' '*4).join(line4_list)
        arranged_problems = arranged_problems + '\n' + line4
    
    return arranged_problems