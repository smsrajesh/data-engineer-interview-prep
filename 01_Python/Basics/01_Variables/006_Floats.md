# ===================================================
# Topic: Floats
# Category: Python Basics
# Difficulty: ⭐⭐☆☆☆
# Interview Importance: ⭐⭐⭐⭐☆
# ===================================================

# 1. Introduction

## What is a Float?

A float (floating-point number) is a numeric data type used to represent numbers that contain a decimal point.

Unlike integers, floats can store fractional values.

Examples

```python
price = 99.99
temperature = 36.5
pi = 3.14159
```

### Why are Floats Important?

Floats are used whenever precision beyond whole numbers is required.

Common use cases:

- Currency calculations
- Scientific computations
- Sensor readings
- Machine Learning
- Statistical analysis
- Data Engineering

---

# 2. Characteristics

- Stores decimal numbers
- Immutable
- Supports arithmetic operations
- Can represent very large and very small numbers
- Based on the IEEE 754 floating-point standard

---

# 3. Syntax

Creating floats

```python
price = 199.99

height = 5.8

temperature = -10.5
```

Check the type

```python
type(price)
```

Output

```python
<class 'float'>
```

---

# 4. Types

## Positive Float

```python
25.5
```

---

## Negative Float

```python
-7.25
```

---

## Scientific Notation

Python supports exponential notation.

```python
1.5e3
```

Output

```python
1500.0
```

```python
2.5e-3
```

Output

```python
0.0025
```

---

# 5. Internal Working

Python stores floats using the IEEE 754 double-precision format (64 bits).

Approximate layout:

```text
---------------------------------------------------------
| Sign (1 bit) | Exponent (11 bits) | Fraction (52 bits) |
---------------------------------------------------------
```

Because floats use binary representation, some decimal values cannot be represented exactly.

Example

```python
0.1 + 0.2
```

Output

```python
0.30000000000000004
```

This is **expected behavior**, not a Python bug.

---

# 6. Examples

## Basic Arithmetic

```python
a = 10.5
b = 2.0

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## Rounding

```python
round(10.5678, 2)
```

Output

```python
10.57
```

---

## Absolute Value

```python
abs(-9.8)
```

Output

```python
9.8
```

---

## Convert Integer to Float

```python
float(100)
```

Output

```python
100.0
```

---

## Convert String to Float

```python
float("99.95")
```

Output

```python
99.95
```

---

# 7. Built-in Methods / Operations

| Function | Description |
|----------|-------------|
| float() | Convert to float |
| round() | Round decimal values |
| abs() | Absolute value |
| pow() | Raise to power |

Examples

```python
round(3.14159, 2)

abs(-10.5)

pow(2.5, 2)
```

---

# 8. Performance Notes

Arithmetic operations on floats execute in constant time.

| Operation | Complexity |
|-----------|------------|
| Addition | O(1) |
| Subtraction | O(1) |
| Multiplication | O(1) |
| Division | O(1) |
| Comparison | O(1) |
| round() | O(1) |

---

# 9. Memory Considerations

- Floats are immutable.
- Each float object occupies more memory than a small integer.
- Operations create new float objects.
- Floating-point arithmetic may introduce small precision errors.

---

# 10. Interview Insights 💡

## Why does this happen?

```python
0.1 + 0.2
```

Output

```python
0.30000000000000004
```

Because decimal fractions like `0.1` cannot always be represented exactly in binary.

---

## Comparing Floats

Avoid

```python
price == 10.1
```

Prefer

```python
abs(price - 10.1) < 1e-9
```

This accounts for tiny precision differences.

---

## int() vs round()

```python
int(5.9)
```

Output

```python
5
```

```python
round(5.9)
```

Output

```python
6
```

`int()` truncates the decimal part, while `round()` rounds to the nearest value.

---

# 11. Common Mistakes ❌

## Direct Float Comparison

Wrong

```python
0.1 + 0.2 == 0.3
```

Output

```python
False
```

Correct

```python
abs((0.1 + 0.2) - 0.3) < 1e-9
```

---

## Losing Precision

```python
int(9.99)
```

Output

```python
9
```

The decimal portion is discarded.

---

## Assuming Floats Are Exact

Remember that floating-point numbers are approximations.

---

# 12. Best Practices ✅

- Avoid direct comparison of floating-point values.
- Use `round()` only for presentation, not for fixing precision issues.
- Use meaningful variable names.
- Convert user input carefully.
- Be aware of floating-point limitations.

---

# 13. Data Engineer Perspective 🌍

Floats appear frequently in data engineering projects.

Examples:

- Sales amounts
- Currency values
- Temperature readings
- Sensor data
- Financial analytics
- Machine Learning features

⚠️ Precision matters.

For financial applications, many systems prefer fixed-precision decimal types rather than binary floating-point values to avoid rounding issues.

---

# 14. Cheat Sheet 📌

| Task | Code |
|------|------|
| Create Float | `price = 99.95` |
| Convert | `float("10.5")` |
| Round | `round(x, 2)` |
| Absolute Value | `abs(x)` |
| Power | `pow(x, y)` |
| Scientific Notation | `1.5e3` |

---

# 15. Related Topics 🔗

```text
Integers
    ↓
Type Casting
    ↓
Floats
    ↓
None
```

---

# 16. Practice Questions 📝

## Easy

1. What is a float?
2. How do you convert a string to a float?
3. What is scientific notation?

---

## Medium

1. Explain why `0.1 + 0.2` is not exactly `0.3`.
2. What is the difference between `int()` and `round()`?
3. Why should you avoid direct float comparisons?

---

## Hard

1. Explain the IEEE 754 standard.
2. Why are decimal fractions difficult to represent in binary?
3. How would you safely compare two floating-point numbers?

---

# 17. Revision Summary 🚀

- Floats represent decimal numbers.
- Python uses IEEE 754 double-precision representation.
- Floating-point values may not be exact.
- Avoid direct equality comparisons.
- Use `abs(a - b) < tolerance` for comparisons.
- Understand the difference between `int()` and `round()`.
- Floats are widely used in scientific and data engineering applications.