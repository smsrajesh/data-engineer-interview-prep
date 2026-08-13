Day 18 --- DataFrame --- Aggregation :

Overview:

    Aggregation is used to summarize DataFrame data using functions such as:

    count()

    countDistinct()

    sum()

    avg()

    min()

    max()

    The main PySpark pattern is:

        df.groupBy("column").agg(...)

### 1. groupBy() :

Definition:

    groupBy() groups DataFrame rows based on one or more columns so thataggregation can be performed for each group.

    df.groupBy("department").count()

Example:

    department | salary
    -----------|-------
    IT         | 60000
    IT         | 70000
    HR         | 50000
    HR         | 55000

    df.groupBy("department").count()

Result:

    department | count
    -----------|------
    IT         | 2
    HR         | 2

What does groupBy() return?

    groupBy() returns a GroupedData object, not an aggregated DataFrame.

    grouped_df = df.groupBy("department")

    Then an aggregation can be applied:

    grouped_df.count()

Mental model:

    DataFrame
        ↓
    groupBy()
        ↓
    GroupedData
        ↓
    Aggregation
        ↓
    DataFrame

Grouping by multiple columns:

    df.groupBy("department", "location").count()

    The grouping key is the combination of both columns.

Why can groupBy() cause a shuffle?

    Records with the same grouping key may exist in different partitions.

    Spark may therefore need to redistribute the data so that records withthe same key can be processed together.

        Partition 1 → IT, HR
        Partition 2 → Sales, IT
        Partition 3 → HR, Sales

                    ↓
                SHUFFLE
                    ↓

        IT    → all IT records
        HR    → all HR records
        Sales → all Sales records

Why is shuffle expensive?

Shuffle can involve:

    Network I/O

    Disk I/O

    Serialization/deserialization

    Data movement between executors

    Additional computation

Therefore, grouped aggregations can become expensive on large datasets.

Interview-ready answer:

    "groupBy() is used to group DataFrame records based on one or morecolumns and then perform aggregations such as count, sum, average,minimum, or maximum. It returns a GroupedData object, and groupedaggregation may require a shuffle because the same grouping key canexist across different partitions."

### 2. count() vs countDistinct() :

count():

    count() can count the total number of rows in a DataFrame or the number of non-null values in a specific column.

Count rows:

    df.count()

Count non-null column values:

    from pyspark.sql.functions import count

    df.select(count("department"))

countDistinct():

    countDistinct() returns the number of unique non-null values in acolumn.

    from pyspark.sql.functions import countDistinct

    df.select(countDistinct("department"))

Example:

    department
    -----------
    IT
    IT
    HR
    NULL
    NULL

Results:

    df.count()                      → 5
    count("department")             → 3
    countDistinct("department")     → 2

Mental model:

    df.count()
        ↓
    How many rows?


    count("column")
        ↓
    How many non-null values?


    countDistinct("column")
        ↓
    How many unique non-null values?

Cardinality:

    Cardinality means the number of distinct values in a column ordataset.

Example:

    customer_id
    -----------
    C1
    C2
    C1
    C3
    C2

    There are 5 rows but only 3 distinct values:

    C1
    C2
    C3

Therefore:

    Cardinality = 3

High Cardinality:

    A high-cardinality column contains a large number of distinctvalues.

Examples:

    transaction_id
    customer_id
    email

High-cardinality columns can make operations such as:

    countDistinct("transaction_id")

    more computationally expensive.

Low Cardinality:

    A low-cardinality column contains relatively few distinct values.

Example:

    status
    ------
    SUCCESS
    FAILED
    PENDING
    SUCCESS

Distinct values:

    SUCCESS
    FAILED
    PENDING

Cardinality:

    3

Why can countDistinct() be expensive?

countDistinct() must identify unique values, which requires morecomputation and may involve data redistribution/shuffle for large orhigh-cardinality datasets.

approx_count_distinct():

    approx_count_distinct() returns an approximate number of distinctvalues.

        from pyspark.sql.functions import approx_count_distinct

        df.select(
            approx_count_distinct("customer_id")
        )

Use it when:

    The dataset is very large.

    An approximate answer is acceptable.

    Better scalability is more important than exactness.

Interview-ready answer:

    "count() can count rows or non-null values depending on how it isused, whereas countDistinct() returns the number of unique non-nullvalues. countDistinct() generally requires more computation than asimple count and can be expensive for large high-cardinalitydatasets."

### 3. sum() :

Definition:

    sum() is an aggregation function used to calculate the total of anumeric column.

    from pyspark.sql.functions import sum

    df.select(
        sum("salary").alias("total_salary")
    )

    With groupBy():

        df.groupBy("department").agg(
            sum("salary").alias("total_salary")
        )

        This calculates the total salary for each department.

NULL handling:

sum() ignores NULL values.

Example:

    salary
    ------
    60000
    70000
    NULL
    50000

Result:

    180000

If all values are NULL, the result is NULL.

If the business requires zero instead of NULL:

    from pyspark.sql.functions import coalesce, lit, sum

    df.select(
        coalesce(sum("salary"), lit(0)).alias("total_salary")
    )

Partial Aggregation :

Definition:

    Partial aggregation means Spark performs aggregation locally within each partition before combining the intermediate results globally.

Suppose:

    id | department | salary
    ---|------------|-------
    1  | IT         | 60000
    2  | IT         | 70000
    3  | HR         | 50000
    4  | IT         | 80000
    5  | HR         | 55000
    6  | HR         | 65000

Assume Spark distributes the data across three partitions:

    Partition 1
    ------------
    IT → 60000
    IT → 70000

    Partition 2
    ------------
    HR → 50000
    IT → 80000

    Partition 3
    ------------
    HR → 55000
    HR → 65000

Step 1 --- Local aggregation:

Spark can first calculate partial results inside each partition:

Partition 1:
    IT → 60000 + 70000 = 130000

Partition 2:
    HR → 50000
    IT → 80000

Partition 3:
    HR → 55000 + 65000 = 120000

Intermediate results:

    IT → 130000
    IT → 80000

    HR → 50000
    HR → 120000

Step 2 --- Shuffle:

    Spark redistributes the intermediate results so records with the samegrouping key can be combined.

    IT → 130000
    IT → 80000

    HR → 50000
    HR → 120000

Step 3 --- Final aggregation:

    IT:
    130000 + 80000 = 210000

    HR:
    50000 + 120000 = 170000

Final result:

    department | total_salary
    -----------|-------------
    IT         | 210000
    HR         | 170000

Why is partial aggregation useful?

    With a very large dataset, local aggregation can reduce the amount of intermediate data that needs to be transferred during the shuffle.

    Large dataset
        ↓
    Local / partial aggregation
        ↓
    Smaller intermediate data
        ↓
    Shuffle
        ↓
    Final aggregation

Important interview point :

    Partial aggregation does not eliminate shuffle.
    It can reduce the amount of data that needs to be shuffled.

Interview-ready answer :

    "Partial aggregation means Spark performs aggregation locally withineach partition before shuffling the intermediate results. This reducesthe amount of data that needs to be transferred across the network andcan improve aggregation performance."

sum() and shuffle :

    sum() itself can be calculated using partial aggregation.

However:

    df.groupBy("department").agg(
        sum("salary")
    )

    may require a shuffle because of the groupBy().

Interview-ready answer :

    "sum() is an aggregation function used to calculate the total of anumeric column. It can be applied to the entire DataFrame or combinedwith groupBy() to calculate totals for each group. NULL values areignored, and if all values are NULL, the result is NULL."

### 4. avg() :

Definition :

    avg() is an aggregation function used to calculate the average of anumeric column.

Conceptually:

    Average = Sum of valid values / Count of valid values

    from pyspark.sql.functions import avg

    df.select(
        avg("salary").alias("avg_salary")
    )

    With groupBy() :

        df.groupBy("department").agg(
            avg("salary").alias("avg_salary")
        )

        This calculates the average separately for each group.

NULL handling :

    avg() ignores NULL values in both the sum and count.

Example :

    100
    200
    NULL

Average :

    (100 + 200) / 2 = 150

    If all values are NULL, the result is NULL.

Distributed average :

    Spark can calculate averages efficiently across partitions by maintaining partial sums and counts.

    Partition 1 → partial sum + count
    Partition 2 → partial sum + count
    Partition 3 → partial sum + count
                        ↓
                    Combine
                        ↓
                total sum/count
                        ↓
                    average

Why can't we simply average the averages?

    Because partitions or groups may contain different numbers of records.

Example:

    Partition 1:
    10, 20
    Average = 15

    Partition 2:
    30, 40, 50, 60
    Average = 45

Incorrect:

    (15 + 45) / 2 = 30

Correct:

    (10 + 20 + 30 + 40 + 50 + 60) / 6 = 35

    Spark therefore combines partial sums and counts instead of simplyaveraging partition averages.

avg() vs mean() :

    avg() and mean() are equivalent aggregation functions in PySpark.

    df.select(avg("salary"))
    df.select(mean("salary"))

Interview-ready answer :

    "avg() is an aggregation function used to calculate the average of anumeric column. It can be applied to the entire DataFrame or combinedwith groupBy() to calculate averages for individual groups. NULLvalues are ignored. Spark can perform partial aggregation bymaintaining sums and counts across partitions and then combine them tocalculate the final average."

### 5. min() :

