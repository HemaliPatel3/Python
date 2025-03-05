
## **1. Creating Your Own Modules**
A module is a file containing Python code, such as functions, classes, or variables, that can be imported and reused in other programs.

### **Steps:**
1. Create a new file **`mymodule.py`**.
2. Define functions or classes inside it.

### **Code (`mymodule.py`):**
```python
def greet(name):
    return f"Hello, {name}!"

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."
```

---

## **2. Accessing a Module in Another File**
To use a module in another file, we need to **import** it.

### **Code (`main.py`):**
```python
import mymodule  # Importing the module

message = mymodule.greet("Alice")
print(message)
```

### **Output (`main.py` Execution):**
```
Hello, Alice!
```

---

## **3. Using Classes from the Module**
We can import and use classes defined inside a module.

### **Code (`main.py`):**
```python
from mymodule import Person  # Importing the Person class

p = Person("Bob")
print(p.introduce())
```

### **Output:**
```
My name is Bob.
```

---

## **4. Using Independent Methods from Modules**
We can directly import and use standalone functions from a module.

### **Code (`main.py`):**
```python
from mymodule import greet  # Importing only the function

print(greet("Charlie"))
```

### **Output:**
```
Hello, Charlie!
```

---

## **5. Using Class Methods from Modules**
Class methods can be used by first importing the class and then calling the method on an object.

### **Code (`main.py`):**
```python
from mymodule import Person  # Importing the Person class

p1 = Person("David")
print(p1.introduce())  # Calling class method
```

### **Output:**
```
My name is David.
```

---

### **Summary**
- **Create a module** → Write Python functions/classes in a separate `.py` file.
- **Access module** → Use `import module_name` in another script.
- **Use classes** → Import class and create objects.
- **Use functions** → Import functions and call them.
- **Use class methods** → Call methods using object instances.
