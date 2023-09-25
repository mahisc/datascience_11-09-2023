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

