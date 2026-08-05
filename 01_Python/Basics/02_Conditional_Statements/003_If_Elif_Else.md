# ===================================================
# Topic: If-Elif-Else Statement
# Category: Python Basics
# Difficulty: ⭐⭐☆☆☆
# Interview Importance: ⭐⭐⭐⭐⭐
# ===================================================

# 1. Introduction

## What is an If-Elif-Else Statement?

The `if-elif-else` statement is a decision-making construct used when there are **multiple possible conditions**.

Python evaluates the conditions **from top to bottom** and executes the **first matching block**. Once a condition is satisfied, the remaining conditions are skipped.

---

## Why is it Important?

Use `if-elif-else` whenever your program has more than two possible outcomes.

Examples:

- Student grading
- Tax calculation
- Salary brackets
- Product discounts
- Weather classification
- Menu-driven programs

---

# 2. Characteristics

- Supports multiple conditions.
- Conditions are evaluated sequentially.
- Only one block executes.
- `else` is optional.
- Improves readability compared to multiple independent `if` statements.

---

# 3. Syntax

```python
if condition1:
    statements

elif condition2:
    statements

elif condition3:
    statements

else:
    statements
```

Example

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 35:
    print("Grade C")

else:
    print("Fail")
```

---

# 4. Flow Diagram

```text
                 Condition 1
                     │
          ┌──────────┴──────────┐
          │                     │
        True                 False
          │                     │
     Execute Block         Condition 2
                                  │
                      ┌───────────┴───────────┐
                      │                       │
                    True                  False
                      │                       │
                 Execute Block         Condition 3
                                            │
                                            │
                                       ...
                                            │
                                         Else
```

---

# 5. Internal Working

Python checks each condition one by one.

```
Condition 1

↓

True?

↓

Yes

↓

Execute

↓

Skip remaining conditions
```

If Condition 1 is False, Python checks Condition 2, and so on.

---

# 6. Examples

## Example 1 – Student Grade

```python
marks = 78

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 35:
    print("Grade C")

else:
    print("Fail")
```

---

## Example 2 – Age Category

```python
age = 25

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")
```

---

## Example 3 – Temperature

```python
temperature = 36

if temperature > 40:
    print("Very Hot")

elif temperature > 30:
    print("Hot")

elif temperature > 20:
    print("Pleasant")

else:
    print("Cold")
```

---

## Example 4 – Login Status

```python
if user is None:
    print("User not found")

elif not password:
    print("Password missing")

else:
    print("Login successful")
```

---

# 7. Performance Notes

Python stops checking conditions as soon as one condition becomes `True`.

Worst Case:

```
All conditions are checked.
```

Time Complexity

| Scenario | Complexity |
|----------|------------|
| First condition matches | O(1) |
| Last condition matches | O(n) |

*n = number of conditions*

---

# 8. Interview Insights 💡

### Does Python evaluate every condition?

No.

Once a condition becomes `True`, Python skips all remaining `elif` and `else` blocks.

---

### Can multiple blocks execute?

No.

Exactly one block executes.

---

### Is `else` mandatory?

No.

It is optional.

---

### Can an `elif` exist without an `if`?

No.

Every `elif` belongs to a preceding `if`.

---

# 9. Common Mistakes ❌

## Wrong Order

```python
marks = 95

if marks >= 35:
    print("Pass")

elif marks >= 90:
    print("Grade A")
```

Output

```
Pass
```

The second condition is never reached.

---

Correct

```python
if marks >= 90:

elif marks >= 75:

elif marks >= 35:
```

Always write **more specific conditions first**.

---

## Multiple Independent If Statements

Wrong

```python
if marks >= 90:
    print("A")

if marks >= 75:
    print("B")
```

Both may execute.

Use `if-elif-else` when only one outcome should occur.

---

# 10. Best Practices ✅

- Arrange conditions from most specific to least specific.
- Avoid duplicate conditions.
- Keep conditions simple.
- Use descriptive variable names.
- Prefer `if-elif-else` over multiple `if` statements when only one result is expected.

---

# 11. When Should You Use This? 🎯

| Situation | Recommendation |
|-----------|---------------|
| Student grading | ✅ |
| Salary slabs | ✅ |
| Tax calculation | ✅ |
| Product discounts | ✅ |
| Menu selection | ✅ |
| Weather classification | ✅ |

---

# 12. When Should You NOT Use This? 🚫

| Situation | Better Choice |
|-----------|---------------|
| Only one condition | `if` |
| Two outcomes | `if-else` |
| Simple assignment | Ternary Operator |
| Pattern matching | `match-case` |

---

# 13. Common Interview Scenario 💼

Determine loan eligibility.

```python
if credit_score >= 750:
    print("Low Risk")

elif credit_score >= 650:
    print("Medium Risk")

else:
    print("High Risk")
```

---

# 14. Data Engineer Perspective 🌍

During ETL processing:

```python
if record["status"] == "NEW":
    process_new()

elif record["status"] == "UPDATED":
    process_update()

elif record["status"] == "DELETED":
    process_delete()

else:
    log_invalid_record()
```

This pattern is common when processing events, transaction types, or data quality rules.

---

# 15. Comparison Table

| Statement | Best For |
|-----------|----------|
| if | One condition |
| if-else | Two outcomes |
| if-elif-else | Multiple outcomes |
| match-case | Pattern matching |
| Ternary | One-line assignment |

---

# 16. Cheat Sheet 📌

| Task | Syntax |
|------|--------|
| Multiple Conditions | `if-elif-else` |
| Optional Default | `else` |
| First Match Wins | ✅ |
| One Block Executes | ✅ |

---

# 17. Related Topics 🔗

```
If
    ↓
If-Else
    ↓
If-Elif-Else
    ↓
Nested If
    ↓
Ternary
```

---

# 18. Practice Questions 📝

## Easy

1. What is the purpose of `elif`?
2. Can multiple `elif` blocks execute?
3. Is `else` mandatory?

---

## Medium

1. Explain the execution flow of `if-elif-else`.
2. Why should conditions be ordered carefully?
3. Compare `if-elif-else` with multiple `if` statements.

---

## Hard

1. Explain the worst-case time complexity.
2. Describe a real-world ETL scenario using `if-elif-else`.
3. Why does Python stop checking conditions after the first match?

---

# 19. Revision Summary 🚀

- Use `if-elif-else` for multiple possible outcomes.
- Conditions are checked from top to bottom.
- Only the first matching block executes.
- Order conditions from most specific to least specific.
- `else` is optional.
- Widely used for business rules, classification, and ETL workflows.