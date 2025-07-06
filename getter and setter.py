class myValue:
    def __init__(self, value):
        self._value = value

    def show(self):
        return print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return self._value *6
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 7
    
obj = myValue(10)
obj.ten_value = 45
print(obj._value)
obj.show()