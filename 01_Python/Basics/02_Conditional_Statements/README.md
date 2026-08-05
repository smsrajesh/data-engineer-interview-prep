# ===================================================
# Chapter 2: Conditional Statements
# ===================================================

## Overview

Conditional Statements allow a program to make decisions based on one or more conditions.

They are one of the most fundamental concepts in programming and are used extensively in Python applications, Data Engineering pipelines, backend systems, APIs, automation scripts, and ETL workflows.

Understanding conditional logic is essential before learning loops, functions, and object-oriented programming.

---

# Chapter Information

| Property | Value |
|----------|-------|
| Difficulty | ⭐⭐☆☆☆ |
| Learning Priority | ⭐⭐⭐⭐⭐ |
| Interview Importance | ⭐⭐⭐⭐⭐ |
| Production Usage | ⭐⭐⭐⭐⭐ |
| Estimated Study Time | 2–3 Hours |

---

# Learning Objectives

After completing this chapter, you will be able to:

- Write simple and complex conditional statements.
- Choose the correct conditional construct for different scenarios.
- Understand how Python evaluates conditions.
- Understand Truthy and Falsy values.
- Use Short Circuit Evaluation safely.
- Apply conditional logic in real-world Data Engineering projects.
- Compare Python conditional statements with SQL, PySpark, and Snowflake.

---

# Topics Covered

| No | Topic | Status |
|----|-------|--------|
| 001 | If Statement | ✅ |
| 002 | If-Else Statement | ✅ |
| 003 | If-Elif-Else | ✅ |
| 004 | Nested If | ✅ |
| 005 | Ternary Operator | ✅ |
| 006 | Match Case | ✅ |
| 007 | Short Circuit Evaluation | ✅ |

---

# Learning Roadmap

```text
Decision Making

↓

If Statement

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

↓

Short Circuit Evaluation
```

---

# Cross Technology Mapping

| Concept | Python | SQL | PySpark | Snowflake |
|----------|--------|------|----------|------------|
| One Condition | if | CASE | when() | CASE |
| Two Outcomes | if-else | CASE | when().otherwise() | CASE |
| Multiple Conditions | if-elif-else | CASE WHEN | chained when() | CASE |
| Logical AND | and | AND | & | AND |
| Logical OR | or | OR | \| | OR |
| Logical NOT | not | NOT | ~ | NOT |

> **Note:** SQL `CASE` and PySpark `when()` solve similar decision-making problems but are not structural pattern matching like Python's `match-case`.

---

# Data Engineering Applications

Conditional statements are used in:

- Data Validation
- Business Rules
- Data Cleansing
- Data Classification
- Record Routing
- ETL Pipelines
- Error Handling
- API Processing
- File Validation

---

# Common Interview Questions

- Difference between if and if-else.
- Difference between if-elif-else and match-case.
- Explain Truthy and Falsy values.
- Explain Short Circuit Evaluation.
- Why does Python return operands in logical expressions?

---

# Prerequisites

Before starting this chapter, you should understand:

- Variables
- Integers
- Strings
- Booleans
- Operators
- Type Casting
- None

---

# Next Chapter

```
Loops
```

---

# Revision Resources

- Chapter Summary *(Coming Next)*
- Interview Questions *(Coming Later)*
- Cheat Sheet *(Coming Later)*

---

# Chapter Completion Checklist

- [x] All concepts completed
- [x] Examples added
- [x] Data Engineer perspective included
- [x] Cross-technology mapping included
- [ ] Notes standardized to final handbook template
- [ ] Chapter summary completed