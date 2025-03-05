## **1. List**
A list is an ordered, mutable collection that allows duplicate elements.

### **Code:**
```python
my_list = [10, 20, 30, 40]
print("List:", my_list)
my_list.append(50)
print("Updated List:", my_list)
```

### **Output:**
```
List: [10, 20, 30, 40]
Updated List: [10, 20, 30, 40, 50]
```

---

## **2. Tuple**
A tuple is an ordered, immutable collection that allows duplicate elements.

### **Code:**
```python
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)
```

### **Output:**
```
Tuple: (1, 2, 3, 4)
```

---

## **3. Dictionary**
A dictionary is an unordered collection of key-value pairs.

### **Code:**
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])
```

### **Output:**
```
Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
Name: Alice
```

---

## **4. Set**
A set is an unordered collection of unique elements.

### **Code:**
```python
my_set = {1, 2, 3, 4, 4, 5}
print("Set:", my_set)  # Duplicates are removed
```

### **Output:**
```
Set: {1, 2, 3, 4, 5}
```

---

## **5. Type Conversion**
Type conversion allows converting one data type into another.

### **Code:**
```python
num = "100"
converted_num = int(num)  # String to Integer
print("Converted Number:", converted_num, "Type:", type(converted_num))
```

### **Output:**
```
Converted Number: 100 Type: <class 'int'>
```

---

## **6. Indexing**
Indexing is used to access elements in lists, tuples, and strings.

### **Code:**
```python
my_list = ['a', 'b', 'c', 'd']
print("First element:", my_list[0])
print("Last element:", my_list[-1])
```

### **Output:**
```
First element: a
Last element: d
```

---

## **7. String and Indexing**
Strings are sequences of characters and can be accessed using indexing.

### **Code:**
```python
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])
```

### **Output:**
```
First character: P
Last character: n
```

---

## **8. Looping Without Index**
Looping through a list without using an index.

### **Code:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### **Output:**
```
apple
banana
cherry
```

---

## **9. `in` and `not in` Operators**
These operators check for membership in sequences like lists, tuples, and strings.

### **Code:**
```python
fruits = ["apple", "banana", "cherry"]
print("banana in list?", "banana" in fruits)
print("grape not in list?", "grape" not in fruits)
```

### **Output:**
```
banana in list? True
grape not in list? True
```

---

## **10. Slicing Using `:` & `::`**
Slicing extracts portions of lists, tuples, or strings.

### **Code:**
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print("Slice [2:5]:", my_list[2:5])  # Elements from index 2 to 4
print("Slice with step [::2]:", my_list[::2])  # Every second element
```

### **Output:**
```
Slice [2:5]: [2, 3, 4]
Slice with step [::2]: [0, 2, 4, 6]
```
