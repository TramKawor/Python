#used to modify the behaviour of the function
def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello!!")
        fx(*args, **kwargs)
        print("Thsnks for visiting")
    return mfx
@greet
def hello():
    print ("How are you\n")

@greet
def add(a,b):
    print(a+b)
    
hello()
add(5,5)