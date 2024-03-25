def sum(a,b):
    s = a + b
    return s
print(sum(2,3))


def print_hello():
    print("hello")
print_hello()   
output = print_hello()
print(output)   #it will print none
output = print_hello
print(output) 


# default parameterd
#assigning a default value to parameter ,which is used when no argument is passed
def sum(a=3,b=9):
    return a+b
print(sum())


# default is given from last