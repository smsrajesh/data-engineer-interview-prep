PySpark --- Day 18: DataFrame_Aggregations --- Solutions

12. Interview Questions --- Solutions

1. What is groupBy() in PySpark?

Answer :

    groupBy() is used to group rows based on one or more columns so thatwe can perform aggregate operations such as sum(), count(), avg(),min(), and max().

    Example:

        df.groupBy("department").sum("salary")

        This calculates the total salary for each department.

2. What does groupBy() return?

Answer :

    groupBy() returns a GroupedData object, not a DataFrame.

    Example:

        grouped_df = df.groupBy("department")

        At this point, Spark has created a grouped representation. We normallyapply an aggregation afterward:

        result_df = df.groupBy("department").sum("salary")

3. Why can groupBy() cause a shuffle?

Answer :

    groupBy() can cause a shuffle because rows belonging to the same groupmay be located in different partitions.

    Spark must redistribute the rows so that records with the same groupingkey are brought together.

    Conceptually:

        Partition 1 → IT, HR
        Partition 2 → IT, Finance
        Partition 3 → HR, IT

                    ↓ Shuffle

        IT      → one target partition
        HR      → one target partition
        Finance → one target partition

    This redistribution of data across partitions is called a shuffle.

4. Why is shuffle expensive?

Answer :

    Shuffle is expensive because Spark may need to:

        Move data across executors.

        Perform network I/O.

        Serialize and deserialize data.

        Write intermediate data to disk when necessary.

        Perform additional processing to redistribute the data.

    Therefore, shuffle can increase execution time and resource usage.

Interview answer :

    Shuffle is expensive because it involves redistributing data acrosspartitions, which can require network transfer, serialization, diskI/O, and additional computation.

5. What is a partition?

Answer :

    A partition is a logical chunk of data within a distributed SparkDataFrame or RDD.

    Spark processes partitions in parallel across executors.

    Conceptually:

        DataFrame
            │
            ├── Partition 1
            ├── Partition 2
            ├── Partition 3
            └── Partition 4

    More partitions allow more parallelism, but too many or too fewpartitions can negatively affect performance.

6. What is partial aggregation?

Answer :

    Partial aggregation means Spark performs aggregation locally within eachpartition before sending the aggregated results across the network.

Example:

    Suppose we want:

    df.groupBy("department").sum("salary")

    Instead of immediately sending every salary value across the network,Spark can first calculate partial sums within each partition.

    Partition 1
        IT → 100K
        HR → 50K

    Partition 2
        IT → 80K
        HR → 70K

            ↓ Shuffle only partial results

        IT → 100K + 80K = 180K
        HR → 50K + 70K = 120K

7. How does partial aggregation reduce shuffle cost?

Answer :

    Partial aggregation reduces shuffle cost by reducing the amount of datathat needs to be transferred across the network.

    Instead of shuffling every individual row:

        1000 rows → shuffle

    Spark may first combine values locally:

        1000 rows
        ↓
        local aggregation
        ↓
        20 partial results
        ↓
        shuffle

    Therefore, less data needs to be transferred between executors.

Interview answer :

    Partial aggregation reduces shuffle volume by combining recordslocally within each partition before the data is redistributed acrossthe network.

8. What is the difference between df.count() and count("column")?

Answer :

    df.count() counts the total number of rows in the DataFrame.

        df.count()

    count("column") counts the number of non-NULL values in that specificcolumn.

        from pyspark.sql.functions import count

        df.select(
            count("salary")
        ).show()

Example:

    id | salary
    ---|-------
    1  | 50000
    2  | NULL
    3  | 70000

Then:

    df.count()          → 3
    count("salary")     → 2

9. What is the difference between count() and countDistinct()?

Answer :

    count() counts rows or non-NULL values depending on how it is used.

        df.count()

    or:

        from pyspark.sql.functions import count

        df.select(
            count("department")
        ).show()

    countDistinct() counts the number of unique non-NULL values.

        from pyspark.sql.functions import countDistinct

        df.select(
            countDistinct("department")
        ).show()

Example:

    department
    ----------
    IT
    IT
    HR
    Finance
    HR

Then:

    count("department")             → 5
    countDistinct("department")     → 3

10. What is cardinality?

Answer :

    Cardinality refers to the number of distinct values in a column ordataset.

Example:

    department
    ----------
    IT
    IT
    HR
    Finance
    HR

    The distinct values are:

        IT
        HR
        Finance

    Therefore, the cardinality is:

        3

    A column such as department usually has lower cardinality, while acolumn such as customer_id may have very high cardinality.

11. Why can countDistinct() be expensive for high-cardinality columns?

Answer :

    countDistinct() needs to determine the unique values.

    For a high-cardinality column, Spark may need to process and maintain avery large set of distinct values and perform significant distributedaggregation and shuffle work.

For example:

    customer_id
    -----------
    1000001
    1000002
    1000003
    ...

If most values are unique, the number of distinct values is very large.

This can increase:

    Memory usage

    Shuffle volume

    Network I/O

    Processing time

12. What is approx_count_distinct()?

Answer :

    approx_count_distinct() provides an approximate count of distinctvalues instead of calculating the exact count.

    from pyspark.sql.functions import approx_count_distinct

    df.select(
        approx_count_distinct("customer_id")
    ).show()

