a=50
def num():
    global b
    b=60
    print(f"inside function{a}")
    print(f"inside function{b}")
num()
print(f"outside function {a}")    
print(f"outside function {b}")    #it should have  caused an error as it has been locally defined inside the function but we are calling it outside of its scope.
#here a and b are namespaces and they both are defined in a specific scope . BUT we've used global keyword for defining value of b globaly rather than just inside of the function.
