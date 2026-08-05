# ===================================================
# Topic: If Statement
# Category: Python Basics
# Difficulty: ⭐☆☆☆☆
# Interview Importance: ⭐⭐⭐⭐⭐
# ===================================================

# 1. Introduction

## What is an If Statement?

An `if` statement is a conditional statement that executes a block of code **only if a specified condition evaluates to `True`**.

It is the foundation of decision-making in Python.

### Why is it Important?

The `if` statement allows programs to make decisions based on data.

It is used in:

- User authentication
- Input validation
- Data filtering
- Business rules
- Error handling
- ETL pipelines
- Machine Learning

---

# 2. Characteristics

- Executes code only when the condition is `True`.
- Uses Boolean expressions.
- Indentation defines the code block.
- Can contain one or more statements.
- Can be nested inside other control structures.

---

# 3. Syntax

General Syntax

```python
if condition:
    statement
```

Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

# 4. Flow of Execution

```
        Condition
            │
      ┌─────┴─────┐
      │           │
    True       False
      │           │
 Execute       Skip
      │           │
      └─────► Next Statement
```

---

# 5. Internal Working

1. Python evaluates the condition.
2. The condition is converted to a Boolean value.
3. If it is `True`, the indented block executes.
4. If it is `False`, Python skips the block.

Example

```python
x = 10

if x > 5:
    print("Greater")
```

Evaluation

```
10 > 5

↓

True

↓

Print executes
```

---

# 6. Truthy and Falsy Conditions

Python automatically converts values into Boolean values.

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

Everything else is generally Truthy.

Example

```python
if []:
    print("Executed")
```

Nothing prints because an empty list is Falsy.

---

# 7. Examples

## Example 1

```python
temperature = 35

if temperature > 30:
    print("Hot")
```

---

## Example 2

```python
marks = 90

if marks >= 35:
    print("Pass")
```

---

## Example 3

```python
username = "Rajesh"

if username:
    print("Valid User")
```

---

## Example 4

```python
numbers = [10,20]

if numbers:
    print("List is not empty")
```

---

# 8. Performance Notes

| Operation | Complexity |
|-----------|------------|
| Condition Evaluation | O(1) |
| Boolean Conversion | O(1) |

The complexity of the condition depends on the expression itself.

Example

```python
if x > 5
```

O(1)

Example

```python
if target in large_list
```

O(n)

---

# 9. Interview Insights 💡

## Can any object be used inside an if statement?

Yes.

Python checks its Truthiness.

Example

```python
if "Python":
```

This executes.

---

## Why doesn't this execute?

```python
if 0:
```

Because `0` is Falsy.

---

## Is this valid?

```python
if True:
```

Yes.

Although not common, it is valid Python.

---

# 10. Common Mistakes ❌

## Forgetting the Colon

Wrong

```python
if age > 18
```

Correct

```python
if age > 18:
```

---

## Incorrect Indentation

Wrong

```python
if age > 18:
print("Adult")
```

Correct

```python
if age > 18:
    print("Adult")
```

---

## Assignment Instead of Comparison

Wrong

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

# 11. Best Practices ✅

- Keep conditions simple.
- Use meaningful variable names.
- Avoid deeply nested conditions.
- Prefer readability over clever code.
- Use Boolean variables when appropriate.

Example

Good

```python
if is_logged_in:
```

Avoid

```python
if is_logged_in == True:
```

---

# 12. Data Engineer Perspective 🌍

Conditional statements are used extensively in data engineering.

Examples:

- Validate records before loading.
- Skip invalid rows.
- Check for missing values.
- Apply business rules.
- Filter data during transformations.

Example

```python
if customer_id is None:
    continue
```

---

# 13. Cheat Sheet 📌

| Task | Syntax |
|------|--------|
| Basic If | `if condition:` |
| Boolean Check | `if flag:` |
| Empty List | `if not items:` |
| None Check | `if value is None:` |

---

# 14. Related Topics 🔗

```
Variables
      ↓
If Statement
      ↓
If-Else
      ↓
If-Elif-Else
```

---

# 15. Practice Questions 📝

## Easy

1. What is an if statement?
2. What happens if the condition is False?
3. What are Truthy and Falsy values?

---

## Medium

1. Explain how Python evaluates conditions.
2. Why is indentation important?
3. Can a string be used as an if condition?

---

## Hard

1. Explain Truthiness in Python.
2. Describe how Python evaluates complex conditions.
3. Compare Python's if statement with C/Java.

---

# 16. Revision Summary 🚀

- The `if` statement executes code only when a condition is `True`.
- Python evaluates conditions using Boolean values.
- Indentation defines the code block.
- Any object can be used in an `if` statement based on its Truthiness.
- Empty collections, `0`, `False`, and `None` are Falsy.
- `if` statements are fundamental for decision-making in Python.