It is useful when:

    The column has high cardinality.

    An approximate result is acceptable.

    Performance is more important than exact precision.

Conceptually:

    countDistinct()
        → exact result
        → potentially more expensive

    approx_count_distinct()
        → approximate result
        → generally more efficient

13. How does sum() handle NULL values?

Answer :

    sum() ignores NULL values when calculating the sum.

Example:

    salary
    ------
    50000
    NULL
    70000

    Then:

        from pyspark.sql.functions import sum

        df.select(
            sum("salary")
        ).show()

    The result is:

        120000

    The NULL value is not treated as zero during the aggregation; it isignored.

14. How does avg() handle NULL values?

Answer :

    avg() ignores NULL values when calculating the average.

Example:

    salary
    ------
    50000
    NULL
    70000

    The average is:

        = (50000 + 70000) / 2
        = 60000

    The NULL value is not included in the count used for the average.

15. Why can't we simply average partition averages?

Answer :

    Because partitions may contain different numbers of valid records.

Example:

    Partition 1:
    values → 10, 20
    average → 15

    Partition 2:
    values → 30, 40, 50, 60
    average → 45

    Simply averaging the partition averages gives:

        = (15 + 45) / 2 = 30

    But the correct global average is:

        = (10 + 20 + 30 + 40 + 50 + 60) / 6
        = 35

    The partition averages must therefore be weighted according to thenumber of records contributing to each average.

16. How can Spark calculate an average in a distributed environment?

Answer :

    Spark can calculate an average using two pieces of information from each partition:

    sum
    count

Each partition can calculate:

    Partition 1 → sum = 30,  count = 2
    Partition 2 → sum = 180, count = 4

Then Spark combines them:

    Total sum   = 30 + 180 = 210
    Total count = 2 + 4 = 6

Average = 210 / 6 = 35

This allows average calculation to work correctly in a distributedenvironment.

Key idea :

    Global average = total sum / total count

    not:

    average of partition averages

17. What is the difference between min() and least()?

Answer :

    min() is an aggregation function. It finds the minimum value acrossmultiple rows.

Example:

    from pyspark.sql.functions import min

    df.select(
        min("salary")
    ).show()

    least() is a row-level function. It finds the smallest value amongmultiple columns within the same row.

Example:

    from pyspark.sql.functions import least

    df.select(
        least("salary", "bonus").alias("minimum_amount")
    ).show()

Conceptually:

    min()
    → across rows

    least()
    → across columns in one row

18. What is the difference between max() and greatest()?

Answer :

    max() is an aggregation function. It finds the maximum value acrossmultiple rows.

        from pyspark.sql.functions import max

        df.select(
            max("salary")
        ).show()

    greatest() is a row-level function. It finds the largest value amongmultiple columns within the same row.

        from pyspark.sql.functions import greatest

        df.select(
            greatest("salary", "bonus").alias("maximum_amount")
        ).show()

Conceptually:

    max()
        → across rows

    greatest()
        → across columns in one row

19. What is agg()?

Answer :

    agg() is used to perform one or more aggregate functions on aDataFrame or grouped DataFrame.

Example:

    from pyspark.sql.functions import sum, avg, max

    df.agg(
        sum("salary").alias("total_salary"),
        avg("salary").alias("average_salary"),
        max("salary").alias("maximum_salary")
    ).show()

    This produces aggregate results for the entire DataFrame.

20. What is the difference between df.agg() and df.groupBy().agg()?

Answer :

    df.agg() performs aggregation over the entire DataFrame.

    df.agg(
        sum("salary").alias("total_salary")
    ).show()

    Conceptually:

        Entire DataFrame
            ↓
        One overall aggregate result

    df.groupBy().agg() first divides the data into groups and thenperforms the aggregation for each group.

        df.groupBy("department").agg(
            sum("salary").alias("total_salary")
        ).show()

        Conceptually:

            DataFrame
                ↓
            Group by department
                ↓
            Aggregate each department

21. Why use aliases for aggregation columns?

Answer :

    Aggregation functions can produce unclear or automatically generatedcolumn names.

For example:

    df.groupBy("department").agg(
        sum("salary")
    )

    Using alias() gives the result a meaningful name:

        df.groupBy("department").agg(
            sum("salary").alias("total_salary")
        )

        This improves:

            Readability

            Downstream transformations

            Data quality checks

            Reporting

            Maintainability

22. Why is one groupBy().agg() generally preferable to multiple separate grouped aggregations?

Answer :

    When multiple aggregations are required for the same grouping key, it isgenerally better to perform them together.

    Instead of:

        df.groupBy("department").sum("salary")

        df.groupBy("department").avg("salary")

        df.groupBy("department").max("salary")

    Use:

        from pyspark.sql.functions import sum, avg, max

        result_df = df.groupBy("department").agg(
            sum("salary").alias("total_salary"),
            avg("salary").alias("average_salary"),
            max("salary").alias("maximum_salary")
        )

    This expresses the required aggregations together and generally givesSpark a better opportunity to optimize the execution plan and avoidunnecessary repeated grouped-processing work.

Interview answer :

    When multiple aggregations use the same grouping key, combining themin a single groupBy().agg() is generally cleaner and can avoidunnecessary repeated grouped-processing and shuffle work.