Definition :

    min() is an aggregation function that returns the smallest non-nullvalue from a column.

    from pyspark.sql.functions import min

    df.select(
        min("salary").alias("min_salary")
    )

    With groupBy() :

        df.groupBy("department").agg(
            min("salary").alias("min_salary")
        )

        This returns the minimum salary for each department.

NULL handling :

    min() ignores NULL values.

    If all values are NULL, the result is NULL.

Dates and timestamps :

    min() can be used with dates and timestamps.

    df.select(
        min("order_date").alias("first_order_date")
    )

For dates/timestamps :

    min(date) → earliest date
    min(timestamp) → earliest timestamp

Distributed execution :

    Spark can calculate local minimums and combine them.

    Partition 1 → min = 20
    Partition 2 → min = 30
    Partition 3 → min = 10

                ↓

    min(20, 30, 10)

                ↓

                10

min() vs least() :

    min()
        ↓
    Across rows of a column


    least()
        ↓
    Across columns within a row

Example:

    salary | bonus | commission
    -------|-------|-----------
    60000  | 5000  | 3000

    least("salary", "bonus", "commission")

    returns 3000.

Interview-ready answer :

    "min() is an aggregation function used to find the minimum value ofa column. It can be applied to the entire DataFrame or combined withgroupBy() to find the minimum value within each group. NULL valuesare ignored, and if all values are NULL, the result is NULL. It canalso be used with dates and timestamps to find the earliest value."

### 6. max()

    max() is the counterpart of min() and returns the largest non-nullvalue.

    from pyspark.sql.functions import max

    df.select(
        max("salary").alias("max_salary")
    )

    With groupBy() :

        df.groupBy("department").agg(
            max("salary").alias("max_salary")
        )

NULL handling :

    100
    200
    NULL
    300

    max() → 300

If all values are NULL:

    NULL
    NULL
    NULL

    max() → NULL

Dates and timestamps :

    max(date) → latest date
    max(timestamp) → latest timestamp

max() vs greatest() :

    max()
        ↓
    Across rows of a column


    greatest()
        ↓
    Across columns within a row

Example:

    salary | bonus | commission
    -------|-------|-----------
    60000  | 5000  | 3000

    greatest("salary", "bonus", "commission")

    returns 60000.

Interview-ready answer :

    "max() is an aggregation function used to find the largest value ina column. It can be applied to the entire DataFrame or combined withgroupBy() to find the maximum value for each group. NULL values areignored, and if all values are NULL, the result is NULL. For dates andtimestamps, it returns the latest value."

### 7. Multiple Aggregations

What is agg()?

    agg() allows multiple aggregation expressions to be calculatedtogether.

    from pyspark.sql.functions import (
        count,
        countDistinct,
        sum,
        avg,
        min,
        max
    )

    df.groupBy("department").agg(
        count("*").alias("employee_count"),
        countDistinct("employee_id").alias("unique_employees"),
        sum("salary").alias("total_salary"),
        avg("salary").alias("avg_salary"),
        min("salary").alias("min_salary"),
        max("salary").alias("max_salary")
    )

df.agg() vs df.groupBy().agg() :

    Entire DataFrame :

        df.agg(
            count("*").alias("employee_count"),
            sum("salary").alias("total_salary"),
            avg("salary").alias("avg_salary"),
            min("salary").alias("min_salary"),
            max("salary").alias("max_salary")
        )

        This produces aggregate metrics for the entire DataFrame.

    Per group :

        df.groupBy("department").agg(
            count("*").alias("employee_count"),
            sum("salary").alias("total_salary"),
            avg("salary").alias("avg_salary"),
            min("salary").alias("min_salary"),
            max("salary").alias("max_salary")
        )

        This produces the metrics separately for each department.

Mental model:

    df.agg(...)
        ↓
    Entire DataFrame
        ↓
    Aggregate result


    df.groupBy("department").agg(...)
        ↓
    Each department
        ↓
    One result per group


count("*") vs count("column") :

    count("*")

        counts rows, including rows where a column contains NULL.

    count("salary")

        counts only non-null salary values.

Example:

    employee_id | salary
    ------------|-------
    1           | 60000
    2           | NULL
    3           | 70000

Results:

    count("*")       → 3
    count("salary")  → 2

    This can also be used as a data-quality check.

Why use one groupBy().agg()?

    Instead of repeatedly doing:

        df.groupBy("department").sum("salary")
        df.groupBy("department").avg("salary")
        df.groupBy("department").min("salary")
        df.groupBy("department").max("salary")

    prefer:

        df.groupBy("department").agg(
            sum("salary").alias("total_salary"),
            avg("salary").alias("avg_salary"),
            min("salary").alias("min_salary"),
            max("salary").alias("max_salary")
        )

    This is cleaner and gives Spark a better opportunity to execute compatible grouped aggregations together rather than repeatedly performing separate grouped operations.

