# **Basic Datatypes in Python**  

Python provides several built-in datatypes, including **Strings, Integers, Floats, Booleans, and Type Conversions**. Below are explanations, example codes, and their outputs.

---

## **1. Strings (`str`)**  
- A **string** is a sequence of characters enclosed in **single (`'`), double (`"`), or triple (`'''` or `"""`) quotes**.
- Strings are **immutable**, meaning they cannot be changed after creation.

### **Example Code:**
```python
text = "Hello, Python!"
print(text)
print(type(text))  # Checking the data type
```

### **Output:**
```
Hello, Python!
<class 'str'>
```

---

## **2. Integer (`int`)**  
- An **integer** is a whole number without a decimal point.
- It can be positive or negative.

### **Example Code:**
```python
num = 100
print(num)
print(type(num))  # Checking the data type
```

### **Output:**
```
100
<class 'int'>
```

---

## **3. Float (`float`)**  
- A **float** is a number that contains a decimal point.
- Used for **precise** numerical calculations.

### **Example Code:**
```python
pi = 3.14159
print(pi)
print(type(pi))  # Checking the data type
```

### **Output:**
```
3.14159
<class 'float'>
```

---

## **4. Boolean (`bool`)**  
- A **Boolean** represents either **True** or **False**.
- It is commonly used in **conditional statements**.

### **Example Code:**
```python
is_python_easy = True
print(is_python_easy)
print(type(is_python_easy))  # Checking the data type
```

### **Output:**
```
True
<class 'bool'>
```

---

## **5. Type Conversions**  
- Python allows **converting** one datatype to another using built-in functions:
  - `int()` → Converts to an integer.
  - `float()` → Converts to a floating-point number.
  - `str()` → Converts to a string.
  - `bool()` → Converts to a boolean.

### **Example Code:**
```python
# Converting int to float
num = 10
num_float = float(num)
print(num_float, type(num_float))  # 10.0 <class 'float'>

# Converting float to int
pi = 3.14
pi_int = int(pi)
print(pi_int, type(pi_int))  # 3 <class 'int'>

# Converting string to int
num_str = "50"
num_int = int(num_str)
print(num_int, type(num_int))  # 50 <class 'int'>

# Converting boolean to int
is_valid = True
print(int(is_valid))  # 1
```

### **Output:**
```
10.0 <class 'float'>
3 <class 'int'>
50 <class 'int'>
1
```

---

## **Summary**
| Datatype   | Description | Example |
|------------|-------------|---------|
| **String (`str`)** | Sequence of characters enclosed in quotes | `"Hello, Python!"` |
| **Integer (`int`)** | Whole numbers without decimals | `100` |
| **Float (`float`)** | Numbers with decimal points | `3.14` |
| **Boolean (`bool`)** | Represents True or False | `True`, `False` |
| **Type Conversion** | Convert one datatype to another | `int("50") → 50` |
