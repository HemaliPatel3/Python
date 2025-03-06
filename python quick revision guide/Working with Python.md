# **Working with Python**

Python offers multiple ways to execute code, including interactive interpretation, running scripts via a terminal, and using IDEs like Eclipse. Below are explanations and examples for **working with the Python interpreter, running Python files from the terminal, and working with Eclipse IDE**.

---

## **1. Working with Python Interpreter**
- The Python interpreter allows users to execute Python commands interactively.
- You can open the interpreter by simply running `python` or `python3` in the terminal.

### **Example (Opening Python Interpreter in Terminal)**
1. Open **Command Prompt (Windows)** or **Terminal (Linux/macOS)**.
2. Type:
   ```
   python
   ```
   or  
   ```
   python3
   ```
3. The interactive shell will start, and you can enter Python commands.

### **Example Code in the Python Interpreter:**
```python
>>> print("Hello, Python Interpreter!")
Hello, Python Interpreter!
>>> x = 5
>>> x * 2
10
```

---

## **2. Running a Python File from the Terminal**
- Python scripts (`.py` files) can be executed from the terminal.
- This is useful for running full programs instead of interactive execution.

### **Steps to Run a Python File in the Terminal:**
1. Create a Python file, e.g., **`script.py`** with the following content:
```python
print("Hello from script.py")
```
2. Open **Command Prompt (Windows)** or **Terminal (Linux/macOS)**.
3. Navigate to the directory where the script is located using `cd`:
   ```
   cd path/to/your/script
   ```
4. Run the script using:
   ```
   python script.py
   ```
   or  
   ```
   python3 script.py
   ```

### **Output:**
```
Hello from script.py
```

---

## **3. Working with Eclipse IDE**
- **Eclipse** is an Integrated Development Environment (IDE) used for Python development with the **PyDev** plugin.
- It provides **code suggestions, debugging, and an interactive console**.

### **Setting Up Python in Eclipse (PyDev)**
1. Download and install **Eclipse IDE** from [eclipse.org](https://www.eclipse.org/downloads/).
2. Open Eclipse and go to **Help → Eclipse Marketplace**.
3. Search for **PyDev** and install it.
4. Go to **Window → Preferences → PyDev → Interpreters → Python Interpreter**.
5. Click **New** and add the path to `python.exe` or `python3` (depending on OS).
6. Create a new Python project:
   - Go to **File → New → Project → PyDev Project**.
   - Set a project name and select the Python interpreter.
   - Create a new Python file inside the project.
7. Write Python code and run it using **Run → Run As → Python Run**.

### **Example Code in Eclipse (PyDev):**
```python
print("Hello from Eclipse IDE!")
```

### **Output (Shown in Eclipse Console):**
```
Hello from Eclipse IDE!
```

---

## **Summary**
| Method                        | Description | Example Command |
|-------------------------------|-------------|----------------|
| **Python Interpreter** | Interactive Python execution | `python` → `print("Hello!")` |
| **Running a Python File** | Executes a `.py` file via terminal | `python script.py` |
| **Eclipse IDE (PyDev)** | Provides an IDE for development | `Run → Run As → Python Run` |
