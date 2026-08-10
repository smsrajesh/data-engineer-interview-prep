# Gaps and Islands in SQL

## 1. What is Gaps and Islands?

**Gaps and Islands** is a SQL technique used to identify:

* Consecutive records grouped into the same **island**
* Breaks between consecutive records called **gaps**
* Longest or shortest consecutive streaks
* Start and end dates of consecutive periods
* Number of separate activity periods
* Missing dates between activity periods

It is commonly used with:

* Customer activity
* Employee attendance
* Login streaks
* Transaction activity
* Order history
* Machine/system events
* Consecutive business days

---

# 2. Basic Example

Suppose a customer has activity on:

```text
Jan 1
Jan 2
Jan 3
Jan 7
Jan 8
Jan 10
Jan 11
Jan 12
```

The dates form three islands:

```text
Island 1 → Jan 1, Jan 2, Jan 3
Island 2 → Jan 7, Jan 8
Island 3 → Jan 10, Jan 11, Jan 12
```

Their sizes are:

```text
Island 1 → 3
Island 2 → 2
Island 3 → 3
```

The gaps are:

```text
Jan 3 → Jan 7
Jan 8 → Jan 10
```

---

# 3. Core Gaps & Islands Pattern

The most important pattern is:

```text
DISTINCT
   ↓
LAG()
   ↓
DATEDIFF()
   ↓
CASE → identify new island
   ↓
Running SUM()
   ↓
island_id
   ↓
COUNT / MIN / MAX / ROW_NUMBER
```

The first four steps create the islands.

The final steps depend on what the question asks.

---

# 4. Step 1 — Remove Duplicate Dates

If duplicate records for the same customer and date may exist, remove them first.

```sql
WITH valid_data AS (
    SELECT DISTINCT
        customer_id,
        activity_date
    FROM customer_activity
)
```

### Why?

Suppose the data contains:

```text
A | Jan 1
A | Jan 1
A | Jan 2
A | Jan 3
```

We want:

```text
A | Jan 1
A | Jan 2
A | Jan 3
```

Otherwise duplicate records can incorrectly affect streak counts.

---

# 5. Step 2 — Find the Previous Date

Use `LAG()`:

```sql
LAG(activity_date) OVER (
    PARTITION BY customer_id
    ORDER BY activity_date
) AS previous_date
```

Example:

| customer_id | activity_date | previous_date |
| ----------- | ------------- | ------------- |
| A           | Jan 1         | NULL          |
| A           | Jan 2         | Jan 1         |
| A           | Jan 3         | Jan 2         |
| A           | Jan 7         | Jan 3         |
| A           | Jan 8         | Jan 7         |

### Why `PARTITION BY`?

Each customer must have an independent sequence.

Without:

```sql
PARTITION BY customer_id
```

the previous record could come from another customer.

---

# 6. Step 3 — Identify New Islands

For consecutive calendar days:

```sql
CASE
    WHEN DATEDIFF(
        DAY,
        previous_date,
        activity_date
    ) = 1
    THEN 0
    ELSE 1
END AS is_new_island
```

Meaning:

```text
0 → continue the existing island
1 → start a new island
```

Example:

| activity_date | previous_date | is_new_island |
| ------------- | ------------- | ------------: |
| Jan 1         | NULL          |             1 |
| Jan 2         | Jan 1         |             0 |
| Jan 3         | Jan 2         |             0 |
| Jan 7         | Jan 3         |             1 |
| Jan 8         | Jan 7         |             0 |
| Jan 10        | Jan 8         |             1 |
| Jan 11        | Jan 10        |             0 |
| Jan 12        | Jan 11        |             0 |

The first row gets `1` because there is no previous date.

---

# 7. Step 4 — Generate the Island ID

Use a running `SUM()`:

```sql
SUM(is_new_island) OVER (
    PARTITION BY customer_id
    ORDER BY activity_date
) AS island_id
```

Example:

| activity_date | is_new_island | island_id |
| ------------- | ------------: | --------: |
| Jan 1         |             1 |         1 |
| Jan 2         |             0 |         1 |
| Jan 3         |             0 |         1 |
| Jan 7         |             1 |         2 |
| Jan 8         |             0 |         2 |
| Jan 10        |             1 |         3 |
| Jan 11        |             0 |         3 |
| Jan 12        |             0 |         3 |

Now every consecutive period has its own identifier.

---

# 8. Complete Island Creation Query

