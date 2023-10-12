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

# Match case
mood='Sad'
match mood :
    case 'Hungry':
        print("Get some food Mahesh")
    case 'Thirsty':
        print("Get some water")
    case _:
        print("out of context!!")
                     
# While loop !! Repeat code as long as condition is True
x=0
while x<3:
    x+=1
    print('loop')

# !! IMPORTANT!! concept of break and continue
# exercise
# use a while loop to create a list with only even values from 0 to 100
# !!Wrong solution !!
# x=0 
# while x < 100:
#     x+=2
#     print(list[x])
# !! Wrong solution !!
# a=10;b=1
# if a!=b:
#  print('untrue')
x=5
while x<10:
    x+=1
    print("hello while loop!!")

#  while will only run if the Boolean value is set to 'True'
#    !!if Boolean value is false while loop will not execute.!!

# Break !! Ends the entire while loop !!

x=0 
while x<5:
    x+=1
    if x==3:
        break # break terminates the loop
    print ("loop is protected")
    
    # continue !! skips the current iteration!!

x=0
while x<10:
    x+=1
    if x==5:
        continue # !!! continue skips the loop
    print(x)
     
# exercise
# use a while loop to create a list with only even values from 0 to 100
# do not add the value 58!

# my_list=[]
# counter=0
# while counter <=100:
#     if counter%2==0 and counter!=58: 
#         my_list.append(counter)
#         counter+=1
# print(my_list)
my_list = []
counter = 0
while counter<= 100:
    if counter % 2 ==0 and counter != 58: # method 1 using and condition
        my_list.append(counter)
    counter += 1
print(my_list)

# method 2 using nested if condition 
my_list = []
counter = 0
while counter<= 100:
    if counter % 2 ==0:
        if counter != 58: # !! method 2 using nested if condition !!
            my_list.append(counter)
    counter += 1
print(my_list)

# CONCEPT !! for loop !! run code for every item inside of a container 
basic_list = [1,2,3]
for x in basic_list:
    print(x)
basic_tuple = (1,2,3)
for x in basic_tuple:
    print(x)
basic_set = {1,2,3}
for x in basic_set:
    print(x)
basic_dict= {1:"one",2:"two",3:"three"}
for x in basic_dict.items():
    print(x)
basic_string = 'one two three'
for x in basic_string:
    print(x)
basic_num = 3 # numbers are not irrerable. use range function
print(range(basic_num)) # range is itself a differnt container 
for x in range(basic_num):
    print(x)

# method 2 'for' & 'range' go hand in hand
for x in range(10,20,2):
    print(x)


# exercise 
