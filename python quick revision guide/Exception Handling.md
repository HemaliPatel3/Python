# **Exception Handling in Python**

Python provides a way to handle runtime errors using **exception handling**, preventing the program from crashing unexpectedly. Below are detailed explanations with example codes and outputs.

---

## **1. Errors**
Errors in Python are categorized as:
- **Syntax Errors**: Occur due to incorrect syntax.
- **Runtime Errors (Exceptions)**: Occur during program execution (e.g., division by zero, accessing an undefined variable).

### **Example Code:**
```python
# Syntax Error (Uncomment to see the error)
# print("Hello"  # Missing closing parenthesis

# Runtime Error
x = 10 / 0  # Division by zero
print(x)
```

### **Output (Error Message):**
```
ZeroDivisionError: division by zero
```

---

## **2. try – except – else**
- **`try`**: Code that may cause an exception is placed inside a `try` block.
- **`except`**: Handles the exception if an error occurs.
- **`else`**: Executes only if there is no exception.

### **Example Code:**
```python
try:
    num = int(input("Enter a number: "))  # User input
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)  # Only runs if no error occurs
```

### **Example Input & Output:**
```
Enter a number: 5
Result: 2.0
```
```
Enter a number: 0
Cannot divide by zero!
```

---

## **3. User-defined Exceptions**
Python allows users to define custom exceptions using the `Exception` class.

### **Example Code:**
```python
class NegativeNumberError(Exception):
    pass  # Custom exception class

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print("You entered:", num)
except NegativeNumberError as e:
    print("Error:", e)
```

### **Example Input & Output:**
```
Enter a positive number: -3
Error: Negative numbers are not allowed!
```
```
Enter a positive number: 7
You entered: 7
```

---

## **4. try – except – finally**
- **`finally`**: The `finally` block always executes, whether an exception occurs or not.

### **Example Code:**
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")  # Always executes
```

### **Example Input & Output:**
```
Enter a number: 2
Execution completed.
```
```
Enter a number: 0
Cannot divide by zero!
Execution completed.
```

---

### **Summary**
- **Errors**: Syntax and runtime errors occur due to incorrect code execution.
- **try – except – else**: Handles exceptions and executes `else` when there is no error.
- **User-defined exceptions**: Custom exceptions are created by inheriting the `Exception` class.
- **try – except – finally**: Ensures a block of code runs regardless of exceptions.
