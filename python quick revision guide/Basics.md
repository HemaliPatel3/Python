# **Python Basics**  

Below are explanations and examples of key Python basics: **Explicit Line Joining, Escape Sequences, Indentation, Undefined Variables, Single Statement Coding, and the `dir()` Method**.

---

## **1. Explicit Line Joining**
- In Python, statements usually end at a newline.
- You can use a **backslash (`\`)** to continue a statement on the next line.

### **Example Code:**
```python
long_string = "This is an example of " \
              "explicit line joining in Python."
print(long_string)
```

### **Output:**
```
This is an example of explicit line joining in Python.
```

---

## **2. Escape Sequences**
- Escape sequences allow you to insert special characters in a string.
- Common escape sequences:
  - `\n` → Newline
  - `\t` → Tab space
  - `\\` → Backslash
  - `\'` → Single quote
  - `\"` → Double quote

### **Example Code:**
```python
print("Hello\nPython\tWorld!")
print("He said, \"Python is awesome!\"")
```

### **Output:**
```
Hello
Python    World!
He said, "Python is awesome!"
```

---

## **3. Indentation**
- Python uses indentation to define code blocks instead of `{}` (curly brackets).
- Incorrect indentation will cause an **IndentationError**.

### **Example Code (Correct Indentation):**
```python
def greet():
    print("Hello!")  # Indented block
    print("Welcome to Python.")  

greet()
```

### **Output:**
```
Hello!
Welcome to Python.
```

### **Example Code (Incorrect Indentation - Will cause an error):**
```python
def greet():
print("Hello!")  # Missing indentation
```

### **Error:**
```
IndentationError: expected an indented block
```

---

## **4. Undefined Variables**
- An **undefined variable** is a variable that has not been assigned a value before use.
- Python will raise a **NameError** if an undefined variable is accessed.

### **Example Code (Error Case):**
```python
print(value)  # 'value' is not defined
```

### **Error Output:**
```
NameError: name 'value' is not defined
```

### **Example Code (Fixing the Error):**
```python
value = 10
print(value)
```

### **Output:**
```
10
```

---

## **5. Single Statement Coding**
- Python allows writing single-line statements using semicolons (`;`).
- This is useful for short, simple commands.

### **Example Code:**
```python
a = 10; b = 20; print(a + b)
```

### **Output:**
```
30
```

---

## **6. `dir()` Method**
- `dir()` returns a list of all attributes (methods, variables, etc.) available for an object.
- It is useful for exploring built-in functions of an object.

### **Example Code:**
```python
print(dir(str))  # Lists all methods available for string objects
```

### **Output (Partial List):**
```
['capitalize', 'casefold', 'center', 'count', 'encode', ...]
```

---

## **Summary**
| Concept                     | Description | Example |
|-----------------------------|-------------|---------|
| **Explicit Line Joining**   | Continue a statement across multiple lines using `\` | `"Hello " \ "World"` |
| **Escape Sequences**        | Special characters like `\n`, `\t`, `\\`, `\"` | `"Hello\nPython!"` |
| **Indentation**             | Python uses indentation instead of `{}` | `def func():\n    print("Hello")` |
| **Undefined Variables**     | Using a variable before defining it causes a `NameError` | `print(x) # Error` |
| **Single Statement Coding** | Write multiple statements in a single line using `;` | `a = 5; b = 10; print(a+b)` |
| **`dir()` Method**          | Lists all available attributes of an object | `dir(str)` |