```sql
WITH valid_data AS (
    SELECT DISTINCT
        customer_id,
        activity_date
    FROM customer_activity
),

previous_date_cte AS (
    SELECT
        customer_id,
        activity_date,
        LAG(activity_date) OVER (
            PARTITION BY customer_id
            ORDER BY activity_date
        ) AS previous_date
    FROM valid_data
),

is_new_island_cte AS (
    SELECT
        customer_id,
        activity_date,
        CASE
            WHEN DATEDIFF(
                DAY,
                previous_date,
                activity_date
            ) = 1
            THEN 0
            ELSE 1
        END AS is_new_island
    FROM previous_date_cte
),

island_id_cte AS (
    SELECT
        customer_id,
        activity_date,
        SUM(is_new_island) OVER (
            PARTITION BY customer_id
            ORDER BY activity_date
        ) AS island_id
    FROM is_new_island_cte
)

SELECT *
FROM island_id_cte;
```

---

# 9. Finding the Size of Each Island

Once `island_id` exists:

```sql
COUNT(*) OVER (
    PARTITION BY customer_id, island_id
) AS island_count
```

Example:

| customer_id | activity_date | island_id | island_count |
| ----------- | ------------- | --------: | -----------: |
| A           | Jan 1         |         1 |            3 |
| A           | Jan 2         |         1 |            3 |
| A           | Jan 3         |         1 |            3 |
| A           | Jan 7         |         2 |            2 |
| A           | Jan 8         |         2 |            2 |
| A           | Jan 10        |         3 |            3 |
| A           | Jan 11        |         3 |            3 |
| A           | Jan 12        |         3 |            3 |

### Important

Use:

```sql
PARTITION BY customer_id, island_id
```

not just:

```sql
PARTITION BY island_id
```

because `island_id = 1` can exist for multiple customers.

---

# 10. Longest Consecutive Streak

Once we have `island_count`, find the maximum per customer:

```sql
SELECT
    customer_id,
    MAX(island_count) AS longest_streak
FROM island_count_cte
GROUP BY customer_id;
```

### Complete pattern

```text
DISTINCT
   ↓
LAG()
   ↓
DATEDIFF()
   ↓
CASE
   ↓
Running SUM()
   ↓
island_id
   ↓
COUNT()
   ↓
MAX()
```

---

# 11. Employees With at Least 3 Consecutive Days

Use:

```sql
HAVING MAX(island_count) >= 3
```

Example:

```sql
SELECT
    employee_id
FROM island_count_cte
GROUP BY employee_id
HAVING MAX(island_count) >= 3;
```

The logic is:

```text
Any island >= 3
        ↓
MAX(island_count) >= 3
        ↓
Employee qualifies
```

---

# 12. Start and End Dates of Every Island

Once we have `island_id`, group by it:

```sql
SELECT
    customer_id,
    island_id,
    MIN(activity_date) AS start_date,
    MAX(activity_date) AS end_date
FROM island_id_cte
GROUP BY
    customer_id,
    island_id;
```

Example:

| customer_id | island_id | start_date | end_date |
| ----------- | --------: | ---------- | -------- |
| A           |         1 | Jan 1      | Jan 3    |
| A           |         2 | Jan 7      | Jan 8    |
| A           |         3 | Jan 10     | Jan 12   |

### Remember

```text
MIN(date) → start of island
MAX(date) → end of island
```

---

# 13. Number of Islands Per Customer

After generating `island_id`, we can count the number of distinct islands:

```sql
SELECT
    customer_id,
    COUNT(DISTINCT island_id) AS island_count
FROM island_id_cte
GROUP BY customer_id;
```

Alternatively:

```sql
SELECT
    customer_id,
    COUNT(*) AS island_count
FROM (
    SELECT DISTINCT
        customer_id,
        island_id
    FROM island_id_cte
)
GROUP BY customer_id;
```

---

# 14. Finding Gaps

If the question asks:

> Find gaps between consecutive activity dates.

We don't need to create an `island_id`.

We only need:

```text
LAG()
   ↓
DATEDIFF()
   ↓
WHERE gap > 1
```

Example:

```sql
WITH valid_data AS (
    SELECT DISTINCT
        customer_id,
        activity_date
    FROM customer_activity
),

previous_date_cte AS (
    SELECT
        customer_id,
        activity_date,
        LAG(activity_date) OVER (
            PARTITION BY customer_id
            ORDER BY activity_date
        ) AS previous_date
    FROM valid_data
),

gap_cte AS (
    SELECT
        customer_id,
        previous_date,
        activity_date AS next_activity_date,
        DATEDIFF(
            DAY,
            previous_date,
            activity_date
        ) AS gap_days
    FROM previous_date_cte
)

SELECT
    customer_id,
    previous_date AS previous_activity_date,
    next_activity_date,
    gap_days
FROM gap_cte
WHERE gap_days > 1;
```

