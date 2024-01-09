#Case1:Default Arguments
def name(fname, mtame = "jenkins", boardname = "Jira"):
    print("Hello, ", fname, mtame, boardname)

name("sonar")  


#Case2:Keyword Arguments
def name(firstTool, secondTool, thirdTool):
    print("Hello, ", firstTool, secondTool, thirdTool)

name(thirdTool = "Ansible", firstTool="Terraform", secondTool="Jmeter")    

#Case3:Required Arguments
def name(firstTool, secondTool, thirdTool):
    print("Hello, ", firstTool, secondTool, thirdTool)

name("Ansible", "Terraform", "Jmeter")


#Case4:Variable-length Arguments
def listName(*name):
    print("Hello, ", name[0], name[1], name[2])

listName("Ansible", "Terraform", "Jmeter") 


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



