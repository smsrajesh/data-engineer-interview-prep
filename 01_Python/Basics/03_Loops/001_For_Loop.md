# ===================================================
# Topic: For Loop
# Category: Python Basics
# Chapter: Loops
# Difficulty: ⭐⭐☆☆☆
# Learning Priority: ⭐⭐⭐⭐⭐
# Interview Importance: ⭐⭐⭐⭐⭐
# Industry Usage: ⭐⭐⭐⭐⭐
# ===================================================

# 🧩 The Problem

Imagine your teacher gives you the following task.

Write the sentence:

"I will practice Python."

100 times.

One possible solution is:

```python
print("I will practice Python.")
print("I will practice Python.")
print("I will practice Python.")
...
```

Would anyone actually do this?

Of course not.

Now think about a software application.

It needs to send a welcome email to **50,000 newly registered users**.

Should we write:

```python
send_email(user1)
send_email(user2)
send_email(user3)
...
send_email(user50000)
```

Again...

No.

The problem isn't printing.

The problem isn't sending emails.

The real problem is **repetition**.

Programming languages needed a way to repeat tasks automatically.

---

# 🌍 Real-World Problem

Now let's think like a Data Engineer.

Every night an ETL pipeline receives a CSV file containing millions of customer records.

Every record must go through the same steps.

```text
Read Record
      │
      ▼
Validate
      │
      ▼
Clean
      │
      ▼
Transform
      │
      ▼
Load into Snowflake
```

Would we write:

```python
validate(record1)
validate(record2)
validate(record3)
...
```

No.

Instead we tell Python:

> "Repeat these steps for every record."

This is exactly the problem that loops solve.

---

# ❓ Why Not Repeat the Code Manually?

Repeating code creates several problems.

## 1. Duplicate Code

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

The same code appears multiple times.

---

## 2. Difficult Maintenance

Suppose:

```python
print("Hello")
```

must become:

```python
print("Welcome")
```

Imagine changing this in **10,000 places**.

---

## 3. Easy to Make Mistakes

Humans get tired of repetitive work.

Computers do not.

Automation reduces mistakes.

---

## 4. Doesn't Scale

Repeating something 5 times?

Easy.

Repeating something 5 million times?

Impossible.

---

# 💡 The Idea

Instead of writing the same code repeatedly,

what if we simply told Python:

> Repeat this block of code for every item.

Python would do the repetition automatically.

This idea is called **iteration**.

---

# ✅ Python's Solution

Python provides looping statements.

The two main ones are:

- `for`
- `while`

A **for loop** is used when we already have a group of items and want to process them **one by one**.

Examples:

- Customer records
- Employee names
- Product IDs
- CSV rows
- File lines

---

# 📖 What is a For Loop?

A **for loop** is a control structure that executes the same block of code once for each item in a sequence.

Think of it like this:

```text
One Task
      │
      ▼
Many Items
      │
      ▼
Automatic Repetition
```

Instead of writing the same code many times,

we write it **once**,

and Python repeats it for us.

---

# 🤔 Why Should I Learn This?

You'll use `for` loops almost everywhere.

Examples include:

- Reading CSV files
- Processing JSON
- Reading log files
- Calling APIs
- Traversing strings
- Processing lists
- ETL pipelines
- Automation scripts
- Data analysis
- DSA problems

If variables **store data**,

then loops **process data**.

---

# 📌 Quick Check

Before moving on, make sure you can answer these questions.

1. What problem does a `for` loop solve?

2. Why is repeating code considered a bad practice?

3. In the ETL example, why don't we call `validate()` for every record manually?

4. What is iteration?

5. Name three real-world situations where a `for` loop can be used.



---

# 📦 What Can a For Loop Process?

A `for` loop can process any object that Python can read **one item at a time**.

Let's look at some examples.

---

## Example 1 — List

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
Apple
Banana
Orange
```

### What Happened?

Python processed the list like this.

```text
Apple
   │
   ▼
Banana
   │
   ▼
Orange
```

It visited one element at a time.

---

## Example 2 — String

```python
language = "Python"

for letter in language:
    print(letter)
```

### Output

```text
P
y
t
h
o
n
```

Python processes one character at a time.

```text
P
│
▼
y
│
▼
t
│
▼
h
│
▼
o
│
▼
n
```

---

## Example 3 — Tuple

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

Output

```text
10
20
30
```

---

## Example 4 — Dictionary

```python
student = {
    "name": "Rajesh",
    "age": 25,
    "city": "Hyderabad"
}

