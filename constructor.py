class Person:    
    def __init__(self,n,o):
        print("Who are you??")
        self.name = n
        self.age = o

    def info(self):
        print(f"{self.name} is {self.age} years old")

a=Person("Kiran", 8)
b=Person("Ramesh", 7)
a.info()
b.info()