Real-world example :

    Daily sales metrics:

        daily_sales = df.groupBy("transaction_date").agg(
            count("*").alias("transaction_count"),
            countDistinct("customer_id").alias("unique_customers"),
            sum("amount").alias("total_revenue"),
            avg("amount").alias("avg_transaction"),
            min("amount").alias("min_transaction"),
            max("amount").alias("max_transaction")
        )

        This can produce an analytics-ready daily summary.

Interview-ready answer :

    "agg() allows us to calculate multiple aggregation metrics together.df.agg() calculates aggregate metrics across the entire DataFrame,while df.groupBy().agg() calculates them separately for each group.Using a single grouped aggregation is generally preferable torepeatedly running separate grouped aggregations because it producescleaner code and gives Spark better opportunities to optimize theexecution."

### 8. Spark Vocabulary :

This section provides quick definitions for important terms usedthroughout aggregation.

Partition :

    A partition is a logical chunk of data distributed across a Spark cluster.

    1 TB Data
    ↓
    Partition 1
    Partition 2
    Partition 3
    ...
    Partition N

    Spark processes partitions in parallel.

Task :

    A task is a unit of work that Spark sends to an executor to processa partition.

    Partition 1 → Task 1
    Partition 2 → Task 2
    Partition 3 → Task 3

Executor :

    An executor is a Spark process running on a worker node thatexecutes tasks and processes data.

Simplified architecture:

             Driver
                |
       -------------------
       |        |        |
   Executor  Executor  Executor
       |        |        |
    Tasks     Tasks     Tasks

Aggregation :

    Aggregation means combining multiple records to produce a summaryvalue.

Common aggregation functions:

    count()
    sum()
    avg()
    min()
    max()

Partial Aggregation :

    Partial aggregation means Spark performs aggregation locally withineach partition before combining the intermediate results globally.

    Partition 1 → partial result
    Partition 2 → partial result
    Partition 3 → partial result
                        ↓
                    Combine
                        ↓
                Final result

Shuffle :

    A shuffle is the redistribution of data across partitions so thatrelated records can be processed together.

For example:

    IT records    → together
    HR records    → together
    Sales records → together

Shuffle can involve:

    Network I/O

    Disk I/O

    Serialization/deserialization

    Data movement between executors

    Additional computation

Cardinality :

    Cardinality is the number of distinct values in a column or dataset.

Example:

    customer_id
    -----------
    C1
    C2
    C1
    C3
    C2

    Cardinality = 3.

High Cardinality :

    A column with a large number of distinct values.

Examples:

    transaction_id
    customer_id
    email

Low Cardinality :

    A column with relatively few distinct values.

Examples:

    status
    country
    category

### 9. Aggregation Interview Cheat Sheet

Function            Purpose                         NULL behavior

groupBy()         Defines groups                  Depends on aggregation
count("*")        Counts rows                     Counts rows
count("column")   Counts non-null values          Ignores NULL
countDistinct()   Counts unique non-null values   Ignores NULL
sum()             Calculates total                Ignores NULL
avg()             Calculates average              Ignores NULL
min()             Finds minimum                   Ignores NULL
max()             Finds maximum                   Ignores NULL

Note :
    If all values supplied to sum(), avg(), min(), or max() are NULL, the aggregate result is NULL.

### 10. Important Spark Relationships

Partition
    ↓
Data is divided into chunks


Task
    ↓
Processes a partition


Executor
    ↓
Runs tasks


groupBy()
    ↓
May require shuffle


Partial aggregation
    ↓
Reduces intermediate data


Shuffle
    ↓
Redistributes data


Final aggregation
    ↓
Produces final result


Important distinction :

    Partial aggregation reduces data movement; it does not eliminate the shuffle required by a grouped operation.

### 11. Most Important Patterns to Remember

Global aggregation:

    df.agg(
        sum("amount").alias("total_amount"),
        avg("amount").alias("avg_amount")
    )

Grouped aggregation :

    df.groupBy("department").agg(
        sum("salary").alias("total_salary"),
        avg("salary").alias("avg_salary")
    )

Multiple metrics :

    df.groupBy("department").agg(
        count("*").alias("row_count"),
        countDistinct("employee_id").alias("unique_employees"),
        sum("salary").alias("total_salary"),
        avg("salary").alias("avg_salary"),
        min("salary").alias("min_salary"),
        max("salary").alias("max_salary")
    )


### Final Mental Model :

                    DataFrame
                       │
          ┌────────────┴────────────┐
          │                         │
      df.agg()              groupBy().agg()
          │                         │
   Entire DataFrame             Each group
          │                         │
   Aggregate metrics        Potential shuffle
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                  count            sum             avg
                    │               │               │
              countDistinct       min             max
                    │
              NULL awareness
                    │
             Partial aggregation
                    │
              Final result