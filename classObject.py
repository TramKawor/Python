class person:
    name = "Harry"
    occupation = "Politician"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()

a.name = "Ram"
b.occupation = "Doctor"

b.name = "Rita"
b.occupation = "Teacher"

a.info()
b.info()

