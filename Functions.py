
#Functions
def versionCheck(version):
    if(version < 0):
        print('vesion is negative')
    elif(version > 0):
        if(version <= 10):
            print("version is between 1 - 10")
        elif(version > 10 and version <= 20):
            print('version is between 11-20')
        else:
            print('version is greater than 20')        
    else:
        print('version is zero') 

versionCheck(10)


def listName(*name):
    print("hello", name[0], name[1], name[2])

listName("Ansible", "Terraform", "Jmeter")    


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
print("Factorial by library: ",factorial(5))


