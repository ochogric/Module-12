class Pet:
    def setName(self,n):
        self.name = n;
    def setType(self, t):
        self.type = t
    def setAge(self, a):
        self.age = a
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAge(self):
        return self.age

mypet = Pet()
name = input("Enter the pet's name: ")
mypet.setName(name)
type = input("Enter the pet's type: ")
mypet.setType(type)
age = input("Enter the pet's age: ")
mypet.setAge(age)
print("The pet's name is", mypet.getName())
print("The pet's type is", mypet.getType())
print("The pet's age is", mypet.getAge())
