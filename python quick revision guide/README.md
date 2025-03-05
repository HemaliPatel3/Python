# 1. Features

- **Simple**: Easy to read and write.

- **Easy to use**: Beginner-friendly syntax.

- **Free and open-source:** Available for all.

- **Portable:** Runs on multiple platforms.

- **Interpreted:** Executes code line-by-line.

- **Scalable:** Suitable for small and large applications.

- **Extensive Libraries:** Supports numerous built-in and third-party libraries.

# 2. Working with Python

- **Working with Python Interpreter:** Python shell allows interactive coding.

- **Running a Python File from Terminal:** Use python filename.py to execute scripts.

- **Working with Eclipse IDE:** Install PyDev plugin to code in Python using Eclipse.  

# 3. Basics

- **Explicit Line Joining:** Use \ to break long lines.

- **Escape Sequences:** \n, \t, \\, etc.

- **Indentation:** Essential for code blocks.

- **Undefined Variables:** Accessing undefined variables raises NameError.

- **Single Statement Coding:** Write single-line if statements: if x > 5: print("Greater")

- **dir() Method:** Lists attributes and methods of an object.

# 4. Basic Data Types

- **Strings:** Text data.

- **Integer:** Whole numbers.

- **Float:** Decimal numbers.

- **Boolean:** True or False.

- **Type Conversions:** Convert between types using int(), str(), float(), etc.

# 5. Operators

- **Arithmetic Operators:** +, -, *, /, **, //, %

- **Bitwise Operators:** <<, >>, &, |, ~, ^

- **Relational Operators:** <, >, <=, >=, ==, !=, is, is not

- **Logical Operators:** and, or, not

# 6. Expressions

- **Variable Expressions:**
```python
x = 10
y = x + 5
print(y)  # Output: 15
```

- **Literal Expressions:**
```python
print(42)  # Output: 42
```

- **Heterogeneous Expressions:**  
```python
print("Age:", 25)  # Output: Age: 25
```

# 7. Control Flow

- **if – elif – else:**
``` python
x = 10
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")
```

- **while – else:**
``` python
x = 3
while x > 0:
    print(x)
    x -= 1
else:
    print("Done")
```
- **for – else:**
``` python
for i in range(3):
    print(i)
else:
    print("Loop Finished")
```
- **break:**
``` python
for i in range(5):
    if i == 3:
        break
    print(i)
```
- **continue:**
``` python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

# 10. Methods/Functions
- **Defining a function:**
``` python
def greet():
    print("Hello")
greet()
```
- **Arguments and Return:**
``` python
def add(a, b):
    return a + b
print(add(5, 3))
```
- **Recursion:** 
``` python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
```

# Object-Oriented Programming
- **Class & Object:**
``` python
class Car:
    def __init__(self, brand):
        self.brand = brand
my_car = Car("Toyota")
print(my_car.brand)
```
- **Method Overriding:**
``` python
class Animal:
    def speak(self):
        print("Animal Sound")
class Dog(Animal):
    def speak(self):
        print("Bark")
dog = Dog()
dog.speak()
```

**12. Data Structures**

**List**
A list is an ordered, mutable collection of elements.
```python
my_list = [1, 2, 3, 4]
print(my_list[0])  # Accessing first element
```

**Tuple**
A tuple is an ordered, immutable collection of elements.
```python
my_tuple = (1, 2, 3, 4)
print(my_tuple[1])
```

**Dictionary**
A dictionary stores key-value pairs.
```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])
```

**Set**
A set is an unordered collection of unique elements.
```python
my_set = {1, 2, 3, 4}
print(2 in my_set)  # True
```

**Type Conversion**
Converting between data types.
```python
num = "10"
converted_num = int(num)
print(converted_num + 5)  # 15
```

**Indexing**
Accessing elements using index positions.
```python
string = "Python"
print(string[0])  # P
```

**String and Indexing**
Strings support indexing.
```python
text = "Hello"
print(text[-1])  # o
```

**Looping without Index**
Using a loop without index.
```python
for item in ["a", "b", "c"]:
    print(item)
```

**in and not in Operators**
Checking membership in a collection.
```python
print(3 in [1, 2, 3])  # True
print("a" not in "hello")  # True
```

**Slicing using : & ::**
Extracting parts of sequences.
```python
lst = [1, 2, 3, 4, 5]
print(lst[1:4])  # [2, 3, 4]
print(lst[::-1])  # Reversed list
```

---

**13. Working with Modules**

**Creating your own modules**
```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"
```

**Accessing them in other files**
```python
import mymodule
print(mymodule.greet("Alice"))
```

**Using Classes from Modules**
```python
class Person:
    def __init__(self, name):
        self.name = name
```

**Using Independent Methods from Modules**
```python
from mymodule import greet
print(greet("Bob"))
```

**Using Class Methods from Modules**
```python
from mymodule import Person
p = Person("Alice")
print(p.name)
```

---

**14. I/O in Python**

**Input**
```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

**Print**
```python
print("Hello, World!")
```

**Pickle**
```python
import pickle

data = {"name": "Alice", "age": 25}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

---

**15. Exception Handling**

**Errors**
```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**try-except-else**
```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid input")
```

**User-defined exceptions**
```python
class MyError(Exception):
    pass

try:
    raise MyError("Custom Error")
except MyError as e:
    print(e)
```

**try-except-finally**
```python
try:
    print(1 / 1)
finally:
    print("This always runs")
```

---

**16. Standard Library**

**sys**
```python
import sys
print(sys.version)
```

**os**
```python
import os
print(os.getcwd())
```

**platform**
```python
import platform
print(platform.system())
```

**logging**
```python
import logging
logging.warning("This is a warning")
```

**re**
```python
import re
match = re.search("hello", "hello world")
print(match.group())
```

**time**
```python
import time
time.sleep(1)
print("Waited 1 second")
```

**datetime**
```python
import datetime
print(datetime.datetime.now())
```

**random**
```python
import random
print(random.randint(1, 10))
```

---

**17. Database Connectivity**

**Connecting with Databases**
```python
import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
```

**Accessing Records**
```python
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
```

**Updating Records**
```python
cursor.execute("UPDATE users SET age=30 WHERE name='Alice'")
conn.commit()
```

---

**18. Power of Python**

**lambda functions**
```python
add = lambda x, y: x + y
print(add(2, 3))
```

**In-line Coding**
```python
print((lambda x: x * 2)(5))
```

**assert**
```python
x = 5
assert x > 0, "x is not positive"
```

**exec**
```python
exec("print(2 + 3)")
```

---

**19. Built-in Functions**

```python
print(any([False, True, False]))  # True
print(all([True, True, False]))  # False
print(round(4.567, 2))  # 4.57
print(abs(-5))  # 5
print(max(3, 7, 2))  # 7
print(min(3, 7, 2))  # 2
print(divmod(10, 3))  # (3, 1)
print(eval("3 * 3"))  # 9
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))  # [3, 4]
print(list(map(lambda x: x * 2, [1, 2, 3])))  # [2, 4, 6]
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # 10
```

This document provides explanations and Python code examples for each topic.

