# Python Recursion: Function calling a function
def factorial_dk(num):
    if(num == 1 or num == 0):
        return 1
    else:
        print("num inside factorial: ",num)
        return (num * factorial_dk(num-1))

num = 6;
print("number: ", num); 
print("Factorial: ", factorial_dk(num)) 





#Library reference
from math import *
print()
print("Factorial by library: ",factorial(6))