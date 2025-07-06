class employee():
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def info(self):
        print(f"{self.name} lives in {self.address}")

class emFatherName(employee):
    def __init__(self, name, address,fname):
       super().__init__(name, address)
       self.fname = fname
    def info2(self):
        print(f"{self.fname}'s is his father name")
    
       

e1 = emFatherName("Ramesh","dang", "Naresh")
e1.info()
e1.info2()
e2 = emFatherName("Viraj", "Ghorahi", "Saroj")
e2.info()
e2.info2()