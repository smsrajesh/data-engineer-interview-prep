# ===================================================
# Topic: Integers
# Category: Python Basics
# ===================================================

# 1. Introduction

## What is an Integer?

An integer is a whole number without a decimal point. It can be positive, negative, or zero.

### Examples

```text
-100
-5
0
7
42
999999
```

### Not Integers

```text
3.14
5.5
-2.7
```

---

# 2. Characteristics

- Whole numbers (no decimal point)
- Immutable
- Supports arithmetic operations
- Supports comparison operations
- Can be positive, negative, or zero
- Python integers have arbitrary precision (no fixed size)

---

# 3. Syntax

## Creating Integers

```python
a = 10
b = -25
c = 0
```

Check type

```python
type(a)
```

Output

```python
<class 'int'>
```

---

# 4. Types

## Positive Integer

Greater than zero.

Examples

```text
1
2
100
999
```

---

## Negative Integer

Less than zero.

Examples

```text
-1
-50
-999
```

---

## Zero

```text
0
```

Zero is neither positive nor negative.

---

## Even Numbers

A number divisible by 2.

```python
num % 2 == 0
```

Examples

```text
2
4
6
8
10
```

---

## Odd Numbers

A number not divisible by 2.

```python
num % 2 != 0
```

Examples

```text
1
3
5
7
9
```

---

## Prime Numbers

A number greater than 1 having exactly two factors.

- 1
- Itself

Examples

```text
2
3
5
7
11
13
17
19
```

Not Prime

```text
4
6
8
9
10
12
```

---

## Composite Numbers

A number greater than 1 having more than two factors.

Examples

```text
4
6
8
9
10
12
15
```

---

# 5. Internal Working

## Python Integer Object

Python stores integers as immutable objects.

```python
a = 10
b = a

b = 20
```

Output

```text
a = 10
b = 20
```

Changing `b` does not modify `a`.

---

## Integer Precision

Unlike Java or C++, Python integers have arbitrary precision.

```python
num = 999999999999999999999999999999999999
```

Python stores it correctly.

---

## Integer Caching

Python caches small integers (typically from **-5 to 256**) for performance.

Example

```python
a = 100
b = 100

a is b
```

Output

```python
True
```

---

# 6. Examples

## Factors

Example

```text
Number = 12

Factors

1
2
3
4
6
12
```

---

## Multiples

```text
Number = 5

Multiples

5
10
15
20
25
30
```

---

## Divisibility Rules

| Number | Rule |
|---------|------|
| 2 | Last digit is even |
| 3 | Sum of digits divisible by 3 |
| 4 | Last two digits divisible by 4 |
| 5 | Ends with 0 or 5 |
| 6 | Divisible by both 2 and 3 |
| 8 | Last three digits divisible by 8 |
| 9 | Sum of digits divisible by 9 |
| 10 | Ends with 0 |

---

## Absolute Value

```python
abs(-15)
```

Output

```text
15
```

---

## Integer Division

```python
7 // 2
```

Output

```text
3
```

---

## Modulus

```python
7 % 2
```

Output

```text
1
```

---

## Quotient and Remainder

```text
17 ÷ 5

Quotient = 3
Remainder = 2
```

```python
17 // 5
17 % 5
```

---

## Reverse an Integer

```text
12345

↓

54321
```

---

## Palindrome Integer

Examples

```text
121
1331
1221
```

Not Palindrome

```text
123
154
```

---

## Count Digits

```text
98765

Digits = 5
```

---

## Sum of Digits

```text
5432

5 + 4 + 3 + 2

=14
```

---

## Product of Digits

```text
234

2 × 3 × 4

=24
```

---

## Largest Digit

```text
539271

Largest = 9
```

---

## Smallest Digit

```text
539271

Smallest = 1
```

---

## Armstrong Number

```text
153

1³ + 5³ + 3³

=153
```

---

## Perfect Number

```text
6

Factors

1
2
3

1+2+3 = 6
```

---

## GCD

```text
12

18

GCD = 6
```

---

## LCM

```text
6

8

LCM = 24
```

---

## Power

```python
2 ** 3

pow(2,3)
```

Output

```text
8
```

---

## Square Root

```python
import math

math.sqrt(25)
```

Output

```text
5
```

---

# 7. Common Methods / Operations

| Operation | Example |
|-----------|---------|
| Addition | `a + b` |
| Subtraction | `a - b` |
| Multiplication | `a * b` |
| Division | `a / b` |
| Integer Division | `a // b` |
| Modulus | `a % b` |
| Power | `a ** b` |
| Absolute | `abs(a)` |
| Maximum | `max(a,b)` |
| Minimum | `min(a,b)` |
| Round | `round(x)` |

---

# 8. Time Complexity

| Operation | Complexity |
|-----------|------------|
| Addition | O(1) |
| Subtraction | O(1) |
| Multiplication | O(1) |
| Division | O(1) |
| Modulus | O(1) |
| Comparison | O(1) |
| Reverse Integer | O(log₁₀ n) |
| Count Digits | O(log₁₀ n) |
| Sum of Digits | O(log₁₀ n) |
| Prime Check | O(√n) |
| GCD (Euclidean) | O(log(min(a,b))) |

---

# 9. Memory Considerations

- Integers are immutable.
- Python caches small integers (-5 to 256).
- Python integers automatically expand to accommodate large values.
- Larger integers consume more memory than smaller ones.

---

# 10. Common Interview Questions

- Reverse Integer
- Palindrome Number
- Count Digits
- Sum of Digits
- Product of Digits
- Prime Number
- Armstrong Number
- Perfect Number
- GCD
- LCM
- Power Function
- Happy Number
- Plus One
- Add Digits
- Integer to Roman
- Roman to Integer

---

# 11. Common Mistakes

### Using `/` instead of `//`

```python
7 / 2
```

Output

```text
3.5
```

Correct

```python
7 // 2
```

Output

```text
3
```

---

### Negative Modulus

```python
-5 % 2
```

Output

```text
1
```

Python's behavior may differ from some other programming languages.

---

### Assuming Integers Overflow

Unlike Java and C++, Python integers do not overflow under normal circumstances.

---

# 12. Best Practices

- Use descriptive variable names.
- Use `//` for integer division.
- Prefer the Euclidean algorithm for GCD.
- Use `% 10` and `// 10` for digit manipulation.
- Avoid unnecessary type conversions.
- Consider edge cases such as `0`, negative values, and very large integers.

---

# 13. Cheat Sheet

| Task | Code |
|------|------|
| Last Digit | `n % 10` |
| Remove Last Digit | `n // 10` |
| Even | `n % 2 == 0` |
| Odd | `n % 2 != 0` |
| Absolute Value | `abs(n)` |
| Power | `n ** p` |
| Integer Division | `a // b` |
| Remainder | `a % b` |
| Maximum | `max(a, b)` |
| Minimum | `min(a, b)` |
| Square Root | `math.sqrt(n)` |

---

# Revision Summary

- Integers are immutable.
- Python integers have arbitrary precision.
- Use `%` for remainders and `//` for integer division.
- Learn digit manipulation (`% 10` and `// 10`).
- Understand prime numbers, GCD, LCM, and common integer-based interview problems.