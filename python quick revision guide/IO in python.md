# **1. Input**
The `input()` function allows users to provide input from the keyboard. The input is always received as a string unless explicitly converted.

### **Code:**
```python
name = input("Enter your name: ")
print("Hello,", name)
```

### **Example Input and Output:**
```
Enter your name: Alice
Hello, Alice
```

---

## **2. Print**
The `print()` function is used to display output to the console.

### **Code:**
```python
name = "Bob"
age = 25
print("Name:", name)
print("Age:", age)
print(f"Hello, my name is {name} and I am {age} years old.")
```

### **Output:**
```
Name: Bob
Age: 25
Hello, my name is Bob and I am 25 years old.
```

---

## **3. Pickle (Serialization and Deserialization)**
The `pickle` module is used for serializing (saving) and deserializing (loading) Python objects. This is useful for storing complex objects such as lists, dictionaries, or custom classes.

### **Code (Saving an Object using Pickle):**
```python
import pickle

data = {"name": "Alice", "age": 30, "city": "New York"}

# Saving data to a file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

print("Data saved successfully!")
```

### **Output:**
```
Data saved successfully!
```

---

### **Code (Loading an Object using Pickle):**
```python
import pickle

# Loading data from a file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print("Loaded Data:", loaded_data)
```

### **Output:**
```
Loaded Data: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

---

### **Summary**
- **`input()`** → Accepts user input as a string.
- **`print()`** → Displays output on the console.
- **`pickle`** → Used for serializing and deserializing Python objects.