---

# 15. Understanding `gap_days`

Suppose:

```text
Jan 3 → Jan 7
```

Then:

```sql
DATEDIFF(DAY, 'Jan 3', 'Jan 7')
```

returns:

```text
4
```

But the actual missing dates are:

```text
Jan 4
Jan 5
Jan 6
```

Therefore:

```text
gap_days = 4
missing_days = gap_days - 1
```

---

# 16. Longest Streak With Start and End Dates

This is a slightly more advanced problem.

First create one row per island:

```sql
WITH island_summary AS (
    SELECT
        customer_id,
        island_id,
        MIN(activity_date) AS start_date,
        MAX(activity_date) AS end_date,
        MAX(island_count) AS island_count
    FROM island_count_cte
    GROUP BY
        customer_id,
        island_id
)
```

Then rank the islands:

```sql
ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY
        island_count DESC,
        start_date ASC
) AS rn
```

The ordering means:

```text
1. Longest island first
2. If tied → earliest island first
```

Then:

```sql
WHERE rn = 1
```

returns the longest streak.

---

# 17. Why `ROW_NUMBER()` Is Important Here

Suppose customer A has:

```text
Island 1 → Jan 1 to Jan 3 → 3 days
Island 2 → Jan 7 to Jan 8 → 2 days
Island 3 → Jan 10 to Jan 12 → 3 days
```

There is a tie between Island 1 and Island 3.

Use:

```sql
ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY
        island_count DESC,
        start_date ASC
)
```

Result:

| island | count | start_date | rn |
| ------ | ----: | ---------- | -: |
| 1      |     3 | Jan 1      |  1 |
| 3      |     3 | Jan 10     |  2 |
| 2      |     2 | Jan 7      |  3 |

Therefore:

```sql
WHERE rn = 1
```

returns the earliest longest island.

---

# 18. Generating Actual Missing Dates in Snowflake

Sometimes the question asks for:

> Return the actual missing dates, not just the size of the gap.

Example:

```text
Jan 3 → Jan 7
```

Expected:

```text
Jan 4
Jan 5
Jan 6
```

Snowflake provides `GENERATOR()` for creating rows.

First create a sequence:

```sql
SELECT
    ROW_NUMBER() OVER (
        ORDER BY SEQ4()
    ) AS n
FROM TABLE(
    GENERATOR(ROWCOUNT => 100)
);
```

This produces:

```text
1
2
3
...
100
```

Then use `DATEADD()`:

```sql
DATEADD(
    DAY,
    n,
    previous_date
)
```

For:

```text
previous_date = Jan 3
```

we get:

```text
n = 1 → Jan 4
n = 2 → Jan 5
n = 3 → Jan 6
```

---

# 19. Complete Missing-Date Query — Snowflake

```sql
WITH valid_data AS (

    SELECT DISTINCT
        customer_id,
        activity_date
    FROM customer_activity
),

previous_date_cte AS (

    SELECT
        customer_id,
        activity_date,
        LAG(activity_date) OVER (
            PARTITION BY customer_id
            ORDER BY activity_date
        ) AS previous_date
    FROM valid_data
),

gap_cte AS (

    SELECT
        customer_id,
        previous_date,
        activity_date AS next_activity_date,
        DATEDIFF(
            DAY,
            previous_date,
            activity_date
        ) AS gap_days
    FROM previous_date_cte
    WHERE DATEDIFF(
        DAY,
        previous_date,
        activity_date
    ) > 1
),

numbers AS (

    SELECT
        ROW_NUMBER() OVER (
            ORDER BY SEQ4()
        ) AS n
    FROM TABLE(
        GENERATOR(ROWCOUNT => 100)
    )
)

SELECT
    g.customer_id,
    DATEADD(
        DAY,
        n.n,
        g.previous_date
    ) AS missing_date
FROM gap_cte g
CROSS JOIN numbers n
WHERE n.n < g.gap_days
ORDER BY
    g.customer_id,
    missing_date;
```

### Important idea

Do not memorize the entire query.

Remember:

```text
Gap
 ↓
gap_days
 ↓
Generate numbers
 ↓
n < gap_days
 ↓
DATEADD(day, n, previous_date)
 ↓
Missing dates
```

---

# 20. Business-Day Islands

Sometimes weekends should **not** break a streak.

