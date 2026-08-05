# ===================================================
# Topic: Booleans
# Category: Python Basics
# Difficulty: ⭐☆☆☆☆
# Interview Importance: ⭐⭐⭐⭐⭐
# ===================================================

# 1. Introduction

## What is a Boolean?

A Boolean is a data type that represents one of two possible values:

- `True`
- `False`

Booleans are mainly used for decision-making and controlling the flow of a program.

### Why are Booleans Important?

Booleans are used in:

- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`)
- Comparisons
- Logical operations
- Filtering data
- Function return values

### Real-World Example

```python
is_logged_in = True

if is_logged_in:
    print("Welcome!")
```

---

# 2. Characteristics

- Has only two values: `True` and `False`
- Derived from comparison operations
- Result of logical expressions
- Subclass of `int` in Python
- Commonly used in decision-making

---

# 3. Syntax

Creating Boolean values

```python
is_active = True

is_admin = False
```

Check the type

```python
type(True)
```

Output

```python
<class 'bool'>
```

---

# 4. Boolean Values

## True

Represents a positive or successful condition.

```python
True
```

---

## False

Represents a negative or unsuccessful condition.

```python
False
```

---

## Boolean from Comparison

```python
10 > 5

5 == 10

100 != 50
```

Output

```text
True

False

True
```

---

## Boolean from Logical Expressions

```python
True and False

True or False

not True
```

Output

```text
False

True

False
```

---

# 5. Internal Working

Python internally represents:

```python
True
```

as

```text
1
```

and

```python
False
```

as

```text
0
```

Example

```python
True + True
```

Output

```text
2
```

Example

```python
False + 10
```

Output

```text
10
```

Although Booleans behave like integers, they should be used only for logical decisions.

---

# 6. Examples

## Using Comparison

```python
age = 20

print(age >= 18)
```

Output

```text
True
```

---

## Using Logical Operators

```python
age = 25
salary = 50000

print(age > 18 and salary > 30000)
```

Output

```text
True
```

---

## Using Boolean Variables

```python
is_student = False

if is_student:
    print("Student Discount")
else:
    print("Regular Price")
```

---

## Truthy and Falsy Values

Falsy values

```python
False
0
0.0
''
[]
{}
set()
None
```

Everything else is generally considered Truthy.

Example

```python
if []:
    print("Hello")
else:
    print("Empty")
```

Output

```text
Empty
```

---

# 7. Built-in Methods / Operations

| Operation | Example |
|-----------|---------|
| bool() | bool(1) |
| and | True and False |
| or | True or False |
| not | not True |

Examples

```python
bool(100)

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

# 8. Performance Notes

Boolean operations execute in constant time.

| Operation | Complexity |
|-----------|------------|
| Comparison | O(1) |
| and | O(1) |
| or | O(1) |
| not | O(1) |
| bool() | O(1) |

Python also uses **short-circuit evaluation**:

```python
False and expensive_function()
```

The second expression is **never evaluated**.

---

# 9. Interview Insights 💡

### Is `bool` a separate type?

Yes.

```python
type(True)
```

returns

```text
bool
```

However,

```python
issubclass(bool, int)
```

returns

```text
True
```

---

### Difference between `==` and `is`

```python
True == 1
```

returns

```text
True
```

But

```python
True is 1
```

returns

```text
False
```

---

### Short-Circuit Evaluation

Interviewers often ask:

Why does this never raise an error?

```python
False and (10 / 0)
```

Because the second expression is never executed.

---

# 10. Common Mistakes ❌

### Comparing with `True`

Avoid

```python
if is_valid == True:
```

Prefer

```python
if is_valid:
```

---

### Comparing with `False`

Avoid

```python
if is_valid == False:
```

Prefer

```python
if not is_valid:
```

---

### Confusing `=` with `==`

Wrong

```python
if x = 5:
```

Correct

```python
if x == 5:
```

---

# 11. Best Practices ✅

- Use meaningful Boolean variable names.
- Prefer `if flag:` instead of `if flag == True:`.
- Use `not` for negation instead of comparing with `False`.
- Keep Boolean expressions simple and readable.
- Take advantage of short-circuit evaluation when appropriate.

---

# 12. Cheat Sheet 📌

| Task | Code |
|------|------|
| Boolean Value | `True`, `False` |
| Convert to Boolean | `bool(x)` |
| Logical AND | `and` |
| Logical OR | `or` |
| Logical NOT | `not` |
| Equality | `==` |
| Identity | `is` |

---

# 13. Related Topics 🔗

Previous

```
Integers
    ↓
Strings
    ↓
Operators
    ↓
Booleans
```

Next

```
Booleans
      ↓
Conditional Statements
      ↓
Loops
      ↓
Functions
```

---

# 14. Practice Questions 📝

## Easy

1. What are the two Boolean values in Python?
2. What does `bool(0)` return?
3. What does `bool("Python")` return?

---

## Medium

1. Explain Truthy and Falsy values.
2. What is short-circuit evaluation?
3. Why is `bool` a subclass of `int`?

---

## Hard

1. Explain the difference between:

```python
True == 1
```

and

```python
True is 1
```

2. Why is

```python
False and (10/0)
```

safe to execute?

---

# 15. Revision Summary 🚀

- Booleans have only two values: `True` and `False`.
- Used in conditions, loops, and logical operations.
- `bool` is a subclass of `int`.
- Learn Truthy and Falsy values.
- Understand short-circuit evaluation.
- Prefer `if flag:` over `if flag == True`.
- Master logical operators before learning conditional statements.