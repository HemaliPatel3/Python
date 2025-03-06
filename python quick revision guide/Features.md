# **Features of Python**  
Python is a powerful programming language with several features that make it popular for developers. Below are explanations of **Simple, Easy to use, Free and open source, Portable, Interpreted, Scalable, and Extensive Libraries**, along with examples.

---

## **1. Simple**  
Python has a clean and readable syntax that resembles natural language, making it easy to understand and use.

### **Example Code:**  
```python
print("Hello, Python is simple!")
```

### **Output:**  
```
Hello, Python is simple!
```

---

## **2. Easy to Use**  
Python has a straightforward syntax, requiring fewer lines of code to perform a task compared to other languages like Java or C++.

### **Example Code (Swapping two numbers):**  
```python
a, b = 5, 10
a, b = b, a  # Swapping without a temp variable
print("a =", a, ", b =", b)
```

### **Output:**  
```
a = 10 , b = 5
```

---

## **3. Free and Open Source**  
Python is freely available and open-source, meaning anyone can use, modify, and distribute it.

### **Example Code (Checking Python License):**  
```python
import sys
print(sys.version)
```

### **Output (varies by version):**  
```
3.10.0 (default, Oct  5 2021, 20:29:47) 
[GCC 7.5.0]
```

---

## **4. Portable**  
Python code can be run on multiple operating systems like Windows, macOS, and Linux without modification.

### **Example Code:**  
```python
import platform
print("Running on:", platform.system())
```

### **Output (depends on OS):**  
```
Running on: Windows
```
or  
```
Running on: Linux
```

---

## **5. Interpreted**  
Python does not require compilation; it is executed line-by-line, making debugging easier.

### **Example Code:**  
```python
print("First Line")
print("Second Line")
print("Python executes line by line!")
```

### **Output:**  
```
First Line
Second Line
Python executes line by line!
```

---

## **6. Scalable**  
Python is scalable and is used in **small scripts** as well as **large applications** like YouTube and Instagram.

### **Example Code (Simple Web Server using Flask):**  
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Python is scalable!"

if __name__ == "__main__":
    app.run(debug=True)
```
(Runs a web server that displays "Python is scalable!")

---

## **7. Extensive Libraries**  
Python has a vast collection of built-in libraries and third-party modules for various tasks like data science, machine learning, and web development.

### **Example Code (Using `math` library):**  
```python
import math
print("Square root of 25 is:", math.sqrt(25))
```

### **Output:**  
```
Square root of 25 is: 5.0
```

---

## **Summary of Python Features**
| Feature                 | Description | Example |
|-------------------------|-------------|---------|
| **Simple**              | Easy-to-read syntax | `print("Hello, Python!")` |
| **Easy to use**         | Requires fewer lines of code | `a, b = b, a` |
| **Free and open-source** | Available for everyone | `import sys; print(sys.version)` |
| **Portable**            | Runs on multiple OS | `import platform; print(platform.system())` |
| **Interpreted**         | Executes line by line | `print("Python executes line by line!")` |
| **Scalable**            | Used in small and large projects | `Flask web server` |
| **Extensive Libraries** | Provides built-in modules | `import math; math.sqrt(25)` |
