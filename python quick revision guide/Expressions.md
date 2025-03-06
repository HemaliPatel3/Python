# **Expressions in Python**  

Expressions in Python combine **variables, literals, and operators** to produce a result. There are three key types of expressions:  

1. **Variable Expressions**  
2. **Literal Expressions**  
3. **Heterogeneous Expressions**  

---

## **1. Variable Expressions**  
- A **variable expression** consists of variables combined with operators to create meaningful computations.  
- The variables **store values** and are used in expressions to perform operations.  

### **Example Code:**
```python
a = 10
b = 5
result = a * b + 2  # Using variables in an expression
print("Variable Expression Result:", result)
```

### **Output:**
```
Variable Expression Result: 52
```

---

## **2. Literal Expressions**  
- **Literals** are fixed values written directly in code, such as **numbers, strings, booleans, and lists**.  
- A **literal expression** consists of only literals without variables.  

### **Example Code:**
```python
result = 5 * 2 + 3  # Only using fixed values (literals)
print("Literal Expression Result:", result)
```

### **Output:**
```
Literal Expression Result: 13
```

---

## **3. Heterogeneous Expressions**  
- A **heterogeneous expression** contains a **mix of variables, literals, and different data types** (numbers, strings, booleans, etc.).  
- Python allows automatic **type conversion** when required.  

### **Example Code:**
```python
name = "Alice"
age = 25
is_adult = age > 18  # Boolean expression

message = name + " is " + str(age) + " years old. Adult: " + str(is_adult)
print("Heterogeneous Expression Result:", message)
```

### **Output:**
```
Heterogeneous Expression Result: Alice is 25 years old. Adult: True
```

---

## **Summary**
| Expression Type | Description | Example |
|---------------|-------------|---------|
| **Variable Expression** | Uses variables in operations | `x + y * 2` |
| **Literal Expression** | Uses fixed values | `5 * 3 + 2` |
| **Heterogeneous Expression** | Mix of variables, literals, and data types | `"Age: " + str(25)` |
