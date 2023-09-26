# lists + functions+ methods # lists are editable.
my_list=[1,2,3,4.5,'mahesh']
print(len(my_list))
my_list.reverse()
print(my_list)
my_list.append(10)
print(my_list)

# tuple




# exercise for list
exerccise_list=['first entry',[123,456,[0,'Hello:)']],'bye']
print(exerccise_list[1][2][1])

# splicing with list
test_list=[1,2,3,4,5,6,7,8,9,10]
# task:: start from 8 and go to 2 , picking second element 
print(test_list[7:0:-2])
# test tuple
test_tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(test_tuple[0:13:3])
# unpacking 
a,b=('mahesh','chivate')
print(a);print(b)
# stich the values of the varible
value_1= 10
value_2= 'test'
value_1,value_2=value_2,value_1
print(value_2)
# exercise
test_string=[1,2,3,4]
print((str(test_string[1:4])).strip('[').strip(']').replace(',',''))
print(str(test_string).strip('[').strip(']').replace(',',''))

# dictionaries
## Basics
test_dict={'A':123,'B':[1,2,3],'mahesh':True}
print(test_dict)
print(test_dict.items())
print(len(test_dict))
# converting a dict
print(tuple(test_dict.items()))
print(list(test_dict.items()))
print(str(test_dict.items()))

# indexing with dict
print(test_dict['mahesh']) # does crash when it does not find a key. @method 1
print(test_dict.get('B')) # doesn't crash when it does not find a key. @ method 2 # preferred.

# update key:value pair
test_dict.update({'another key':(1,2,3,4,5)}) # method 1
test_dict.update(Z= 'zebra', O='owl') # method 2 
print(test_dict)
test_dict['D']='dog' # method 3
print(test_dict)

## sets
# sets values needs to be unique
# any duplicate will be deleted.
my_set={1,2,3,4,5,6,6}
print(len(my_set))
print(my_set)
my_set.add(7) # add value to the set
print(my_set)

my_set.remove(3) # remove value from the set.
print(my_set)
print(list(my_set)[2])
print(list(my_set))

# indexing and slicing doesn't work in set

print(my_set.pop())
print(my_set)


# !! IMPORTANT !! sets are very good when it comes  to #comparisons.

set1={1,2,3,4,4}
set2={4,5,6,7,8,9}
print(set1.union(set2)) # method 1
print(set1|set2) # method 2 @ preferred.

print(set1 .intersection(set2)) # met  hod 1 
print(set1 & set2) # method 2

print(set2.difference(set1)) # method 1 
print(set1.difference(set2))
print(set2 - set1) # method 2 

# exercise 
# check if the list below has duplicate values
test_list1= [1,2,4,5,6,7,8,9,88,66,55,44,33,22,22,21,34,65,76,43,22,53,22,11,10]
print(len(test_list1))
print(len(set(test_list1)))
print(len(test_list1)==(len(set(test_list1)))) # boolean comparsion

# Boolean operators
"""Usually created by comparison operators; 5<10 creates the boolean 'True'.This is useful to control #flow of code. If condition is True then do something."""
print(1==10)
print(1!=10)   
print(not 10>10)
# Booleans and lists and strings
print(1 in (1,2,3,4))
print('m' in 'hello')
print(4 not in[1,2,3,5])

# data conversion
e_dict={1:'one',2:'two',3:'three'} 
# check if key 1 exits in the dict
print (1 in e_dict.keys())
# check if the value 'four' in the dict 
print('three' in e_dict.values()) 
# Booleans by themselves
print(not True)
print(True)

# Bool function
# !! IMPORTANT!! bool() can accept any number , string , type of container and still return a value
 # truthy
 # Falsy 0,0.0,'',
print(bool(123))
print(bool(-12))

# other data types
#  1 sequence 2 Bytes 3 complex numbers 4 memoryview 5 frozensets  
