#Printig simple message
print('Hi. Welcome to python')

#variable declaration
var_int=12
var_string="Deepak"
print(var_int,var_string)

#function declaration
def f1():
    s = 'some text inside the f1 function'
    print(s)
    
#Calling/invoking the function
f1()


#Sequenced data: List, Tupple, Range, data:dictionary, Set
list_data = [9,2.9,[3,-5],['jenkins','jira']]
print(list_data)

#Tupple uses () but list uses [] and set uses {}
tupple1 = (("cicd","jenkins"),("security","fortify"))
print(tupple1)

#region Diff between List and Tupple
# 
# In Python, both lists and tuples are used to store collections of items, but there are some key differences between them:

# Mutability:

# List: Lists are mutable, which means you can modify their contents by adding or removing elements, or by changing the values of existing elements.
# Tuple: Tuples, on the other hand, are immutable. Once a tuple is created, you cannot change its values or size. You can't add, remove, or modify elements in a tuple.
# Syntax:

# List: Lists are created using square brackets [].
# python
# Copy code
# my_list = [1, 2, 3, 4]
# Tuple: Tuples are created using parentheses ().
# python
# Copy code
# my_tuple = (1, 2, 3, 4)
# Performance:

# List: Because of their mutability, lists may require more memory and can be slightly slower than tuples.
# Tuple: Tuples, being immutable, are generally more memory-efficient and may offer better performance in certain situations.
# Use Cases:

# List: Use lists when you have a collection of items that might need to be modified during the program's execution, such as when you are working with a dynamic dataset.
# Tuple: Use tuples when you want to create a collection of items that should remain constant throughout the program, or when you want to ensure data integrity and prevent accidental modification.
# Here's a simple example to illustrate the difference:

# python
# Copy code
# # List example
# my_list = [1, 2, 3, 4]
# my_list[0] = 99  # Valid - lists are mutable

# # Tuple example
# my_tuple = (1, 2, 3, 4)
# # The following line would result in an error because tuples are immutable
# # my_tuple[0] = 99
# In summary, choose between lists and tuples based on your requirements for mutability and the specific characteristics of the data you are working with.
# 
# endregion


#Initial value: 10
#Last value: 30
#Increment by 5
sequence1 = range(10,30,5) 
for i in sequence1:
    print(i)
#Output:10 15 20 25   


dict1 = {"name":'Devops', "batch":3.0}
print(dict1)
print("Dictionary by key/name",dict1["name"])

set1 = {"test", 19, False, 5.9}
print("set is: ",set1)

# region remove duplicate elements using set
# Sets in Python are unordered collections of unique elements. Here are some situations where using a set in Python is beneficial:

# Uniqueness:

# Sets do not allow duplicate elements. If you have a collection of items and you want to ensure that each item is unique, a set is a good choice.
# python
# Copy code
# unique_numbers = {1, 2, 3, 4, 5}
# Membership Testing:

# Sets provide constant-time membership testing. If you need to quickly check whether a specific element is present in a collection, a set is more efficient than a list.
# my_set = {1, 2, 3, 4, 5}
# print(3 in my_set)  # Output: True

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("unique list after convertion of set: ", unique_list)
# endregion

letters = "abcdefghijklmnopqrstuvwxyz"
str_letters = str(letters)
list_letters = list(letters)
tuple_letters = tuple(letters)
set_letters = set(letters)
print("str_letters:-",str_letters)
print("list_letters:-",list_letters)
print("tuple_letters:-",tuple_letters)
print("set_letters:-",set_letters)

complexType = 2+4j
print("Complex type",complexType)

num1=25
num2=float(num1)
print("Number converted to float:",num2)

float1=35.6
int1=int(float1)
print("Float converted to int:",int1)
print("Float converted to bool:",bool(float1))
print("Bool of zero:",bool(0))








