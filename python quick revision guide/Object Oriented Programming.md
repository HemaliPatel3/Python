## **1. Class & Object**
A class is a blueprint for creating objects. An object is an instance of a class with attributes (variables) and behaviors (methods).

### **Code:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print("Car Brand:", car1.brand)
print("Car Model:", car1.model)
```

### **Output:**
```
Car Brand: Toyota
Car Model: Corolla
```

---

## **2. Object Methods**
Object methods are functions defined inside a class that operate on the object’s attributes.

### **Code:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Honda", "Civic")
car1.show_details()
```

### **Output:**
```
Car: Honda Civic
```

---

## **3. Self**
The `self` parameter represents the instance of the class and is used to access its attributes and methods.

### **Code:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

p1 = Person("Alice", 25)
p1.introduce()
```

### **Output:**
```
Hi, I am Alice and I am 25 years old.
```

---

## **4. Constructor (`__init__`)**
A constructor is a special method (`__init__`) that gets called when an object is instantiated. It initializes object attributes.

### **Code:**
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def details(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

s1 = Student("Bob", "A")
s1.details()
```

### **Output:**
```
Student: Bob, Grade: A
```

---

## **5. Destructor (`__del__`)**
A destructor (`__del__`) is called when an object is deleted or goes out of scope.

### **Code:**
```python
class Example:
    def __init__(self):
        print("Object created!")

    def __del__(self):
        print("Object destroyed!")

obj = Example()
del obj  # Manually deleting the object
```

### **Output:**
```
Object created!
Object destroyed!
```

---

## **6. Inheritance**
Inheritance allows a class (child class) to inherit properties and methods from another class (parent class).

### **Code:**
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited method
d.bark()   # Own method
```

### **Output:**
```
Animal speaks
Dog barks
```

---

## **7. Method Overriding**
Method overriding allows a child class to redefine a method of its parent class.

### **Code:**
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()

d = Dog()
d.speak()
```

### **Output:**
```
Animal makes a sound
Dog barks
```

---
