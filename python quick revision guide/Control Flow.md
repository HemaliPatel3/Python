# **Control Flow in Python**  

Control flow structures help determine the sequence in which code executes. Python provides several control flow statements, including conditional (`if-elif-else`) and loop constructs (`while`, `for`, `break`, `continue`).

---

## **1. `if – elif – else`**  
- Used for **decision-making**.
- Checks conditions and executes corresponding blocks of code.

### **Example Code:**
```python
num = 10

if num > 10:
    print("Number is greater than 10")
elif num == 10:
    print("Number is exactly 10")
else:
    print("Number is less than 10")
```

### **Output:**
```
Number is exactly 10
```

---

## **2. `while – else`**  
- `while` loop runs as long as the condition is **True**.
- The `else` block executes when the loop condition becomes **False** (not exited via `break`).

### **Example Code:**
```python
x = 3
while x > 0:
    print("x =", x)
    x -= 1
else:
    print("Loop ended naturally")
```

### **Output:**
```
x = 3
x = 2
x = 1
Loop ended naturally
```

---

## **3. `for – else`**  
- `for` loop iterates over a sequence.
- The `else` block runs **only if the loop completes without `break`**.

### **Example Code:**
```python
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop completed successfully")
```

### **Output:**
```
Iteration: 0
Iteration: 1
Iteration: 2
Loop completed successfully
```

---

## **4. `break`**  
- **Terminates** the loop immediately.
- Prevents execution of the `else` block (if present).

### **Example Code:**
```python
for i in range(5):
    if i == 3:
        print("Breaking at:", i)
        break
    print(i)
else:
    print("Loop completed")

```

### **Output:**
```
0
1
2
Breaking at: 3
```

---

## **5. `continue`**  
- **Skips** the current iteration and proceeds to the next.

### **Example Code:**
```python
for i in range(5):
    if i == 2:
        print("Skipping", i)
        continue
    print("Processing", i)
```

### **Output:**
```
Processing 0
Processing 1
Skipping 2
Processing 3
Processing 4
```

---

## **Summary**
| Control Flow | Description | Example |
|--------------|-------------|---------|
| **`if-elif-else`** | Conditional execution | `if x > 5: print("Yes")` |
| **`while-else`** | Loops with a final block | `while x > 0: x -= 1 else: print("Done")` |
| **`for-else`** | Iteration with a final block | `for x in range(5): print(x) else: print("Done")` |
| **`break`** | Exits the loop early | `if x == 3: break` |
| **`continue`** | Skips to the next iteration | `if x == 3: continue` |
