# parameters and Arguments
## note: parameters are the variables in the function definition
## note: arguments are the values passed into the function
# !! Positional Arguments follows keyword arguments !!
# !! keyword arguments must be defined after positional arguments !!

# Default Arguments are difined in function itself by"=" sign 
# Example



def test_function ( 
    arg1 = 'Argument 1',
    arg2 = 'Argument 2',
    arg3 = 'Argument 3',
    arg4 = 'Argument 4'
    ):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

test_function()


# exercise
# create greeting function with 3 parameters: person,greet and weekday
# person and greet should have default arguments("Person" for person and "Hello" for greet)
# inside the function use f'string to print the greeting, person and weekday
# when calling the function, use atleast one positional argument and one keyword argument

# Building a function
def greeting(person = "Person",greet = "Hello",weekday = "Monday"):
    print(f'{greet} {person}! Happy {weekday}!!')
    
# !! calling the function !!
greeting("John","Good morning",weekday="Sunday")


# !! types of parameters !!

# 1. Positional Parameters (Required Parameters) # It is defined while building a function itself.
def positional_parameters(a,b,c,d):
    print(a,b,c,d)
    
# !! calling the function !!    
positional_parameters(1,2,3,[4,'mahesh']) # here 1 is assigned to a, 2 is assigned to b, 3 is assigned to c and [4,'mahesh'] is assigned to d. therefore, the output is 1 2 3 [4,'mahesh']

# 2. Default Parameters (Optional Parameters) # It is defined while building a function itself by "=" sign.
def default_parameters(a,b,c,d=10):
    print(a,b,c,d)
# !! calling the function !!
default_parameters(1,2,3) # here a=1 is assigned to a, b=2 is assigned to b, c=3 is assigned to c and d=10 is assigned to d. therefore, the output is 1 2 3 10

# 3. Keyword Parameters (Named Parameters) # It is defined while calling a function by "=" sign.
def keyword_parameters(a,b,c,d):
    print(a,b,c,d)

# !! calling the function !!
keyword_parameters(d=1,b=2,c=3,a=[4,'mahesh']) # here a=1 is assigned to a, b=2 is assigned to b, c=3 is assigned to c and d=[4,'mahesh'] is assigned to d. therefore, the output is 1 2 3 [4,'mahesh']





 ## !!  positional arguments follows keyword arguments !!
def positional_keyword_parameters(a,b,c,d):
    print(a,b,c,d)

# !! calling the function !!
positional_keyword_parameters(1,2,c=3,d=4) # here a=1 is assigned to a, b=2 is assigned to b, c=3 is assigned to c and d=4 is assigned to d. therefore, the output is 1 2 3 4

# !! Summary !!
# Parameters and Arguments 
## Parameters are the variables in the function definition and Arguments are the values passed into the function.
## Positional Arguments follows keyword arguments.
## Keyword arguments must be defined after positional arguments.
## Default arguments are defined in function itself by "=" sign.
## Positional Parameters are defined while building a function itself.
## Default Parameters are defined while building a function itself by "=" sign.
## Keyword Parameters are defined while calling a function by "=" sign.

## Parameters and Arguments II 
# List unpacking
hello,mahesh,python = "world","kumar","programming"

def print_all (one , *arguments,extra = "extra"):
    print(type(arguments))
    # print two parameters in single print statement
    print(one,arguments,extra)
    #print(arguments)
    #print(one)
    # print all the arguments
    for argument in arguments:
        print(argument)
        
print_all(1,2,3,4,5,6,7,8,9,10, [hello =="earth","kumar","programming"], extra = 12)
