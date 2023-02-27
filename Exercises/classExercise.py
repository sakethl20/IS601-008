class Person:
    def __init__(self, name, age , occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getOccupation(self):
        return self.occupation
    
    
p1 = Person('Saketh Lakshmanan', 21, 'student')

print(p1.getName())
print(p1.getAge())
print(p1.getOccupation())