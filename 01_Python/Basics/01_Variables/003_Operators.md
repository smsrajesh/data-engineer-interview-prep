# ===================================================
# Topic: Operators
# Category: Python Basics
# Difficulty: ⭐☆☆☆☆
# Interview Importance: ⭐⭐⭐⭐⭐
# ===================================================

# 1. Introduction

## What are Operators?

Operators are special symbols or keywords that perform operations on one or more operands (variables or values).

They are used to perform arithmetic calculations, compare values, assign values, evaluate logical conditions, manipulate bits, and check object identity or membership.

### Why are Operators Important?

Operators are used in almost every Python program.

They help us:

- Perform mathematical calculations
- Compare values
- Make decisions
- Write conditions and loops
- Manipulate data
- Build algorithms

### Real-World Example

```python
age = 24

if age >= 18:
    print("Eligible to vote")
```

Here,

- `=` is an Assignment Operator
- `>=` is a Comparison Operator

---

# 2. Characteristics

- Operate on one or more operands.
- Produce a result.
- Can return numbers, strings, or Boolean values.
- Follow operator precedence.
- Some operators create new objects, while others modify existing ones.

---

# 3. Syntax

General Syntax

```python
operand1 operator operand2
```

Examples

```python
10 + 5

age >= 18

name == "Rajesh"

x += 1
```

Unary Operator

```python
-x

not True
```

Binary Operator

```python
a + b

a == b
```

---

# 4. Types of Operators

Python provides seven major categories of operators.

| Category | Purpose |
|----------|---------|
| Arithmetic | Mathematical calculations |
| Assignment | Assign values |
| Comparison | Compare values |
| Logical | Combine conditions |
| Identity | Compare object identity |
| Membership | Check existence |
| Bitwise | Operate on binary values |

---

## 4.1 Arithmetic Operators

Used to perform mathematical operations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| + | Addition | 10 + 5 | 15 |
| - | Subtraction | 10 - 5 | 5 |
| * | Multiplication | 10 * 5 | 50 |
| / | Division | 10 / 4 | 2.5 |
| // | Floor Division | 10 // 4 | 2 |
| % | Modulus | 10 % 4 | 2 |
| ** | Exponent | 2 ** 3 | 8 |

Example

```python
a = 10
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 4.2 Assignment Operators

Assignment operators assign or update variable values.

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| = | x = 5 | Assign value |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 3 | x = x * 3 |
| /= | x /= 3 | x = x / 3 |
| //= | x //= 3 | x = x // 3 |
| %= | x %= 3 | x = x % 3 |
| **= | x **= 3 | x = x ** 3 |

Example

```python
count = 10

count += 5

print(count)
```

Output

```text
15
```

---

## 4.3 Comparison Operators

Comparison operators compare two values and always return a Boolean value (`True` or `False`).

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example

```python
10 > 5

10 == 10

10 != 5
```

Output

```text
True

True

True
```

---

## 4.4 Logical Operators

Logical operators combine multiple conditions.

| Operator | Description |
|----------|-------------|
| and | True if both conditions are True |
| or | True if at least one condition is True |
| not | Reverses the Boolean value |

Example

```python
age = 24
salary = 50000

age > 18 and salary > 30000
```

Output

```text
True
```

---

## 4.5 Identity Operators

Identity operators check whether two variables refer to the same object in memory.

| Operator | Description |
|----------|-------------|
| is | Same object |
| is not | Different object |

Example

```python
a = [1, 2]
b = a

print(a is b)
```

Output

```text
True
```

---

## 4.6 Membership Operators

Membership operators check whether an element exists inside a collection.

| Operator | Meaning |
|----------|---------|
| in | Exists |
| not in | Does not exist |

Example

```python
"Py" in "Python"

10 in [1, 5, 10]
```

Output

```text
True

True
```

---

## 4.7 Bitwise Operators

Bitwise operators work directly on binary representations of integers.

| Operator | Description |
|----------|-------------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

Example

```python
5 & 3

5 | 3

5 ^ 3
```

---

# 5. Operator Precedence

Python evaluates operators based on precedence.

Example

```python
2 + 3 * 4
```

Output

```text
14
```

Because multiplication has higher precedence.

Use parentheses to improve readability.

```python
(2 + 3) * 4
```

Output

```text
20
```

Common precedence (highest to lowest):

1. `()`
2. `**`
3. `* / // %`
4. `+ -`
5. Comparison Operators
6. `not`
7. `and`
8. `or`