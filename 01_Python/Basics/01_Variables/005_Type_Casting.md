# ===================================================
# Topic: Type Casting
# Category: Python Basics
# Difficulty: ⭐⭐☆☆☆
# Interview Importance: ⭐⭐⭐⭐⭐
# ===================================================

# 1. Introduction

## What is Type Casting?

Type casting is the process of converting a value from one data type to another.

Python provides built-in functions to perform explicit type conversions.

### Why is Type Casting Important?

Type casting is useful when:

- Reading user input
- Processing files
- Performing mathematical operations
- Converting data from APIs or databases
- Cleaning and transforming data

### Real-World Example

```python
age = input("Enter your age: ")

print(age + 5)
```

This raises an error because `input()` returns a string.

Correct:

```python
age = int(input("Enter your age: "))

print(age + 5)
```

---

# 2. Characteristics

- Python is dynamically typed.
- Type casting converts one type into another.
- Can be explicit or implicit.
- Some conversions may fail.
- Invalid conversions raise exceptions.

---

# 3. Syntax

General Syntax

```python
type_name(value)
```

Examples

```python
int("10")

float("10.5")

str(100)

bool(1)
```

---

# 4. Types of Type Casting

Python supports two types of type conversion.

## 4.1 Implicit Type Casting

Python automatically converts compatible data types.

Example

```python
a = 10
b = 2.5

print(a + b)
```

Output

```text
12.5
```

Python converts `10` into `10.0` automatically.

---

## 4.2 Explicit Type Casting

The programmer manually converts the data type.

Example

```python
num = "100"

num = int(num)

print(num)
```

Output

```text
100
```

---

# 5. Common Type Casting Functions

## int()

Converts a value to an integer.

```python
int(10.8)

int("50")
```

Output

```text
10

50
```

---

## float()

Converts a value to a floating-point number.

```python
float(10)

float("12.5")
```

Output

```text
10.0

12.5
```

---

## str()

Converts a value to a string.

```python
str(100)

str(True)
```

Output

```text
'100'

'True'
```

---

## bool()

Converts a value to a Boolean.

```python
bool(1)

bool(0)

bool("")
```

Output

```text
True

False

False
```

---

## list()

Converts an iterable into a list.

```python
list("Python")
```

Output

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

## tuple()

```python
tuple([1,2,3])
```

Output

```text
(1,2,3)
```

---

## set()

```python
set([1,2,2,3])
```

Output

```text
{1,2,3}
```

---

# 6. Examples

## String to Integer

```python
age = "25"

age = int(age)

print(age + 5)
```

---

## Integer to String

```python
roll = 101

print("Roll No: " + str(roll))
```

---

## Float to Integer

```python
price = 99.99

print(int(price))
```

Output

```text
99
```

---

## Integer to Float

```python
marks = 95

print(float(marks))
```

Output

```text
95.0
```

---

## List to Set

```python
nums = [1,2,2,3,3]

print(set(nums))
```

Output

```text
{1,2,3}
```

---

# 7. Performance Notes

Most primitive type conversions (`int`, `float`, `str`, `bool`) are **O(1)**.

Conversions involving collections depend on the number of elements.

| Conversion | Complexity |
|------------|------------|
| int() | O(1) |
| float() | O(1) |
| str() | O(1)* |
| bool() | O(1) |
| list(iterable) | O(n) |
| tuple(iterable) | O(n) |
| set(iterable) | O(n) |

\* Converting very large objects to strings depends on their size.

---

# 8. Memory Considerations

- Type casting creates a new object.
- The original object is unchanged.
- Collection conversions allocate new memory.
- Avoid unnecessary conversions inside loops.

---

# 9. Interview Insights 💡

### Why does `input()` always return a string?

Because Python treats user input as text by default.

Always convert it if numeric operations are needed.

---

### What happens here?

```python
int(True)
```

Output

```text
1
```

---

### What happens here?

```python
bool("False")
```

Output

```text
True
```

Because any non-empty string is Truthy.

---

### Difference between

```python
int(5.9)
```

and

```python
round(5.9)
```

`int()` truncates the decimal part, while `round()` rounds to the nearest integer.

---

# 10. Common Mistakes ❌

## Invalid Integer Conversion

Wrong

```python
int("10.5")
```

Raises

```text
ValueError
```

Correct

```python
int(float("10.5"))
```

---

## Forgetting to Convert Input

Wrong

```python
age = input()

print(age + 5)
```

Correct

```python
age = int(input())

print(age + 5)
```

---

## Assuming bool("False") is False

```python
bool("False")
```

Output

```text
True
```

Because the string is not empty.

---

# 11. Best Practices ✅

- Convert data only when necessary.
- Validate user input before conversion.
- Handle exceptions for invalid conversions.
- Avoid repeated type casting in loops.
- Choose the correct conversion function for the situation.

---

# 12. Cheat Sheet 📌

| Task | Code |
|------|------|
| String → Integer | `int("10")` |
| String → Float | `float("10.5")` |
| Integer → String | `str(100)` |
| Integer → Float | `float(10)` |
| Value → Boolean | `bool(value)` |
| String → List | `list("Python")` |
| List → Tuple | `tuple(lst)` |
| List → Set | `set(lst)` |

---

# 13. Related Topics 🔗

```
Integers
     ↓
Strings
     ↓
Operators
     ↓
Booleans
     ↓
Type Casting
     ↓
Floats
     ↓
None
```

Next:

```
Type Casting
      ↓
Conditional Statements
```

---

# 14. Practice Questions 📝

## Easy

1. What is type casting?
2. What is the difference between implicit and explicit type casting?
3. What does `bool(0)` return?

---

## Medium

1. Explain why `input()` returns a string.
2. What is the difference between `int()` and `float()`?
3. Explain `bool("False")`.

---

## Hard

1. Why does `int("10.5")` raise an error?
2. Explain the memory implications of type casting collections.
3. Compare implicit and explicit type conversion with examples.

---

# 15. Revision Summary 🚀

- Type casting converts one data type into another.
- Python supports implicit and explicit type conversion.
- `input()` always returns a string.
- `bool()` follows Truthy and Falsy rules.
- Invalid conversions raise exceptions.
- Collection conversions require O(n) time.
- Validate input before conversion.