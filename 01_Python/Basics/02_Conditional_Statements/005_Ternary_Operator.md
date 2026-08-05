# ===================================================
# Topic: Ternary Operator
# Category: Python Basics
# Difficulty: ⭐⭐☆☆☆
# Interview Importance: ⭐⭐⭐⭐☆
# ===================================================

# 1. Introduction

## What is the Ternary Operator?

The Ternary Operator is a concise way to write a simple `if-else` statement in a single line.

Instead of writing multiple lines, you can choose between two values based on a condition.

---

## Why is it Important?

The ternary operator makes code shorter and more readable when there are only **two possible outcomes**.

Common use cases:

- Assigning values
- Displaying messages
- Returning values from functions
- Simple conditional expressions

---

# 2. Characteristics

- One-line conditional expression
- Returns one of two values
- Improves readability for simple conditions
- Not suitable for complex logic
- Evaluates only one branch

---

# 3. Syntax

General Syntax

```python
value_if_true if condition else value_if_false
```

Example

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output

```text
Adult
```

---

# 4. Flow Diagram

```text
               Condition
                   │
         ┌─────────┴─────────┐
         │                   │
       True               False
         │                   │
 value_if_true      value_if_false
         │                   │
         └─────────┬─────────┘
                   │
            Assigned to Variable
```

---

# 5. Internal Working

Python first evaluates the condition.

If the condition is `True`, it evaluates only the expression before `else`.

If the condition is `False`, it evaluates only the expression after `else`.

Example

```python
marks = 80

result = "Pass" if marks >= 35 else "Fail"
```

Python internally behaves like:

```python
if marks >= 35:
    result = "Pass"
else:
    result = "Fail"
```

---

# 6. Examples

## Beginner

```python
num = 8

result = "Even" if num % 2 == 0 else "Odd"

print(result)
```

---

## Intermediate

```python
temperature = 32

weather = "Hot" if temperature > 30 else "Pleasant"

print(weather)
```

---

## Interview Level

```python
customer_id = None

status = "Invalid" if customer_id is None else "Valid"

print(status)
```

---

# 7. Performance Notes

The ternary operator has the same time complexity as an equivalent `if-else` statement.

| Operation | Complexity |
|-----------|------------|
| Condition Evaluation | Depends on the condition |
| Assignment | O(1) |

---

# 8. Interview Insights 💡

### Is the ternary operator faster than `if-else`?

No.

It mainly improves readability for simple conditions.

---

### Can multiple statements be written?

No.

It should only be used for simple expressions.

---

### Does Python evaluate both expressions?

No.

Only the selected expression is evaluated.

---

# 9. Common Mistakes ❌

## Using for Complex Logic

Avoid

```python
result = (
    "A"
    if x > 90
    else "B"
    if x > 75
    else "C"
)
```

This quickly becomes difficult to read.

---

## Forgetting `else`

Wrong

```python
value = "Yes" if flag
```

A ternary expression always requires both `if` and `else`.

---

# 10. Best Practices ✅

- Use for simple assignments.
- Avoid nested ternary operators.
- Prefer readability over shorter code.
- Use regular `if-else` for complex business logic.

---

# 11. When Should You Use This? 🎯

| Situation | Recommendation |
|-----------|---------------|
| Two possible values | ✅ |
| Variable assignment | ✅ |
| Function return value | ✅ |
| Printing a simple message | ✅ |

---

# 12. When Should You NOT Use This? 🚫

| Situation | Better Choice |
|-----------|---------------|
| Multiple conditions | `if-elif-else` |
| Complex logic | Standard `if-else` |
| Multiple statements | Standard `if-else` |

---

# 13. Common Interview Scenario 💼

Assign a record status.

```python
status = "Valid" if email else "Invalid"
```

This is a common pattern in ETL validation.

---

# 14. Data Engineer Perspective 🌍

Suppose you're processing customer records.

```python
customer_status = (
    "ACTIVE"
    if customer["last_login"] is not None
    else "INACTIVE"
)
```

Simple assignments like this improve readability without adding unnecessary `if-else` blocks.

---

# 15. Cross-Technology Mapping 🌉

| Concept | Python | SQL | PySpark | Snowflake |
|----------|--------|------|----------|------------|
| Conditional Assignment | Ternary Operator | CASE WHEN | when().otherwise() | CASE |

### SQL

```sql
CASE
    WHEN salary > 50000 THEN 'High'
    ELSE 'Low'
END
```

### PySpark

```python
when(col("salary") > 50000, "High").otherwise("Low")
```

---

# 16. Comparison Table

| Statement | Best Use |
|-----------|----------|
| if | One condition |
| if-else | Two execution paths |
| Ternary | One-line assignment |
| if-elif-else | Multiple outcomes |
| match-case | Pattern matching |

---

# 17. Mental Model 🧠

```text
Need to execute multiple statements?

        │
       Yes
        │
Use if-else

        │
       No
        │
Need to assign one value?

        │
       Yes
        │
Use Ternary Operator
```

---

# 18. Cheat Sheet 📌

| Task | Syntax |
|------|--------|
| Basic | `A if condition else B` |
| Assignment | `x = A if cond else B` |
| Function Return | `return A if cond else B` |

---

# 19. Related Topics 🔗

```
If
   ↓
If-Else
   ↓
If-Elif-Else
   ↓
Nested If
   ↓
Ternary Operator
   ↓
Match Case
```

---

# 20. Practice Questions 📝

## Easy

1. What is the ternary operator?
2. What is its syntax?
3. Can it replace every `if-else` statement?

---

## Medium

1. Explain why nested ternary operators reduce readability.
2. Compare a ternary operator with a standard `if-else`.
3. When should you avoid using it?

---

## Hard

1. Refactor multiple `if-else` assignments using the ternary operator where appropriate.
2. Compare the ternary operator with SQL `CASE WHEN`.
3. Explain why only one branch is evaluated.

---

# 21. Revision Summary 🚀

- The ternary operator is a one-line `if-else` expression.
- Best used for simple assignments.
- Improves readability when used appropriately.
- Avoid nested ternary expressions.
- Has equivalent concepts in SQL (`CASE`) and PySpark (`when().otherwise()`).