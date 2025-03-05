# **Database Connectivity in Python**
Python provides libraries such as `psycopg2` for **PostgreSQL** and `mysql-connector-python` for **MySQL** to interact with databases. Below are explanations with example codes for **connecting, accessing, and updating records** in both PostgreSQL and MySQL.

---

## **1. Connecting with Databases (PostgreSQL & MySQL)**
To connect to a database, we need:
- **Host** (Database server address)
- **Database name**
- **User & Password**
- **Port** (Default: PostgreSQL `5432`, MySQL `3306`)

### **PostgreSQL Connection Example (`psycopg2`)**
```python
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    print("Connected to PostgreSQL successfully!")
    conn.close()  # Close the connection
except Exception as e:
    print("Error:", e)
```

### **MySQL Connection Example (`mysql-connector-python`)**
```python
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="testdb"
    )
    print("Connected to MySQL successfully!")
    conn.close()  # Close the connection
except Exception as e:
    print("Error:", e)
```

### **Expected Output (Both)**
```
Connected to PostgreSQL successfully!
```
or
```
Connected to MySQL successfully!
```

---

## **2. Accessing Records (SELECT Query)**
After connecting, we can retrieve data using the `SELECT` statement.

### **PostgreSQL Example**
```python
import psycopg2

conn = psycopg2.connect(dbname="testdb", user="postgres", password="password", host="localhost", port="5432")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")  # Fetch all records
records = cursor.fetchall()

for row in records:
    print(row)

conn.close()
```

### **MySQL Example**
```python
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="password", database="testdb")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")  # Fetch all records
records = cursor.fetchall()

for row in records:
    print(row)

conn.close()
```

### **Example Output (Assuming Sample Data in `employees` Table)**
```
(1, 'Alice', 'HR', 3000)
(2, 'Bob', 'IT', 4500)
```

---

## **3. Updating Records (UPDATE Query)**
We can update records using the `UPDATE` SQL statement.

### **PostgreSQL Example**
```python
import psycopg2

conn = psycopg2.connect(dbname="testdb", user="postgres", password="password", host="localhost", port="5432")
cursor = conn.cursor()

cursor.execute("UPDATE employees SET salary = 5000 WHERE name = 'Alice'")
conn.commit()  # Commit changes
print("Record Updated!")

conn.close()
```

### **MySQL Example**
```python
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="password", database="testdb")
cursor = conn.cursor()

cursor.execute("UPDATE employees SET salary = 5000 WHERE name = 'Alice'")
conn.commit()  # Commit changes
print("Record Updated!")

conn.close()
```

### **Expected Output**
```
Record Updated!
```

---

## **Summary**
| Operation          | PostgreSQL (`psycopg2`) | MySQL (`mysql-connector-python`) |
|--------------------|-----------------------|-------------------------------|
| **Connecting**     | `psycopg2.connect()`   | `mysql.connector.connect()`  |
| **Accessing Data** | `SELECT * FROM table`  | `SELECT * FROM table`        |
| **Updating Data**  | `UPDATE table SET ...` | `UPDATE table SET ...`       |
