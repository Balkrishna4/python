# -*- coding: utf-8 -*-
"""Introduction To Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CKdiGgREyEROHwkB2RKiTsZisRJJQO62

# Introduction To Functions

Python functions are a powerful tool in the world of programming. They allow us to group a set of instructions into a reusable block of code. Functions help organize our code and make it more readable. In this lecture, let’s explowre the power of functions in Python.

Python functions are user-defined blocks of code that are designed to perform specific tasks. They allow us to break down our programs into smaller, reusable pieces of code, making our code more organized and easier to maintain.

Why Use Functions?

- Modularity: Functions break down complex programs into smaller, manageable parts, improving code organization and structure.
- Reusability: Functions allow code to be reused, saving time and effort by avoiding code duplication.
- Abstraction: Functions provide a high-level overview, hiding implementation details and making code more readable and understandable.
- Decomposition: Functions help break down complex problems into smaller, more manageable tasks, simplifying the problem-solving process.
- Code Maintenance: Functions make code easier to maintain and debug by isolating and focusing on specific parts of the program.

Types Of Functions.

1. Built-in function: These are pre-defined functions that come with Python, such as print(), len(), input(), range(), and type(). They are readily available for use without requiring any additional code.

2. User-defined function: These functions are created by the user to perform specific tasks. They provide a way to modularize code and promote reusability. User-defined functions are defined using the def keyword.

## Functions Syntax.

```
def function_name(parameters):
    # Function body (code to be executed)
    # ...
    # Optional return statement
    return value
```

Let's break down the different components:

- def: Keyword used to define a function.
- function_name: Name given to the function. It should follow Python naming conventions.
- parameters: Optional input parameters that the function can accept. These are - placeholders for values passed into the function.
- :: Colon to indicate the start of the function block.
- Function body: Contains the code to be executed when the function is called. It is indented with consistent whitespace.
- return: Optional statement used to return a value from the function. If not specified, the function returns None.

## Defining and Calling Python Functions:

To define a function in Python, we use the "def" keyword followed by the function name and parentheses. The function body is then indented and contains the code that will be executed when the function is called. Functions in Python are a powerful tool that helps us write cleaner and more efficient code.
"""

def function_name():

    # Function body: Code that performs the desired task(s)
    print('Hello')

    # Optional return statement: Returns a value or multiple values

# Outside the function: Code that is not part of the function

"""Once the function is defined, you can call it by using the function name followed by parentheses.

"""

def add(a,b):
  return a+b

add(5,6)

function_name()

print(function_name())

"""## Scope of Variables in Functions.

Variables defined inside a function are called local variables. These variables are only accessible within the function. Variables outside a function are called global variables. They can be accessed both inside and outside a function.

"""

x = 101  # global variable


def example_func():
    x = 202  # local variable
    print(x) # Output: 202


example_func()
print(x) # Output: 101

res = add1(5,6)
print(res)

def add1(a,b):
  return a+b

"""## Functions With Parameters.

We know that to create a function, you use the "def" keyword followed by the function name and parentheses.

Inside the parentheses, you can specify any parameters that the function will accept.

```
def function_name(parameters):
    
    # Function body: Code that performs the desired task(s)
    
    # Optional return statement: Returns a value or multiple values
    
# Outside the function: Code that is not part of the function
```


If the function has parameters, you can pass in values for those parameters when calling the function. These values are called as arguments.

Arguments can be of any data type, such as strings, numbers, lists, or dictionaries. Python doesn't require you to explicitly specify the data type of a parameter, making it a flexible and user-friendly language.

```
function_name(argument1, argument2, ...)
```


Functions can be called multiple times with different arguments, allowing you to reuse code and perform the same task with different inputs.


"""

def greet(name):
    print("Hello " + name + "!")

greet("Mithun")
greet("Sanjay")

"""## Types of Arguments:

### Default argument.

These are parameters in a function that have a default value assigned. If an argument is not provided for a default parameter, the default value is used.

"""

def greet(name, message="Hello"):
    print(message, name)

greet("Vishwa", "Good Morning !")


greet("Mithun")  # Uses the default value "Hello" for the message parameter
# Output: Hello Mithun

greet("Mithun", "Hii")
# Output: Hii Mithun

def func(a,b,c,d):
  print(a,b,c,d)

func(5,11,12,9)

"""### Keyword arguments (named arguments)

These arguments are passed to a function using the name of the parameter they correspond to, followed by the = sign. The order of keyword arguments does not matter.

"""

def greet(name, age):
    print("Hello", name, "you are", age, "years old.")

greet("Vishwa",99)


greet(name="Mithun", age=21)  # Output: Hello Mithun you are 21 years old.

# This will also work fine with:

greet(age=21, name="Mithun")  # Output: Hello Mithun you are 21 years old.

"""### Positional arguments.

These are arguments passed to a function in the order specified by the function's parameter list. The values are assigned to the corresponding parameters based on their position.

"""

def add_numbers(x, y):
    sum = x + y
    print("Sum:", sum)

add_numbers(5, 3)
add_numbers(3,5)  # Positional arguments: 5 is assigned to x, 3 is assigned to y
# Output: Sum: 8

"""### Arbitrary arguments (variable-length arguments *args and **kwargs)

Variable-length arguments in Python allow a function to accept a varying number of arguments.

There are two types of variable-length arguments:

1. non-keyword variable-length arguments (*args)
2. keyword variable-length arguments (**kwargs).

- Non-Keyword Variable-Length Arguments (*args):

The *args syntax allows a function to accept any number of non-keyword arguments. Within the function, args becomes a tuple that holds all the passed arguments. You can access and process the individual arguments using indexing or iterating over args.
"""

