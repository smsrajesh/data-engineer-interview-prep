===================================================

Topic: range()

Category: Python Basics

Chapter: Loops

Difficulty: ⭐⭐☆☆☆

Interview Importance: ⭐⭐⭐⭐⭐

Industry Usage: ⭐⭐⭐⭐☆

===================================================

1. Problem

When a loop needs a sequence of numbers, manually writing every value is repetitive.

for number in [1, 2, 3, 4, 5]:
    print(number)

2. Real-World Problem

A Data Engineering script may need to process numbered batches:

Batch 1
Batch 2
...
Batch 100

We need a simple way to generate those numbers.

3. Why Not Do It Manually?

Instead of:

for batch_id in [1, 2, 3, 4, 5]:
    process_batch(batch_id)

we can describe the sequence with:

range(1, 6)

4. Python's Solution

range() is a built-in function that returns a range object representing a sequence of integers.

for number in range(1, 6):
    print(number)

Output:

1
2
3
4
5

5. What Is range()?

A range is represented using:

start
stop
step

Example:

print(list(range(5)))

Output:

[0, 1, 2, 3, 4]

range(5) is a range object; list(range(5)) is a list.

6. Why Should I Learn This?

range() is fundamental to Python loops and helps with:

Numeric sequences

Repetition

Counting forward/backward

Indexes

Batch/file/page processing

Python interview questions

7. Characteristics

start is included.

stop is excluded.

Default start is 0.

Default step is 1.

A negative step moves backward.

step = 0 is invalid.

Example:

list(range(2, 6))

[2, 3, 4, 5]

8. Syntax

range(stop)

list(range(5))
# [0, 1, 2, 3, 4]

range(start, stop)

list(range(2, 6))
# [2, 3, 4, 5]

range(start, stop, step)

list(range(2, 10, 2))
# [2, 4, 6, 8]

9. Behind the Scenes (Internal Working)

A range object is an iterable.

An iterator keeps track of the current position and provides the next value.

numbers = range(3)
iterator = iter(numbers)

print(next(iterator))

Output:

0

Conceptually:

range()
   ↓
iter()
   ↓
iterator
   ↓
next()
   ↓
value

10. Flow Diagram

range(start, stop, step)
          ↓
     range object
          ↓
       iterable
          ↓
        iter()
          ↓
       iterator
          ↓
        next()
          ↓
       value
          ↓
   execute loop body
          ↓
     more values?
      ↙       ↘
    yes        no
     ↓          ↓
  next()    StopIteration

11. In Action

Beginner

for number in range(1, 6):
    print(number)

Output:

1
2
3
4
5

Intermediate

list(range(10, 3, -2))

Output:

[10, 8, 6, 4]

Interview

list(range(20, 5, -5))

Output:

[20, 15, 10]

5 is excluded.

Data Engineering

for batch_id in range(1, 6):
    process_batch(batch_id)

The same pattern can represent batch IDs, file numbers, API pages, or partition IDs.

12. Performance Notes

Creating a range object:

Time  → O(1)
Space → O(1)

Iterating through n values:

Time → O(n)

Compare:

range(1000000000)

with:

list(range(1000000000))

The second materializes the values and therefore uses much more memory.

13. Real-World Usage

Common uses include:

for _ in range(5):
    run_task()

for i in range(len(records)):
    process(records[i])

for page in range(1, 101):
    fetch_page(page)

Use the simplest form that matches the task.

14. Cross Technology Mapping

Python

for i in range(1, 6):
    process(i)

SQL / Snowflake

SQL generally uses set-based processing rather than explicit Python-style loops.

Spark

Spark normally applies transformations to datasets rather than manually looping through rows.

Airflow

Airflow focuses on workflow orchestration, DAGs, scheduling, and task dependencies.

range() → Python control flow
SQL/Spark → dataset processing
Airflow → workflow orchestration

15. Common Mistakes

stop is excluded

list(range(1, 5))
# [1, 2, 3, 4]

Reverse ranges need a negative step

list(range(5, 0))
# []

Use:

range(5, 0, -1)

Zero step is invalid

range(1, 10, 0)
# ValueError

Range is not a list

range(5)          # range object
list(range(5))    # list

16. Best Practices

Remember that stop is excluded.

Use a negative step for reverse ranges.

Never use step = 0.

Don't convert range() to a list unless you need a list.

Use range(len(sequence)) only when the index is actually required.

Prefer meaningful names such as batch_id or page_number.

17. Interview Perspective

Frequently Asked

What is range()?

A built-in Python function that returns a range object representing a sequence of integers.

What are its forms?

range(stop)
range(start, stop)
range(start, stop, step)

Is stop included?

No.

Is a range object an iterator?

No. It is iterable.

iterator = iter(range(5))

Why is range() memory efficient?

It represents the sequence without materializing all values into a list.

Interview Trap

list(range(5, 0))

is:

[]

not:

[5, 4, 3, 2, 1]

The default step is +1.

18. Industry Adoption

range() is a standard Python feature used in:

Data Engineering

ETL scripts

Automation

API integrations

Batch processing

File processing

Testing

It is a control-flow tool, not a distributed data-processing mechanism.

19. Practice Questions

We will solve these using our Coding Workflow.

Beginner

Print numbers from 1 to 20.

Print numbers from 20 down to 1.

Print even numbers from 1 to 50.

Intermediate

Find the sum of numbers from 1 to 100.

Print a multiplication table.

Generate data_001.csv through data_020.csv.

Interview

Predict:

list(range(10, 2, -2))

Explain why:

list(range(5, 0))

is empty.

Explain:

range(5)

vs.

list(range(5))

Explain iterable vs iterator using range().

20. Key Takeaways

range(stop)
range(start, stop)
range(start, stop, step)

start → included
stop  → excluded

positive step → forward
negative step → backward
zero step     → error

range()
   ↓
range object
   ↓
iterable

iter(range object)
   ↓
iterator

range() represents a controlled sequence of integers and is commonly used with Python loops.

21. What's Next?

Continue with:

range()
   ↓
for loop
   ↓
while loop
   ↓
break
   ↓
continue
   ↓
nested loops
   ↓
loop-based problem solving

Later, iterable/iterator concepts will connect to generators and lazy evaluation.

