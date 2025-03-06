# **Python Operators**  

Operators in Python are used to perform operations on variables and values. The key types of operators include **Arithmetic, Bitwise, Relational (Comparison), and Logical Operators**.

---

## **1. Arithmetic Operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`)**  
These operators perform basic mathematical operations.

### **Example Code:**
```python
a = 10
b = 3

print("Addition:", a + b)     # 10 + 3 = 13
print("Subtraction:", a - b)  # 10 - 3 = 7
print("Multiplication:", a * b)  # 10 * 3 = 30
print("Division:", a / b)     # 10 / 3 = 3.3333
print("Exponentiation:", a ** b)  # 10^3 = 1000
print("Floor Division:", a // b)  # 10 // 3 = 3
print("Modulus:", a % b)      # 10 % 3 = 1
```

### **Output:**
```
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Exponentiation: 1000
Floor Division: 3
Modulus: 1
```

---

## **2. Bitwise Operators (`<<`, `>>`, `&`, `|`, `~`, `^`)**  
Bitwise operators work at the **binary level** (bit-by-bit operations).

### **Example Code:**
```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011

print("Bitwise AND:", x & y)  # 0101 & 0011 = 0001 (1)
print("Bitwise OR:", x | y)   # 0101 | 0011 = 0111 (7)
print("Bitwise XOR:", x ^ y)  # 0101 ^ 0011 = 0110 (6)
print("Bitwise NOT (~x):", ~x)  # ~0101 = -(0101 + 1) = -6
print("Left Shift:", x << 1)  # 0101 << 1 = 1010 (10)
print("Right Shift:", x >> 1) # 0101 >> 1 = 0010 (2)
```

### **Output:**
```
Bitwise AND: 1
Bitwise OR: 7
Bitwise XOR: 6
Bitwise NOT (~x): -6
Left Shift: 10
Right Shift: 2
```

---

## **3. Relational (Comparison) Operators (`<`, `>`, `<=`, `>=`, `==`, `!=`, `is`, `is not`)**  
These operators **compare values** and return a **Boolean (`True` or `False`)**.

### **Example Code:**
```python
a = 10
b = 20

print("a < b:", a < b)   # True
print("a > b:", a > b)   # False
print("a <= b:", a <= b) # True
print("a >= b:", a >= b) # False
print("a == b:", a == b) # False
print("a != b:", a != b) # True

# `is` and `is not` compare object identity (memory location)
x = [1, 2, 3]
y = x  # `y` points to the same list as `x`
z = [1, 2, 3]  # `z` is a separate list with the same values

print("x is y:", x is y)   # True (same object)
print("x is not z:", x is not z)  # True (different objects)
```

### **Output:**
```
a < b: True
a > b: False
a <= b: True
a >= b: False
a == b: False
a != b: True
x is y: True
x is not z: True
```

---

## **4. Logical Operators (`and`, `or`, `not`)**  
Logical operators are used to combine conditional statements.

### **Example Code:**
```python
x = True
y = False

print("x and y:", x and y)  # False (both must be True)
print("x or y:", x or y)    # True (at least one is True)
print("not x:", not x)      # False (negates True)
```

### **Output:**
```
x and y: False
x or y: True
not x: False
```

---

## **Summary**
| Operator Type | Operators | Description |
|--------------|-----------|-------------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `**`, `//`, `%` | Basic math operations |
| **Bitwise** | `<<`, `>>`, `&`, `|`, `~`, `^` | Operate on binary values |
| **Relational (Comparison)** | `<`, `>`, `<=`, `>=`, `==`, `!=`, `is`, `is not` | Compare values or object identity |
| **Logical** | `and`, `or`, `not` | Combine conditions |