for key in student:
    print(key)
```

### Output

```text
name
age
city
```

Notice something interesting.

Python returned the **keys**, not the values.

We'll learn why when we study dictionaries.

---

## Example 5 — File

```python
with open("employees.txt") as file:

    for line in file:
        print(line)
```

Python reads one line at a time instead of loading the whole file into memory.

This is why `for` loops are heavily used in Data Engineering.

---

# 💡 A New Term — Iterable

So far we've learned that a `for` loop can process:

- Lists
- Strings
- Tuples
- Dictionaries
- Files

Python has a special name for objects that can be processed one item at a time.

They are called **Iterables**.

> **Definition**
>
> An iterable is any object that Python can process one element at a time.

Examples include:

✅ List

✅ Tuple

✅ String

✅ Dictionary

✅ Set

✅ File

✅ Range

Don't worry about memorizing the word.

Remember the idea instead.

> If Python can visit one item after another,
> it is usually an iterable.

---

# ⚙️ Syntax

General Syntax

```python
for variable in iterable:
    statements
```

Let's understand every part.

```python
for fruit in fruits:
    print(fruit)
```

### `for`

Starts the loop.

---

### `fruit`

A temporary variable that stores the current item.

---

### `in`

Means

> "Take one item from..."

---

### `fruits`

The iterable object.

---

### `:`

Marks the beginning of the loop body.

---

### Indentation

Everything inside the indentation belongs to the loop.

```python
for fruit in fruits:
    print(fruit)
```

The indented statement executes once for every element.

---

# 🎬 Step-by-Step Execution

Consider the following code.

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

Python executes it like this.

### Iteration 1

```text
fruit = Apple
```

Output

```text
Apple
```

---

### Iteration 2

```text
fruit = Banana
```

Output

```text
Banana
```

---

### Iteration 3

```text
fruit = Orange
```

Output

```text
Orange
```

---

No more elements remain.

The loop ends automatically.

---

# 🧠 Behind the Scenes

Now comes the interesting part.

How does Python know which item comes next?

Imagine reading a book.

You place a bookmark where you stopped.

```text
Page 1
   │
   ▼
Page 2
   │
   ▼
Page 3
```

Every time you continue reading,

you move the bookmark.

Python uses a similar idea.

It creates something called an **Iterator**.

An iterator remembers:

> "Which item should I return next?"

Suppose we have:

```text
10

20

30
```

Initially

```text
▼
10

20

30
```

After one iteration

```text
10

▼
20

30
```

After another

```text
10

20

▼
30
```

Finally

```text
10

20

30

▼

End
```

This moving position is the iterator.

---

Internally, Python performs something conceptually similar to:

```python
iterator = iter(numbers)

while True:

    try:
        item = next(iterator)
        print(item)

    except StopIteration:
        break
```

Don't worry if you don't understand this code yet.

We'll study:

- `iter()`
- `next()`
- `StopIteration`

in the **Advanced Python** chapter.

For now, just remember this picture.

```text
Iterable
     │
     ▼
Iterator
     │
     ▼
Next Item
     │
     ▼
Execute Loop Body
     │
     ▼
More Items?
     │
  Yes ▼ No
     │
Repeat   End
```

---

# 📌 Quick Check

1. Name five objects that can be used with a `for` loop.

2. What is an iterable?

3. What is the purpose of the loop variable?

4. Why is indentation important?

5. What is the job of an iterator?


---

# 🌍 Real-World Applications

Now that you understand how a `for` loop works, let's see where it is actually used.

---

## 1. Reading a CSV File

```python
import csv

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["employee_name"])
```

Every row in the CSV file is processed one by one.

---

## 2. Processing API Data

```python
customers = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

for customer in customers:
    print(customer["name"])
```

In production, instead of `print()`, you may:

- Validate data
- Transform data
- Insert into Snowflake
- Store in S3
- Send messages to Kafka

---

## 3. Reading Log Files

```python
with open("application.log") as log_file:

    for line in log_file:
        print(line.strip())
```

Python processes one line at a time, making it memory efficient.

---

## 4. Data Validation

```python
ages = [22, 17, 35, 15, 28]

for age in ages:

    if age >= 18:
        print(f"{age} -> Eligible")

    else:
        print(f"{age} -> Not Eligible")
