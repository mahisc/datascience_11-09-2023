# !! Functions are a way to group code together and reuse it
# We first create a function and then we call it
# exercise
# create a calculator function 

# Basic calculator !! function !! Building a function

def calculator(num1,num2,operator):
    if operator == "+": # Addition
        result = num1 + num2
        print(f'Addition of {num1} + {num2} = {result}')
    elif operator == "-": # Subtraction
        result = num1 - num2
        print(f'Subtraction of {num1} - {num2} = {result}')
    elif operator == "*": # Multiplication
        result = num1 * num2
        print(f'Multiplication of {num1} * {num2} = {result}')
    elif operator == "/": # Division
        result = num1 / num2
        print(f'Division of  {num1} / {num2} = {result}')
    elif operator == "//": # Floor Division
        result = num1 // num2
        print(f'Floor Division of {num1} // {num2} = {result}')
    elif operator == "%": # Modulus
        result = num1 % num2
        print(f'Modulus of {num1} % {num2} = {result}')
    elif operator == "**": # Exponent
        result = num1 ** num2
        print(f'Exponent of {num1} ** {num2} = {result}')
    else:
        print("Invalid operator")
        
# !! calling the function !!

# ADDITION

calculator(10,5,"+")

# SUBTRACTION

calculator(10,5,"-")

# MULTIPLICATION

calculator(10,5,"*")

# DIVISION

calculator(10,5,"/")

# FLOOR DIVISION


calculator(10,5,"//")

# MODULUS

calculator(10,5,"%")

# EXPONENT

calculator(10,5,"**")   

# INVALID OPERATOR

calculator(10,5,"&") # invalid operator

