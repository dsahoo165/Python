class Tools:
    name = "Jenkins"
    version = 20

    def toolsdesc(self):
        print(self.version, self.name + "\t Inside Tools function")

   #self has to be passed in the function param. otherwise method can not be invoked
   #with the help of self properties/global variables can be accessed inside the method


T1 = Tools()    
T1.toolsdesc()

print(T1.name)
print(T1.version)