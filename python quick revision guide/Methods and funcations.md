Here’s a brief explanation, example code, and the expected output for each topic:

---

### **1. Defining a Function**
A function is a block of reusable code that performs a specific task. Functions help in code reusability and modularity.

#### **Code:**
```python
def greet():
    print("Hello, welcome to Python!")

greet()
```

#### **Output:**
```
Hello, welcome to Python!
```

---

### **2. Local Variables**
A local variable is defined inside a function and can only be accessed within that function.

#### **Code:**
```python
def local_example():
    message = "I am a local variable"
    print(message)

local_example()

# print(message)  # This would give an error since 'message' is local to the function
```

#### **Output:**
```
I am a local variable
```

---

### **3. Arguments and Return**
Functions can take arguments as input and return a value as output.

#### **Code:**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
```

#### **Output:**
```
Sum: 8
```

---

### **4. Keyword Parameters / Default Parameters**
Keyword arguments allow specifying arguments by name, and default parameters provide default values if no argument is passed.

#### **Code:**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")
greet()
```

#### **Output:**
```
Hello, Alice!
Hello, Guest!
```

---

### **5. Global Variable**
A global variable is accessible throughout the program, inside and outside functions.

#### **Code:**
```python
global_var = "I am global"

def access_global():
    print(global_var)

access_global()
```

#### **Output:**
```
I am global
```

---

### **6. Nested Function**
A nested function is a function defined inside another function.

#### **Code:**
```python
def outer():
    def inner():
        print("Hello from inner function")
    inner()  # Calling inner function inside outer

outer()
```

#### **Output:**
```
Hello from inner function
```

---

### **7. Recursion**
Recursion is a technique where a function calls itself to solve a problem.

#### **Code (Factorial Calculation):**
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
```

#### **Output:**
```
Factorial of 5: 120
```

---
