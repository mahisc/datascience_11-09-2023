# Flow 
"""1 If elif else # run code if conditions are true 
    2 Match # If statements for more specific values
    3 While # Repeat code as long as conditions are true
    4 For # Run code for every item in a container
    5 next # 
    6 break # 
"""
# exercise 'If elif else'
money_available = 50  
if money_available >= 80:
    print('Eat something Fancy')
elif money_available > 45:
    print('Eat something Nice')
elif money_available > 15:
    print('Eat something ok!')
else:
    print('Eat something Cheap')
# more complex 'if' conditions
# combining with And,or and nesting if conditions
if True and True :
    print(True)
     
# Exercise 
money_available=100
hungry=True
bored=True
# check if money available > 80 and if hungry is true or if bored
if money_available >= 80 and hungry==True or bored==True:
    print('Eat something fancy!!')
    
# nested if statements
x= 'a'
if x in ['a','b', 1]:
    print( "is in the list")
    if not x.isalpha():
        print('It is a integer')
    if True:
        print('Something')
# exercise
money_available=100
hungry=True
bored=True

# create a nested if statement that runs of all 3 conditions are true
if money_available > 80:
    print('I have enough money')
    if hungry== True:
        print('i am hungry too!')
        if bored== True:
            print('Eat something faancy!!')
            