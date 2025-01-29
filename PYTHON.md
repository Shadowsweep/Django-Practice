# Python Basics 🚀

## 📌 Table of Contents
1. [Indentation](#indentation)
2. [Comments](#comments)
3. [Variables & Data Types](#variables--data-types)
4. [Print Statement](#print-statement)
5. [User Input](#user-input)
6. [Conditional Statements](#conditional-statements)
7. [Loops](#loops)
8. [Functions](#functions)
9. [Exception Handling](#exception-handling)
10. [Importing Modules](#importing-modules)

---

## 1️⃣ Indentation
```python
if True:
    print("This is indented correctly")
    print("Python uses indentation instead of {}")
```

## 2️⃣ Comments
```python
# This is a single-line comment

''' 
This is a multi-line comment.
It can span multiple lines.
'''
```

## 3️⃣ Variables & Data Types
```python
name = "Alice"   # String
age = 25         # Integer
height = 5.6     # Float
is_active = True # Boolean
```

## 4️⃣ Print Statement
```python
print("Hello, World!")
print("Age:", age)
```

## 5️⃣ User Input
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name)
```

## 6️⃣ Conditional Statements
```python
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
```

## 7️⃣ Loops
### (A) `for` Loop
```python
for i in range(1, 6):
    print(i)
```

### (B) `while` Loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### (C) `break` and `continue`
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

## 8️⃣ Functions
```python
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
```

## 9️⃣ Exception Handling
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
```

## 🔟 Importing Modules
```python
import math
print(math.sqrt(16))
```

```python
from math import sqrt
print(sqrt(25))