```

---

# ⚡ Performance Analysis

Suppose there are **n** elements.

### Time Complexity

```text
O(n)
```

Python visits every element exactly once.

---

### Space Complexity

```text
O(1)
```

The loop itself stores only:

- Loop variable
- Iterator

It does not create another copy of the iterable.

> **Note:** The overall space usage may be higher depending on what your loop does (for example, if you build a new list inside the loop).

---

# 🌉 Cross-Technology Mapping

One of the goals of this handbook is to connect concepts across technologies.

## Python

```python
for employee in employees:
    process(employee)
```

Processes one item at a time.

---

## SQL

```sql
SELECT *
FROM employees;
```

SQL does **not** use explicit loops.

Instead, it processes sets of rows.

---

## Spark

```python
df.filter(...)
  .select(...)
```

Spark encourages transformations on datasets instead of explicit row-by-row loops.

---

## Snowflake

```sql
SELECT *
FROM employee;
```

Like SQL, Snowflake uses set-based operations.

---

## Airflow

Airflow doesn't iterate over data.

Instead, it repeatedly executes tasks according to a schedule.

Example:

```text
Every day at 8 AM

↓

Run Pipeline
```

The idea of repetition exists, but at the workflow level rather than the row level.

---

# ⚠️ Common Mistakes

## Mistake 1

Trying to iterate over an integer.

```python
number = 100

for x in number:
    print(x)
```

Result

```text
TypeError
```

Integers are not iterable.

---

## Mistake 2

Modifying a list while iterating.

```python
numbers = [1, 2, 3, 4]

for number in numbers:

    if number == 2:
        numbers.remove(number)
```

This can lead to unexpected results because the list changes while it is being traversed.

---

## Mistake 3

Poor variable names.

❌

```python
for x in employees:
```

✅ Better

```python
for employee in employees:
```

Meaningful names improve readability.

---

## Mistake 4

Incorrect indentation.

```python
for i in range(5):
print(i)
```

Python raises an `IndentationError`.

---

# ✅ Best Practices

✔ Use descriptive loop variable names.

✔ Keep the loop body short and readable.

✔ Move complex logic into separate functions.

✔ Prefer `for` over `while` when processing an existing sequence.

✔ Avoid modifying collections while iterating.

✔ Add comments only when the purpose of the loop is not obvious.

---

# 💼 Interview Perspective

### Frequently Asked Questions

**Q1. What is a `for` loop?**

A control structure used to execute a block of code once for each item in an iterable.

---

**Q2. What is an iterable?**

An object that Python can process one element at a time.

Examples:

- List
- Tuple
- String
- Dictionary
- Set
- File
- Range

---

**Q3. Why is a `for` loop preferred over a `while` loop?**

Because:

- Simpler
- Safer
- More readable
- Stops automatically when all items are processed

---

**Q4. Can a `for` loop iterate over an integer?**

No.

Integers are not iterable.

---

**Q5. What happens internally when a `for` loop executes?**

Python creates an iterator and repeatedly retrieves the next item until there are no more items to process.

---

# 🧪 Practice Questions

## Concept Check

1. What problem does a `for` loop solve?
2. What is an iterable?
3. Why does a `for` loop stop automatically?
4. Why are strings iterable?
5. Why are integers not iterable?

---

## Predict the Output

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

---

```python
for letter in "AI":
    print(letter)
```

---

## Coding Practice

1. Print numbers from 1 to 10.
2. Print all names in a list.
3. Count the total number of vowels in a string.
4. Calculate the sum of numbers in a list.
5. Find the largest number in a list.

---

## Real-World Scenario

A retail company receives a list of product prices.

Use a `for` loop to:

- Print each product price.
- Count the number of products.
- Calculate the total price.

---

# 📌 Key Takeaways

- A `for` loop automates repetition.
- It processes one item at a time.
- It works with iterable objects.
- Python uses an iterator internally.
- A `for` loop automatically stops after the last item.
- Prefer `for` loops when processing existing sequences.
- `for` loops are widely used in ETL pipelines, automation, file processing, and data analysis.

---

# 🚀 What's Next?

Most examples in this chapter used something like:

```python
for i in range(5):
```

This raises a few questions.

- What is `range()`?
- Does `range()` create a list?
- How can it count backwards?
- How can it skip numbers?

We'll answer these questions in the next note.

➡ **002_Range_Function.md**

---

# 📌 Quick Check

Before moving on, make sure you can answer:

1. What is the purpose of a `for` loop?
2. What objects can be used with a `for` loop?
3. What is an iterable?
4. Why is `for` usually preferred over `while` for processing sequences?
5. Where have you seen `for` loops used in Data Engineering?