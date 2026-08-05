# ===================================================
# Topic: Match-Case Statement
# Category: Python Basics
# Difficulty: ⭐⭐⭐☆☆
# Interview Importance: ⭐⭐⭐⭐☆
# Python Version: 3.10+
# ===================================================

# 1. Introduction

## What is Match-Case?

`match-case` is Python's **pattern matching** statement, introduced in **Python 3.10**.

It compares a value against multiple patterns and executes the first matching case.

It is Python's equivalent of **switch-case** in languages like Java, C++, and JavaScript, but it is much more powerful because it supports structural pattern matching.

---

## Why was Match-Case Introduced?

Before Python 3.10, developers often wrote long `if-elif-else` chains.

Example

```python
if status == "NEW":
    ...
elif status == "PROCESSING":
    ...
elif status == "FAILED":
    ...
else:
    ...
```

This becomes harder to read as the number of conditions grows.

`match-case` provides a cleaner alternative for matching values and patterns.

---

# 2. Characteristics

- Introduced in Python 3.10
- Executes only the first matching case
- No `break` statement required
- Supports literals, sequences, mappings, classes, and wildcards
- More expressive than traditional switch-case statements

---

# 3. Syntax

```python
match expression:
    case pattern1:
        statements

    case pattern2:
        statements

    case _:
        default statements
```

Example

```python
status = "NEW"

match status:
    case "NEW":
        print("Create Record")

    case "UPDATED":
        print("Update Record")

    case "DELETED":
        print("Delete Record")

    case _:
        print("Unknown Status")
```

---

# 4. Flow Diagram

```text
              Match Expression
                     │
        ┌────────────┴────────────┐
        │                         │
     Pattern 1                Not Match
        │                         │
     Execute                 Pattern 2
                                  │
                           ...
                                  │
                            Default (_)
```

---

# 5. Internal Working

Python evaluates the `match` expression once.

Then it compares the value with each `case` from top to bottom.

- First matching case executes.
- Remaining cases are skipped.
- If nothing matches, the wildcard (`_`) executes (if provided).

Unlike C/Java, there is **no fall-through**.

---

# 6. Examples

## Beginner

```python
day = 2

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case _:
        print("Invalid Day")
```

---

## Intermediate

```python
status = "FAILED"

match status:
    case "NEW":
        print("Insert")

    case "FAILED":
        print("Retry")

    case _:
        print("Ignore")
```

---

## Interview Level

```python
event = "DELETE"

match event:
    case "INSERT":
        process_insert()

    case "UPDATE":
        process_update()

    case "DELETE":
        process_delete()

    case _:
        log_unknown_event()
```

---

# 7. Performance Notes

Performance is generally comparable to an `if-elif-else` chain for simple value matching.

The choice between the two should primarily be based on **readability and maintainability**, not speed.

---

# 8. Interview Insights 💡

### Is Match-Case a replacement for If-Elif-Else?

No.

Use it when you're matching **patterns or discrete values**.

If your logic depends on relational conditions like:

```python
marks > 90
salary >= 50000
age < 18
```

`if-elif-else` is usually the better choice.

---

### Does Match-Case need break?

No.

Python automatically stops after the first matching case.

---

### What is `_`?

It is the wildcard (default case).

Equivalent to:

```python
else:
```

in an `if-elif-else` chain.

---

# 9. Common Mistakes ❌

## Forgetting the Default Case

Although optional, using `_` is recommended when unexpected values are possible.

---

## Using Match-Case for Range Checks

Avoid

```python
match marks:
    case ???:
```

Instead use

```python
if marks >= 90:
```

---

# 10. Best Practices ✅

- Use `match-case` for known discrete values.
- Include a wildcard (`_`) when appropriate.
- Keep each case focused.
- Prefer `if-elif-else` for complex Boolean expressions.

---

# 11. When Should You Use This? 🎯

| Situation | Recommendation |
|------------|---------------|
| Status values | ✅ |
| Menu selection | ✅ |
| Event type | ✅ |
| API response type | ✅ |
| Command parsing | ✅ |

---

# 12. When Should You NOT Use This? 🚫

| Situation | Better Choice |
|------------|---------------|
| Range comparison | `if-elif-else` |
| Complex Boolean logic | `if-elif-else` |
| Mathematical conditions | `if-elif-else` |

---

# 13. Common Interview Scenario 💼

Processing ETL events.

```python
match event_type:
    case "INSERT":
        load_new()

    case "UPDATE":
        update_existing()

    case "DELETE":
        remove_record()

    case _:
        log_unknown()
```

---

# 14. Data Engineer Perspective 🌍

Imagine an event-driven ingestion pipeline.

Each incoming record has an operation.

```text
INSERT
UPDATE
DELETE
UPSERT
```

Instead of multiple `if-elif` statements, `match-case` makes the routing logic cleaner and easier to extend.

---

# 15. Cross-Technology Mapping 🌉

| Concept | Python | SQL | PySpark | Snowflake |
|----------|--------|------|----------|------------|
| Pattern Matching | match-case | CASE | when().otherwise() | CASE |

> **Note:** SQL `CASE` and PySpark `when()` are conditional expressions, not true structural pattern matching. They solve similar decision-making problems but are not direct feature equivalents.

---

# 16. Comparison Table

| Statement | Best Use |
|------------|----------|
| if | One condition |
| if-else | Two outcomes |
| if-elif-else | Multiple conditions |
| match-case | Multiple known values/patterns |
| Ternary | Simple assignment |

---

# 17. Mental Model 🧠

```text
Need to compare ranges?

↓

Use if-elif-else

--------------------------

Need to compare fixed values?

↓

Use match-case

--------------------------

Need one-line assignment?

↓

Use Ternary
```

---

# 18. Code Review Tip 🧪

❌ Less Readable

```python
if command == "start":
    ...
elif command == "stop":
    ...
elif command == "restart":
    ...
elif command == "status":
    ...
```

✅ Better

```python
match command:
    case "start":
        ...
    case "stop":
        ...
    case "restart":
        ...
    case "status":
        ...
```

---

# 19. Cheat Sheet 📌

| Task | Syntax |
|------|--------|
| Match value | `match value:` |
| Compare | `case pattern:` |
| Default | `case _:` |

---

# 20. Related Topics 🔗

```text
If
   ↓
If-Else
   ↓
If-Elif-Else
   ↓
Nested If
   ↓
Ternary
   ↓
Match-Case
   ↓
Short Circuit Evaluation
```

---

# 21. Practice Questions 📝

## Easy

1. What is `match-case`?
2. Which Python version introduced it?
3. What is the purpose of `_`?

---

## Medium

1. Compare `match-case` with `if-elif-else`.
2. When should you prefer `match-case`?
3. Why is `break` not required?

---

## Hard

1. Design a menu-driven application using `match-case`.
2. Explain structural pattern matching.
3. Compare Python `match-case` with Java's `switch`.

---

# 22. Related LeetCode Problems 🔗

While `match-case` itself is rarely required on LeetCode, similar decision-making logic appears in:

- 146. LRU Cache (command handling)
- 150. Evaluate Reverse Polish Notation
- 155. Min Stack
- 622. Design Circular Queue

---

# 23. 5-Minute Revision ⚡

✔ Fixed values?

→ Match-Case

✔ Range comparisons?

→ If-Elif-Else

✔ One-line assignment?

→ Ternary

✔ Multiple dependent conditions?

→ Nested If

✔ Default branch?

→ case _