Example:

```text
Friday → Monday
```

Normally:

```text
DATEDIFF = 3
```

But if weekends are ignored, Friday and Monday may belong to the same streak.

A simple interview-specific solution can explicitly handle:

```text
Friday → Monday
```

However, a production solution should preferably use a **calendar/business-day table**.

---

# 21. INNER JOIN vs CROSS JOIN in Gaps & Islands

Two different joins are used in the Gaps & Islands variations we covered. They serve completely different purposes.

## A. Attendance → Calendar: `INNER JOIN`

When using a business calendar, we need to match each attendance date with its corresponding calendar record.

```sql
SELECT
    a.employee_id,
    a.attendance_date,
    c.business_day_number
FROM employee_attendance a
INNER JOIN dim_calendar c
    ON a.attendance_date = c.calendar_date
WHERE c.is_business_day = TRUE;
```

### Why `INNER JOIN`?

We are performing a **key-based lookup**:

```text
attendance_date
       ↓
matches
       ↓
calendar_date
```

For example:

```text
employee_attendance
E1 | 2026-01-09

        ↓ JOIN

dim_calendar
2026-01-09 | TRUE | 101

        ↓

E1 | 2026-01-09 | 101
```

The purpose is:

> **Match each attendance date with its business-day information.**

---

## B. Gap → Generated Numbers: `CROSS JOIN`

When generating the actual missing dates, we have:

```text
gap_cte

customer | previous_date | next_date | gap_days
A        | Jan 3         | Jan 7     | 4
A        | Jan 8         | Jan 12    | 4
```

And a generated sequence:

```text
numbers

n
1
2
3
4
5
...
```

We need to pair each gap with the generated numbers.

Therefore, we use:

```sql
CROSS JOIN numbers n
```

Example:

```sql
SELECT
    g.customer_id,
    g.previous_date,
    g.next_activity_date,
    g.gap_days,
    n.n
FROM gap_cte g
CROSS JOIN numbers n
WHERE n.n < g.gap_days;
```

For:

```text
Jan 3 → Jan 7
gap_days = 4
```

the filter:

```sql
n.n < g.gap_days
```

keeps:

```text
1
2
3
```

Then:

```sql
DATEADD(
    DAY,
    n.n,
    g.previous_date
)
```

produces:

```text
Jan 4
Jan 5
Jan 6
```

### Why `CROSS JOIN`?

We want to create combinations between:

```text
Every gap
    ×
Generated numbers
```

Then we filter those combinations according to the size of each gap.

---

## Key Difference

| Situation               | Join         | Why?                                           |
| ----------------------- | ------------ | ---------------------------------------------- |
| Attendance → Calendar   | `INNER JOIN` | Match each attendance date to its calendar row |
| Gap → Generated numbers | `CROSS JOIN` | Generate multiple rows for every gap           |

### Easy way to remember

```text
INNER JOIN
→ "Find the matching information."

CROSS JOIN
→ "Create combinations."
```

So:

```text
Attendance + Calendar
        ↓
    INNER JOIN
        ↓
Business-day information
```

while:

```text
Gap + Numbers
        ↓
    CROSS JOIN
        ↓
Multiple rows for each gap
        ↓
DATEADD()
        ↓
Actual missing dates
```

**Important:** `CROSS JOIN` is not specifically a "Gaps & Islands join." It is used here because we need to pair each gap with a sequence of generated numbers.

---

# 22. Common Mistakes

## Mistake 1 — Not removing duplicates

If duplicate dates exist:

```text
A | Jan 1
A | Jan 1
A | Jan 2
```

use:

```sql
SELECT DISTINCT
    customer_id,
    activity_date
```

before applying `LAG()`.

---

## Mistake 2 — Forgetting `PARTITION BY`

Incorrect:

```sql
LAG(activity_date) OVER (
    ORDER BY activity_date
)
```

For customer-level problems, usually use:

```sql
LAG(activity_date) OVER (
    PARTITION BY customer_id
    ORDER BY activity_date
)
```

---

## Mistake 3 — Using only `island_id` for partitioning

Incorrect:

```sql
COUNT(*) OVER (
    PARTITION BY island_id
)
```

Correct:

```sql
COUNT(*) OVER (
    PARTITION BY customer_id, island_id
)
```

Because `island_id = 1` can exist for many customers.

---

## Mistake 4 — Confusing `gap_days` with missing days

For:

```text
Jan 3 → Jan 7
```

```text
gap_days = 4
missing days = 3
```

So actual missing dates require:

