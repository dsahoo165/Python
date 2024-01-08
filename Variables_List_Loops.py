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

In Python, both lists and tuples are used to store collections of items, but there are some key differences between them:

Mutability:

List: Lists are mutable, which means you can modify their contents by adding or removing elements, or by changing the values of existing elements.
Tuple: Tuples, on the other hand, are immutable. Once a tuple is created, you cannot change its values or size. You can't add, remove, or modify elements in a tuple.
Syntax:

List: Lists are created using square brackets [].
python
Copy code
my_list = [1, 2, 3, 4]
Tuple: Tuples are created using parentheses ().
python
Copy code
my_tuple = (1, 2, 3, 4)
Performance:

List: Because of their mutability, lists may require more memory and can be slightly slower than tuples.
Tuple: Tuples, being immutable, are generally more memory-efficient and may offer better performance in certain situations.
Use Cases:

List: Use lists when you have a collection of items that might need to be modified during the program's execution, such as when you are working with a dynamic dataset.
Tuple: Use tuples when you want to create a collection of items that should remain constant throughout the program, or when you want to ensure data integrity and prevent accidental modification.
Here's a simple example to illustrate the difference:

python
Copy code
# List example
my_list = [1, 2, 3, 4]
my_list[0] = 99  # Valid - lists are mutable

# Tuple example
my_tuple = (1, 2, 3, 4)
# The following line would result in an error because tuples are immutable
# my_tuple[0] = 99
In summary, choose between lists and tuples based on your requirements for mutability and the specific characteristics of the data you are working with.
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

genderDict = {"male":0,"female":0}
peopleData = [{"name":"Deepak", "gender":"male"}, 
              {"name":"Shyam", "gender":"male"},
              {"name":"Ram", "gender":"male"},
              {"name":"Sita", "gender":"female"}]
for i in peopleData:
    if(i["gender"] is "male"): # is similar to == 
        genderDict["male"] = genderDict["male"] + 1
    else:
        genderDict["female"] = genderDict["female"] + 1    
print("males in the list",genderDict["male"])
print("females in the list",genderDict["female"])

strToTest = "Deepak"
strVowels = ["A","E","I","O","U"]
print("String length is : ",len(strToTest)) 
print("String in uppercase", strToTest.upper())
strVowelsFound = []
for i in strToTest.upper():
    if(i in strVowels):
        strVowelsFound.append(i)
print("Length of matching letters:",len(strVowelsFound))
print("matching array", strVowelsFound)    

print('Spaces removed by strip():',"   hello   ".strip())
print('Capitalize() to make the first char to upper and rest of the chars to lower():',"heLLO".capitalize())
print('Find() to find the portion from string:',"Hello World".find('World'))

#Indexes
ToolsData = ['Maven','Ansible','Jenkins']
CloudData = ['aws','azure','gcp']
print("Array before appending",ToolsData)
ToolsData.append('Docker')
print("Array after appending",ToolsData)
ToolsData.insert(1,'NodeJS')
print("Array after Insert",ToolsData)

ToolsData.extend(CloudData)
print("Array after extend",ToolsData)

ToolsData.pop()
print("Array after pop",ToolsData)

ToolsData.remove('Docker')
print("Array after remove()",ToolsData)

del ToolsData[4]
print("Array after del",ToolsData)

#ToolsData.clear()
#print("Array after clear",ToolsData)

if "Maven" in ToolsData:
    print('Maven is present')

#While loop
count=5
while(count > 0):
    print("count inside the while loop",count)
    count = count-1

#nested loop
i=1
while(i<=3):
    for k in range(1,4):
        print(i,"*",k,"=",(i*k))
    i=i+1
    print() #prints empty line



print('For and while starts below')
for i in range(1,4):
    k=1
    while(k<=3):
        print(i,"*",k,"=",(i*k))
        k = k+1
    print()   

ToolsData = ["Maven","Ansible","Jenkins","Sonar"] 
ToolsData.sort()
print(ToolsData)

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)










