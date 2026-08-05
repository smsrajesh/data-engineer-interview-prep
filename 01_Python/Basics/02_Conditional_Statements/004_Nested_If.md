# ===================================================
# Topic: Nested If Statement
# Category: Python Basics
# Difficulty: ⭐⭐☆☆☆
# Interview Importance: ⭐⭐⭐⭐☆
# ===================================================

# 1. Introduction

## What is a Nested If Statement?

A Nested If Statement is an `if` statement placed inside another `if` or `else` block.

It allows a program to make decisions in multiple stages.

Think of it as:

> "Only if the first condition is satisfied, check another condition."

---

## Why is it Important?

Nested `if` statements are useful when one decision depends on another.

Examples:

- ATM Authentication
- User Login
- Loan Approval
- Student Admission
- Access Control
- Data Validation

---

# 2. Characteristics

- One `if` inside another `if` or `else`
- Executes step by step
- Inner condition is checked only if the outer condition allows it
- Can have multiple levels of nesting
- Excessive nesting reduces readability

---

# 3. Syntax

```python
if condition1:
    if condition2:
        statements
```

Example

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can Drive")
```

---

# 4. Flow Diagram

```text
            Condition 1
                 │
         ┌───────┴────────┐
         │                │
       True            False
         │                │
    Condition 2         End
         │
    ┌────┴─────┐
    │          │
  True      False
    │          │
 Execute     End
```

---

# 5. Internal Working

Python evaluates the outer condition first.

If the outer condition is False,

→ Python skips the entire nested block.

If the outer condition is True,

→ Python evaluates the inner condition.

---

# 6. Examples

## Example 1 – ATM Withdrawal

```python
balance = 10000
amount = 3000

if balance >= amount:
    if amount > 0:
        print("Transaction Successful")
```

---

## Example 2 – Login System

```python
username = "Rajesh"
password = "python123"

if username == "Rajesh":
    if password == "python123":
        print("Login Successful")
```

---

## Example 3 – Student Admission

```python
marks = 90
sports_quota = True

if marks >= 85:
    if sports_quota:
        print("Eligible for Special Admission")
```

---

## Example 4 – File Validation

```python
filename = "employees.csv"

if filename:
    if filename.endswith(".csv"):
        print("Valid CSV File")
```

---

# 7. Performance Notes

Nested `if` statements themselves do not increase complexity.

Complexity depends on the conditions being evaluated.

| Condition | Complexity |
|------------|------------|
| Numeric Comparison | O(1) |
| String Comparison | O(n) |
| List Membership | O(n) |
| Dictionary Lookup | O(1) |

---

# 8. Interview Insights 💡

### Does Python evaluate the inner if every time?

No.

Only if the outer condition evaluates to True.

---

### Is nested if bad?

No.

But too many levels make code difficult to read and maintain.

---

### How many levels can we nest?

There is no fixed limit, but more than 3–4 levels is usually a sign that the logic should be simplified.

---

# 9. Common Mistakes ❌

## Too Much Nesting

Bad

```python
if A:
    if B:
        if C:
            if D:
                print("Done")
```

Hard to read.

---

## Forgetting Indentation

Wrong

```python
if age > 18:
if license:
    print("Drive")
```

Correct

```python
if age > 18:
    if license:
        print("Drive")
```

---

# 10. Best Practices ✅

- Keep nesting shallow.
- Extract complex logic into functions.
- Use meaningful variable names.
- Consider `if-elif-else` when conditions are alternatives rather than dependent.

---

# 11. When Should You Use This? 🎯

| Situation | Recommendation |
|------------|---------------|
| Authentication | ✅ |
| Permission checks | ✅ |
| Multi-step validation | ✅ |
| Parent-child conditions | ✅ |

---

# 12. When Should You NOT Use This? 🚫

| Situation | Better Choice |
|------------|---------------|
| Independent conditions | Multiple `if` statements |
| Multiple alternatives | `if-elif-else` |
| Too many nesting levels | Functions or guard clauses |

---

# 13. Common Interview Scenario 💼

Validate a customer record before loading.

```python
if customer_id is not None:
    if email:
        load_record()
```

If the customer ID is missing, there is no need to check the email.

---

# 14. Data Engineer Perspective 🌍

Nested `if` statements are common in ETL pipelines.

Example:

```python
if record["status"] == "ACTIVE":
    if record["email"]:
        process_record(record)
```

This avoids unnecessary processing of invalid or inactive records.

---

# 15. Cross-Technology Mapping 🌉

| Concept | Python | SQL | PySpark | Snowflake |
|----------|--------|------|----------|------------|
| Nested Conditions | Nested `if` | Nested `CASE` | Nested `when()` | Nested `CASE` |

Example:

### SQL

```sql
CASE
    WHEN status = 'ACTIVE' THEN
        CASE
            WHEN email IS NOT NULL THEN 'VALID'
            ELSE 'INVALID'
        END
END
```

### PySpark

```python
when(col("status") == "ACTIVE",
     when(col("email").isNotNull(), "VALID")
     .otherwise("INVALID"))
```

---

# 16. Comparison Table

| Statement | Best Use |
|------------|----------|
| if | One condition |
| if-else | Two outcomes |
| if-elif-else | Multiple alternatives |
| Nested if | Dependent conditions |
| match-case | Pattern matching |

---

# 17. Cheat Sheet 📌

| Task | Syntax |
|------|--------|
| Nested Condition | `if ...: if ...:` |
| Parent Condition | Outer `if` |
| Child Condition | Inner `if` |
| Skip Inner Block | Outer condition is False |

---

# 18. Related Topics 🔗

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
```

---

# 19. Practice Questions 📝

## Easy

1. What is a nested if statement?
2. When is the inner if executed?
3. Can an if be nested inside an else block?

---

## Medium

1. Explain the execution flow of nested if.
2. What are the disadvantages of excessive nesting?
3. When should you choose nested if over if-elif-else?

---

## Hard

1. Refactor deeply nested code to improve readability.
2. Design a login system using nested if.
3. Explain how nested conditions can affect code maintainability.

---

# 20. Revision Summary 🚀

- Nested `if` statements evaluate conditions in stages.
- The inner condition is checked only if the outer condition passes.
- Keep nesting shallow for readability.
- Use nested `if` for dependent conditions.
- Consider alternatives when nesting becomes excessive.