# ===================================================
# Topic: If-Else Statement
# Category: Python Basics
# Difficulty: ⭐☆☆☆☆
# Interview Importance: ⭐⭐⭐⭐⭐
# ===================================================

# 1. Introduction

## What is an If-Else Statement?

An `if-else` statement is a decision-making construct that executes one block of code when a condition is `True` and another block when the condition is `False`.

Unlike a simple `if` statement, an `if-else` statement guarantees that exactly one of the two blocks will execute.

### Why is it Important?

The `if-else` statement allows programs to make decisions when there are exactly two possible outcomes.

It is commonly used for:

- Authentication
- Eligibility checks
- Input validation
- Business rules
- Data quality checks
- Error handling

---

# 2. Characteristics

- Executes only one block.
- Condition must evaluate to a Boolean value.
- Uses indentation to define code blocks.
- Exactly one branch executes.
- Can be nested inside other control structures.

---

# 3. Syntax

```python
if condition:
    # Executes if condition is True
else:
    # Executes if condition is False
```

Example

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# 4. Flow of Execution

```text
           Condition
               │
       ┌───────┴────────┐
       │                │
     True             False
       │                │
 Execute If      Execute Else
       │                │
       └────────┬───────┘
                │
          Next Statement
```

---

# 5. Internal Working

Python follows these steps:

1. Evaluate the condition.
2. Convert the result to `True` or `False`.
3. If `True`, execute the `if` block.
4. Otherwise, execute the `else` block.
5. Continue with the next statement.

Example

```python
marks = 75

if marks >= 35:
    print("Pass")
else:
    print("Fail")
```

Evaluation

```text
75 >= 35

↓

True

↓

Execute "Pass"
```

---

# 6. Examples

## Example 1 - Even or Odd

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Example 2 - Login Status

```python
is_logged_in = True

if is_logged_in:
    print("Welcome")
else:
    print("Please Login")
```

---

## Example 3 - Empty List

```python
items = []

if items:
    print("List contains data")
else:
    print("List is empty")
```

---

## Example 4 - Temperature Check

```python
temperature = 18

if temperature > 25:
    print("Hot")
else:
    print("Pleasant")
```

---

# 7. Performance Notes

| Operation | Complexity |
|-----------|------------|
| Condition Evaluation | O(1)* |

\* Complexity depends on the condition itself.

Examples

```python
x > 5
```

O(1)

```python
target in large_list
```

O(n)

---

# 8. Interview Insights 💡

### Does Python execute both blocks?

No.

Only one block executes.

---

### Is the else block mandatory?

No.

A simple `if` statement can exist without `else`.

---

### Can the else block contain another if statement?

Yes.

This creates a nested conditional.

---

### Does Python evaluate the condition twice?

No.

The condition is evaluated only once.

---

# 9. Common Mistakes ❌

## Missing Colon

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
else:
print("Minor")
```

Correct

```python
if age > 18:
    print("Adult")
else:
    print("Minor")
```

---

## Using Assignment Instead of Comparison

Wrong

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

# 10. Best Practices ✅

- Keep conditions simple.
- Avoid unnecessary nesting.
- Use meaningful Boolean variables.
- Keep both branches readable.
- Avoid duplicate code inside both blocks.

---

# 11. Common Interview Scenario 💼

A data pipeline should load only valid records.

```python
if customer_id is not None:
    print("Load Record")
else:
    print("Skip Record")
```

Another example:

```python
if amount > 0:
    print("Valid Transaction")
else:
    print("Invalid Transaction")
```

---

# 12. Data Engineer Perspective 🌍

`if-else` statements are widely used for:

- Data validation
- Rejecting invalid records
- Handling NULL values
- Logging failed records
- Routing data to different pipelines

Example

```python
if email:
    load_record()
else:
    log_invalid_record()
```

---

# 13. Cheat Sheet 📌

| Task | Syntax |
|------|--------|
| Basic | `if condition:` |
| Alternative | `else:` |
| None Check | `if value is None:` |
| Empty Collection | `if not items:` |
| Boolean Variable | `if is_valid:` |

---

# 14. Related Topics 🔗

```text
If Statement
      ↓
If-Else Statement
      ↓
If-Elif-Else
      ↓
Nested If
```

---

# 15. Practice Questions 📝

## Easy

1. What is an `if-else` statement?
2. Can both blocks execute?
3. Is `else` mandatory?

---

## Medium

1. Explain the execution flow of an `if-else` statement.
2. How does Python evaluate the condition?
3. Why is indentation important?

---

## Hard

1. Explain the difference between `if` and `if-else`.
2. Describe a real-world scenario where `if-else` is preferable to multiple `if` statements.
3. How would you use `if-else` in a data validation pipeline?

---

# 16. Revision Summary 🚀

- `if-else` provides two possible execution paths.
- Only one branch executes.
- Conditions are evaluated once.
- Indentation defines each block.
- Widely used for validation, business rules, and decision-making.
- Keep conditions simple and readable.