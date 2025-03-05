# **Python Standard Library Modules**
The Python standard library provides several built-in modules that help in performing various tasks efficiently. Below is a brief explanation along with example codes and outputs for each module.

---

## **1. sys (System-specific Parameters and Functions)**
The `sys` module provides access to system-specific parameters and functions, such as command-line arguments and system paths.

### **Example Code:**
```python
import sys

print("Python Version:", sys.version)
print("Platform:", sys.platform)
```

### **Output:**
```
Python Version: 3.x.x (varies by installation)
Platform: win32 (or linux/macOS depending on your system)
```

---

## **2. os (Operating System Interface)**
The `os` module allows interaction with the operating system, such as file handling, environment variables, and directory manipulation.

### **Example Code:**
```python
import os

print("Current Working Directory:", os.getcwd())
print("List of files in current directory:", os.listdir("."))
```

### **Output:**
```
Current Working Directory: /Users/username/project
List of files in current directory: ['file1.py', 'file2.txt', 'folder']
```

---

## **3. platform (System Information)**
The `platform` module provides information about the system, such as OS, processor, and architecture.

### **Example Code:**
```python
import platform

print("System:", platform.system())
print("Release:", platform.release())
print("Processor:", platform.processor())
```

### **Output:**
```
System: Windows
Release: 10
Processor: Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
```

---

## **4. logging (Logging Messages)**
The `logging` module is used for debugging and logging system messages.

### **Example Code:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
```

### **Output:**
```
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
```

---

## **5. re (Regular Expressions)**
The `re` module provides functions for pattern matching using regular expressions.

### **Example Code:**
```python
import re

text = "My email is example@example.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

match = re.search(pattern, text)
if match:
    print("Found Email:", match.group())
else:
    print("No email found.")
```

### **Output:**
```
Found Email: example@example.com
```

---

## **6. time (Time-related Functions)**
The `time` module provides functions for handling time-related operations, such as delays and timestamps.

### **Example Code:**
```python
import time

print("Current Time (Epoch):", time.time())
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake now!")
```

### **Output:**
```
Current Time (Epoch): 1709658856.548755
Sleeping for 2 seconds...
Awake now!
```

---

## **7. datetime (Date and Time Handling)**
The `datetime` module helps in working with dates and times.

### **Example Code:**
```python
from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
```

### **Output:**
```
Current Date and Time: 2025-03-05 14:30:00
```

---

## **8. random (Random Number Generation)**
The `random` module is used for generating random numbers, selecting random elements, and shuffling sequences.

### **Example Code:**
```python
import random

print("Random Number (1-100):", random.randint(1, 100))
print("Random Choice from List:", random.choice(["apple", "banana", "cherry"]))
```

### **Output:**
```
Random Number (1-100): 42
Random Choice from List: banana
```

---

### **Summary**
- **`sys`**: System-specific functions (e.g., Python version, platform details).
- **`os`**: Operating system interactions (e.g., directory listing, file paths).
- **`platform`**: Retrieves system and hardware details.
- **`logging`**: Logs messages for debugging and error tracking.
- **`re`**: Regular expressions for pattern matching.
- **`time`**: Time-related functions like sleep and timestamps.
- **`datetime`**: Date and time handling.
- **`random`**: Generates random numbers and selections.
