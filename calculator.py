# prompt the user to input two operands, which are floating point numbers.
first_operand = float(input("Enter first operand: "))
second_operand = float(input("Enter second operand: "))

# This block of code will display the calculator menu - the list of operations to choose from
print("Calculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# prompt the user to input an integer value (1, 2, 3, or 4) corresponding to the operation of their choice
operation = int(input("Which operation do you want to perform? "))

# this block of code will perform the operation based on user selection and stores the result
# If the user inputs "1", the operation is addition,
# If the user inputs "2", the operation is subtraction,
# If the user inputs "3", the operation is multiplication,
# If the user inputs "4", the operation is division,
# If the user doesn't select an invalid option (a value outside of 1,2,3, or 4), The error message prints.
if operation == 1:
    result = first_operand + second_operand
elif operation == 2:
    result = first_operand - second_operand
elif operation == 3:
    result = first_operand * second_operand
elif operation == 4:
    result = first_operand / second_operand
else:
    print("Error: Invalid selection! Terminating program.")
    exit()

# this block of code prints the result and the goodbye message
print(f'The result of the operation is {result}. Goodbye!')

