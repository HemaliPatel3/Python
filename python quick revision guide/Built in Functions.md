# **Python Built-in Functions**  
Python provides several built-in functions that simplify tasks like mathematical operations, condition checking, and data processing. Below are explanations and examples for **`any`, `all`, `round`, `abs`, `max`, `min`, `divmod`, `eval`, `filter`, `map`, and `reduce`**.

---

## **1. any()**
- Returns `True` if at least **one** element in an iterable is `True`, otherwise returns `False`.

### **Example Code:**
```python
values = [0, 0, 1, 0]
print(any(values))  # True (since there's at least one `1`)
```

### **Output:**
```
True
```

---

## **2. all()**
- Returns `True` if **all** elements in an iterable are `True`, otherwise returns `False`.

### **Example Code:**
```python
values = [1, 1, 1, 0]
print(all(values))  # False (since `0` is present)
```

### **Output:**
```
False
```

---

## **3. round()**
- Rounds a floating-point number to the nearest integer or specified decimal places.

### **Example Code:**
```python
print(round(3.14159, 2))  # Rounds to 2 decimal places
print(round(7.5))         # Rounds to nearest integer
```

### **Output:**
```
3.14
8
```

---

## **4. abs()**
- Returns the absolute (positive) value of a number.

### **Example Code:**
```python
print(abs(-10))  # 10
print(abs(3.5))  # 3.5
```

### **Output:**
```
10
3.5
```

---

## **5. max()**
- Returns the largest value from an iterable or given values.

### **Example Code:**
```python
numbers = [5, 3, 8, 2]
print(max(numbers))  # 8
```

### **Output:**
```
8
```

---

## **6. min()**
- Returns the smallest value from an iterable or given values.

### **Example Code:**
```python
numbers = [5, 3, 8, 2]
print(min(numbers))  # 2
```

### **Output:**
```
2
```

---

## **7. divmod()**
- Returns a tuple containing **quotient and remainder** when dividing two numbers.

### **Example Code:**
```python
result = divmod(10, 3)
print(result)  # (3, 1) → 10 divided by 3 gives quotient 3 and remainder 1
```

### **Output:**
```
(3, 1)
```

---

## **8. eval()**
- Evaluates a given string as a Python expression.

### **Example Code:**
```python
expression = "5 + 10 * 2"
print(eval(expression))  # Evaluates the string expression
```

### **Output:**
```
25
```

---

## **9. filter()**
- Filters elements from an iterable based on a function that returns `True` or `False`.

### **Example Code:**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
```

### **Output:**
```
[2, 4, 6]
```

---

## **10. map()**
- Applies a function to every element in an iterable and returns a new iterable.

### **Example Code:**
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]
```

### **Output:**
```
[1, 4, 9, 16]
```

---

## **11. reduce()**
- Applies a function cumulatively to elements in an iterable to reduce them to a single value.
- `reduce()` is in the `functools` module.

### **Example Code:**
```python
from functools import reduce

numbers = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 10
```

### **Output:**
```
10
```

---

## **Summary**
| Function  | Description | Example Output |
|-----------|------------|---------------|
| **any()** | Returns `True` if at least one element is `True` | `any([0, 1, 0]) → True` |
| **all()** | Returns `True` if all elements are `True` | `all([1, 1, 0]) → False` |
| **round()** | Rounds a number to a specified decimal | `round(3.141, 2) → 3.14` |
| **abs()** | Returns absolute value | `abs(-5) → 5` |
| **max()** | Returns max value | `max([3, 8, 1]) → 8` |
| **min()** | Returns min value | `min([3, 8, 1]) → 1` |
| **divmod()** | Returns quotient & remainder | `divmod(10, 3) → (3, 1)` |
| **eval()** | Evaluates string as Python code | `eval("5+10") → 15` |
| **filter()** | Filters elements based on condition | `filter(even, [1,2,3]) → [2]` |
| **map()** | Applies function to all elements | `map(square, [1,2]) → [1,4]` |
| **reduce()** | Cumulatively applies function | `reduce(add, [1,2,3]) → 6` |