def sum_numbers(*args):
    print(args)
    print(*args)
    total = 0
    for num in args:
        total += num
    return total


result = sum_numbers(1, 2, 3, 4)
print(result)  # Output: 10

def f(c):
  print(c)



f((5,6,7))

f(5,6)

def f1(*args,a=5,b=6):
  print(args, a, b)

f1(1,2,3,4,5,6)

def f(*args,a,b,):
  print(a,b,args)
  print(*args)


#f(5,6,7,8,9,10)
result = f(6,7,7,8,a=9,b=10)
print(result)

"""**In the above code:**

1. def sum_numbers(*args):: This line defines a function called sum_numbers. The *args syntax in the function parameter list allows you to pass a variable number of arguments to the function. These arguments will be collected into a tuple called args inside the function.

2. total = 0: This line initializes a variable total to 0. This variable will be used to store the sum of all the numbers passed as arguments to the function.

3. for num in args:: This line starts a for loop that iterates over each element in the args tuple, which contains all the arguments passed to the function.

4. total += num: Inside the loop, each number (num) in the args tuple is added to the total variable. This accumulates the sum of all the numbers passed as arguments.

5. return total: After the loop completes, the function returns the total variable, which now holds the sum of all the numbers.

6. result = sum_numbers(1, 2, 3, 4): This line calls the sum_numbers to function with four arguments: 1, 2, 3, and 4. The function calculates the sum of these numbers and returns it, which is assigned to the result variable.

7. print(result): Finally, this line prints the value of the result variable, which contains the sum of the numbers passed to the sum_numbers function.

8. The output of this code is 10, which is the result of adding 1 + 2 + 3 + 4, as calculated by the sum_numbers function.

- Keyword Variable-Length Arguments (**kwargs):

The **kwargs syntax allows a function to accept any number of keyword arguments. Within the function, kwargs becomes a dictionary that holds the passed keyword arguments. You can access and process the individual arguments using dictionary operations.
"""

def display_info(**kwargs):
  print(kwargs)
  print(**kwargs)
  for key, value in kwargs.items():
      print(key + ": " + value)

display_info(name="Mithun", age="21", city="Bengaluru", hobby="Cricket")
# Output:
# name: Mithun
# age: 21
# city: Bengaluru

def func(a,b,*args,**kwargs):
  print(a,b,args,kwargs)

func(5,6,7,8,9,10,name="Vishwa",age=99)

def func1(**kwargs ,a,b):
  print(kwargs,a,b)

func1(name="Vishwa", age=99, 7,9)

def func1(a,b,**kwargs):
  print(kwargs,a,b)
func1(7,9, name="Vishwa")

"""**Here's an explanation of the code snippet:**

1. def display_info(**kwargs):: This line defines a function called display_info. The **kwargs syntax in the function parameter list allows you to pass a variable number of keyword arguments to the function. These keyword arguments are collected into a dictionary called kwargs inside the function, where the keys are the argument names and the values are the corresponding argument values.

2. for key, value in kwargs.items():: This line starts a for loop that iterates over each key-value pair in the kwargs dictionary. In this loop, the key represents the argument name, and the value represents the argument's value.

3. print(key + ": " + value): Inside the loop, the code prints each key-value pair in a specific format, where the key and value are concatenated together with a colon and space in between.

4. display_info(name="Mithun", age="21", city="Bengaluru"): This line calls the display_info function with three keyword arguments: name, age, and city, each with a corresponding value. These keyword arguments are passed in the form of key-value pairs.

## Return Type.

The return type of a function refers to the type of value that the function returns when it is executed. The return type can be explicitly specified using type annotations or implicitly determined based on the value returned by the function.
"""

def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(2, 3))  # Output: 5
#print(add_numbers('2', 3))  # Output: TypeError.

"""In this example, the function add_numbers takes two parameters a and b, both of type int, and it explicitly specifies the return type as an int using the -> syntax. The function performs the addition operation and returns the result, which is of type int."""

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(20))  # Output: True

"""In this case, the function is_even does not have an explicitly specified return type. However, based on the True and False values returned, Python infers that the return type is bool.

Note: It's important to note that in Python, a function can also return None if there is no explicit return statement, or if the return statement does not provide a value.

## Nested functions.

Nested functions in Python refer to defining a function inside another function. The inner function has access to the scope of the outer function, including its variables, parameters, and other nested functions.

Closures
"""

def my_fn():
  name = "Vishwa"
  print(name)

my_fn()
print(name)

def outer_function():
    x = 1  # Variable in the outer function

    def inner_function():
        y = 2  # Variable in the inner function
        result = x + y
        return result

    return inner_function


inner = outer_function() #return a function
print(inner())  # Output: 3

"""In this example, we have an outer function called outer_function() that defines a variable x with a value of 1. Inside the outer function, there is an inner function called inner_function(). The inner function defines a variable y with a value of 2 and performs the addition of x and y. The result is returned from the inner function. Now it is important to note why the inner_function() got called. Well, this is because the outer_function's return statement calls the inner_function() i.e. return inner_function().

Nested functions are like little helpers inside bigger tasks. They keep things neat and organized by doing smaller jobs within a larger job. This helps make code easier to read and understand. They also let you hide some secrets (data) so that only the big task and its helpers can see them. Plus, these little helpers can be used over and over again, saving you time and effort. So, nested functions make your code cleaner, more reusable, and easier to work with.

"""