```text
1 through gap_days - 1
```

---

## Mistake 5 — Using `ROW_NUMBER()` incorrectly

When ranking islands:

Incorrect concept:

```sql
PARTITION BY customer_id, island_count
```

Instead:

```sql
ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY island_count DESC,
             start_date ASC
)
```

`PARTITION BY` defines **who gets ranked independently**.

`ORDER BY` defines **how they are ranked**.

---

# 23. Interview Question Patterns

When you see these questions, recognize the pattern immediately.

### Pattern 1 — Longest streak

> Find the longest consecutive login streak.

```text
LAG
→ DATEDIFF
→ CASE
→ Running SUM
→ COUNT
→ MAX
```

---

### Pattern 2 — At least N consecutive days

> Find employees with at least 3 consecutive attendance days.

```text
LAG
→ DATEDIFF
→ island_id
→ island_count
→ HAVING MAX(island_count) >= 3
```

---

### Pattern 3 — Start and end of every streak

> Return the start and end dates of each consecutive period.

```text
LAG
→ DATEDIFF
→ island_id
→ GROUP BY customer_id, island_id
→ MIN(date), MAX(date)
```

---

### Pattern 4 — Find gaps

> Find gaps between activity periods.

```text
LAG
→ DATEDIFF
→ WHERE gap > 1
```

No `island_id` is required.

---

### Pattern 5 — Longest streak with dates

> Find the longest streak and return its start/end dates.

```text
Create islands
→ summarize each island
→ ROW_NUMBER()
→ ORDER BY island_count DESC, start_date ASC
→ rn = 1
```

---

### Pattern 6 — Actual missing dates

> Return every missing date.

```text
LAG
→ DATEDIFF
→ GENERATOR
→ ROW_NUMBER
→ CROSS JOIN
→ DATEADD
```

---

# 24. The Most Important Mental Model

Do not memorize individual queries.

Remember this:

```text
                GAPS & ISLANDS
                       |
              +--------+--------+
              |                 |
            GAPS             ISLANDS
              |                 |
           LAG()             LAG()
              |                 |
         DATEDIFF()          DATEDIFF()
              |                 |
          gap > 1          CASE 0 / 1
                                |
                           Running SUM
                                |
                            island_id
                                |
                    +-----------+-----------+
                    |           |           |
                  COUNT       MIN/MAX     ROW_NUMBER
                    |           |           |
               island size   boundaries   ranking
                    |
                   MAX
                    |
              longest streak
```

The central idea is:

> **First identify where a new group starts. Then create an `island_id`. Once you have `island_id`, many different questions become simple aggregations.**

---

# 25. Quick Interview Cheat Sheet

| Requirement               | Main technique                         |
| ------------------------- | -------------------------------------- |
| Find previous record      | `LAG()`                                |
| Detect gap                | `DATEDIFF()`                           |
| Mark new island           | `CASE`                                 |
| Create island ID          | Running `SUM()`                        |
| Island size               | `COUNT()`                              |
| Island start              | `MIN()`                                |
| Island end                | `MAX()`                                |
| Longest island            | `MAX()`                                |
| Rank islands              | `ROW_NUMBER()`                         |
| Handle duplicate dates    | `DISTINCT`                             |
| Find actual missing dates | `GENERATOR()` + `DATEADD()`            |
| Business-day streak       | Calendar table + business-day sequence |

---

# 26. Final Interview Checklist

Before considering a Gaps & Islands problem solved, ask:

1. **Are duplicate records possible?**

   * If yes → `DISTINCT` first.

2. **What defines consecutive?**

   * Calendar day?
   * Business day?
   * Month?
   * Week?
   * Sequential number?

3. **Do I need `LAG()`?**

   * Usually yes for date-based gaps/islands.

4. **How do I identify a new island?**

   * `CASE`.

5. **Do I need an `island_id`?**

   * Yes for most island questions.
   * Not necessarily for a simple gap-finding problem.

6. **What does the question ask after identifying islands?**

   * Size → `COUNT`
   * Start → `MIN`
   * End → `MAX`
   * Longest → `MAX`
   * Rank → `ROW_NUMBER`
   * Number of islands → `COUNT(DISTINCT island_id)`
   * Actual missing dates → `GENERATOR` + `DATEADD`

---

## Core Pattern to Remember

```sql
LAG()
    ↓
DATEDIFF()
    ↓
CASE
    ↓
Running SUM()
    ↓
island_id
    ↓
Aggregation / Ranking
```

**This is the Gaps & Islands pattern you should be able to recognize in an interview.**
