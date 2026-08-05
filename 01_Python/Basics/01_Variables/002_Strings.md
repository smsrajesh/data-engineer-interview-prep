# ===================================================
# Topic: Strings
# Category: Python Basics
# ===================================================

# 1. Introduction

## What is a String?

A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

Strings are one of the most commonly used data types in Python and are widely used for storing text.

Examples

```python
name = "Rajesh"

city = 'Hyderabad'

message = """Welcome to Python"""
```

---

# 2. Characteristics

- Ordered
- Immutable
- Iterable
- Indexable
- Allows duplicate characters
- Supports slicing
- Supports concatenation
- Unicode supported

Example

```python
s = "Python"
```

| Index | Character |
|------:|-----------|
| 0 | P |
| 1 | y |
| 2 | t |
| 3 | h |
| 4 | o |
| 5 | n |

Negative Index

| Index | Character |
|------:|-----------|
| -6 | P |
| -5 | y |
| -4 | t |
| -3 | h |
| -2 | o |
| -1 | n |

---

# 3. Syntax

## Creating Strings

```python
name = "Rajesh"

city = 'Hyderabad'

paragraph = """Python is easy"""
```

Check type

```python
type(name)
```

Output

```python
<class 'str'>
```

Empty String

```python
s = ""
```

---

# 4. Types

## Single Quotes

```python
'Python'
```

---

## Double Quotes

```python
"Python"
```

---

## Triple Quotes

Used for multi-line strings.

```python
"""
Hello

World
"""
```

---

## Raw Strings

Used to ignore escape sequences.

```python
r"C:\Users\Rajesh"
```

---

## Unicode Strings

Python supports Unicode.

```python
"こんにちは"

"😊"

"नमस्ते"
```

---

# 5. Internal Working

Strings are immutable.

```python
name = "Python"

name[0] = "J"
```

Output

```text
TypeError
```

Instead,

```python
name = "Jython"
```

creates a new string.

---

Python stores strings as Unicode.

Every character has a Unicode code point.

Example

```python
ord("A")
```

Output

```text
65
```

Example

```python
chr(65)
```

Output

```text
A
```

---

# 6. Examples

## Access Characters

```python
s = "Python"

s[0]

s[3]

s[-1]
```

---

## String Slicing

Syntax

```python
string[start:end:step]
```

Examples

```python
s = "Python"

s[0:2]

s[:4]

s[2:]

s[::-1]

s[::2]
```

---

## Concatenation

```python
first = "Hello"

second = "World"

first + " " + second
```

Output

```text
Hello World
```

---

## Repetition

```python
"Hi" * 3
```

Output

```text
HiHiHi
```

---

## Membership

```python
"Py" in "Python"

"Java" not in "Python"
```

---

## Looping

```python
for ch in "Python":
    print(ch)
```

---

## Reverse String

```python
s[::-1]
```

---

## ASCII

```python
ord("A")

chr(65)
```

---

# 7. Common Methods / Operations

| Method | Description |
|---------|-------------|
| len() | Length |
| lower() | Lowercase |
| upper() | Uppercase |
| title() | Title Case |
| capitalize() | Capitalize |
| strip() | Remove spaces |
| replace() | Replace substring |
| split() | Split string |
| join() | Join strings |
| find() | Find substring |
| index() | Find index |
| count() | Count occurrences |
| startswith() | Prefix check |
| endswith() | Suffix check |
| isalpha() | Alphabet only |
| isdigit() | Digits only |
| isalnum() | Alphanumeric |
| isspace() | Spaces only |

---

# 8. Time Complexity

| Operation | Complexity |
|-----------|------------|
| Indexing | O(1) |
| Length | O(1) |
| Slicing | O(k) |
| Concatenation | O(n+m) |
| Membership | O(n) |
| find() | O(n) |
| replace() | O(n) |
| split() | O(n) |
| join() | O(n) |
| Reverse | O(n) |

---

# 9. Memory Considerations

- Strings are immutable.
- Every modification creates a new string.
- Large numbers of concatenations consume extra memory.
- Prefer `"".join()` over repeated `+` inside loops.

---

# 10. Common Interview Questions

- Reverse String
- Valid Palindrome
- Valid Anagram
- Longest Common Prefix
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Group Anagrams
- Encode and Decode Strings
- String Compression
- Roman to Integer
- Integer to Roman

---

# 11. Common Mistakes

## Strings are immutable

Wrong

```python
s = "Python"

s[0] = "J"
```

---

Correct

```python
s = "J" + s[1:]
```

---

## Using "+" inside loops

Bad

```python
result = ""

for ch in words:
    result += ch
```

Better

```python
"".join(words)
```

---

## Confusing find() and index()

find()

Returns

```text
-1
```

if not found.

index()

Raises

```text
ValueError
```

---

## Forgetting Negative Indexing

```python
s[-1]
```

returns the last character.

---

# 12. Best Practices

- Use meaningful variable names.
- Use slicing instead of manual loops where appropriate.
- Use `join()` for concatenation in loops.
- Learn common string methods.
- Remember that strings are immutable.
- Prefer f-strings for formatting.

---

# 13. Cheat Sheet

| Task | Code |
|------|------|
| Length | len(s) |
| First Character | s[0] |
| Last Character | s[-1] |
| Reverse | s[::-1] |
| Uppercase | s.upper() |
| Lowercase | s.lower() |
| Remove Spaces | s.strip() |
| Split | s.split() |
| Join | "".join(lst) |
| Replace | s.replace(a,b) |
| Find | s.find(x) |
| Count | s.count(x) |
| Starts With | s.startswith(x) |
| Ends With | s.endswith(x) |
| ASCII | ord(ch) |
| Character | chr(65) |

---

# Revision Summary

- Strings are ordered and immutable.
- Support indexing and slicing.
- Unicode is supported.
- Learn the most common string methods.
- Prefer `join()` for repeated concatenation.
- Master slicing (`start:end:step`) before starting DSA string problems.