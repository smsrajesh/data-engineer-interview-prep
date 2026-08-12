
=============================================================================================

PySpark --- Day 17: DataFrame I

Goal :

    Learn the core PySpark DataFrame operations used in day-to-day DataEngineering and interviews:

    Read → Select → Filter → Transform → Cast → Conditional Logic → Write

=============================================================================================

## 1. What is a PySpark DataFrame?

A PySpark DataFrame is a distributed collection of data organized intonamed columns.

Conceptually, it is similar to a table in SQL, but it is designed fordistributed processing using Spark.

Example:

+---+----+---+------+----------+
| id|name|age|salary|department|
+---+----+---+------+----------+
|  1| Raj| 28| 60000|        IT|
|  2|Ravi| 32| 45000|        HR|
|  3|John| 25| 75000|        IT|
+---+----+---+------+----------+

## 2. SparkSession :

SparkSession is the entry point for working with Spark DataFrames andSpark SQL.

    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("Day-17") \
        .getOrCreate()

Interview answer :

SparkSession is the entry point for working with Spark functionality,including DataFrames and Spark SQL. It provides access to the Sparkexecution environment and allows us to read, process, and write data.

## 3. Reading Data

### 3.1 Read CSV

    df = spark.read.csv(
        "employees.csv",
        header=True,
        inferSchema=True
    )

header=True

    Treats the first row as column names.

inferSchema=True

    Asks Spark to infer the datatypes of the columns.

Example:

    id          → integer
    name        → string
    age         → integer
    salary      → integer
    department  → string

Production interview point :

inferSchema=True is convenient during development, but productionpipelines often use an explicit schema for predictable datatypes andschema control.

### 3.2 Inspect the DataFrame

Show data :

    df.show()

Show schema :

    df.printSchema()

Basic statistics :

    df.describe().show()

Remember:

    show()         → data
    printSchema()  → structure + datatypes
    describe()     → basic statistics

## 4. Read JSON :

    df = spark.read.json("employees.json")

    For multiline JSON:

    df = spark.read \
        .option("multiLine", True) \
        .json("employees.json")

## 5. Read Parquet :

df = spark.read.parquet("employees.parquet")

Parquet is very important in Data Engineering because it is:

    *    Columnar

    *   Compressed

    *   Schema-aware

    *   Efficient for analytical workloads

    *   Well suited for Spark

Why Parquet instead of CSV?

Parquet supports efficient analytical processing, including columnpruning and predicate pushdown, and is generally much better suited fordata lake workloads than CSV.

## 6. DataFrame Immutability :

PySpark DataFrames are immutable.

This:

    df.select("name", "salary")

    does not permanently modify df.

    Instead, it returns a new DataFrame.

    df2 = df.select("name", "salary")

    Or:

    df = df.select("name", "salary")

This concept is important when chaining transformations.

## 7. select()

select() is used to choose columns or column expressions for theoutput DataFrame.

    df.select("name", "salary")

Using col():

    from pyspark.sql.functions import col

    df.select(
        col("name"),
        col("salary")
    )   

With expressions :

    df.select(
        "name",
        "salary",
        (col("salary") * 12).alias("annual_salary")
    )

Remember :

    select() → Which COLUMNS do I want?
    filter() → Which ROWS do I want?

## 8. filter() :

filter() is used to restrict rows based on a condition.

    df.filter(
        col("salary") > 50000
    )

where() can also be used:

    df.where(
        col("salary") > 50000
    )

filter() and where() are commonly interchangeable.

Multiple conditions:

AND:

    df.filter(
        (col("salary") > 50000) &
        (col("age") > 25)
    )

OR:

    df.filter(
        (col("salary") > 50000) |
        (col("age") > 30)
    )

NOT:

    df.filter(
        ~(col("department") == "HR")
    )

Important syntax

Use:

    AND → &
    OR  → |
    NOT → ~

Put individual conditions inside parentheses.

Do not use Python's ( and / or ) for Spark Column expressions.

## 9. withColumn() :

withColumn() is used to:

    *    Create a new column

    *    Replace an existing column

    *    Transform an existing column

Create a new column :

    df = df.withColumn(
        "annual_salary",
        col("salary") * 12
    )

Replace/transform an existing column :

    df = df.withColumn(
        "salary",
        col("salary") * 1.10
    )

The existing salary column is replaced by the transformed expression.

Common pattern :

df.withColumn(
    "column_name",
    expression
)

## 10. Rename a Column :

Use withColumnRenamed():

    df = df.withColumnRenamed(
        "name",
        "employee_name"
    )

Multiple columns can be renamed by chaining:

    df = df.withColumnRenamed(
        "name",
        "employee_name"
    ).withColumnRenamed(
        "salary",
        "monthly_salary"
    )

## 11. Drop a Column :

        df = df.drop("age")

    Multiple columns:

        df = df.drop(
            "age",
            "department"
        )

## 12. cast() :

cast() explicitly converts a column from one datatype to another.

Example:

    df = df.withColumn(
        "salary",
        col("salary").cast("integer")
    )

Common casts:

    .cast("integer")
    .cast("long")
    .cast("double")
    .cast("float")
    .cast("string")
    .cast("date")
    .cast("timestamp")

Interview answer :

    cast() is used to explicitly convert a DataFrame column from onedatatype to another.

## 13. String → Date :

For a string such as:

11-08-2026

use to_date() when the source format is known.

from pyspark.sql.functions import to_date

df = df.withColumn(
    "hire_date",
    to_date(col("hire_date"), "dd-MM-yyyy")
)

Other formats:

to_date(col("hire_date"), "yyyy-MM-dd")

to_date(col("hire_date"), "yyyy/MM/dd")


cast("date") vs to_date() :

Simple conversion:

    col("hire_date").cast("date")

Parsing a string with a known format:

    to_date(col("hire_date"), "dd-MM-yyyy")

    When the input has a specific date format, to_date() is more explicit.

## 14. when() and otherwise() :

These implement conditional logic similar to SQL CASE WHEN.

SQL:

    CASE
        WHEN salary >= 50000 THEN 'High'
        ELSE 'Low'
    END

PySpark:

    df = df.withColumn(
        "salary_category",
        when(col("salary") >= 50000, "High")
        .otherwise("Low")
    )

Multiple conditions :

    df = df.withColumn(
        "salary_category",
        when(col("salary") >= 80000, "High")
        .when(col("salary") >= 50000, "Medium")
        .otherwise("Low")
    )

Important :

    The order of conditions matters.

    Spark evaluates the conditions in order.

Interview answer :

when() defines a condition and the value to return when it is true.otherwise() provides the default value when none of the when()conditions are satisfied.

## 15. NULL Handling :

### fillna()

    Replace NULL salary values with zero:

    df = df.fillna({
        "salary": 0
    })

    Multiple columns:

        df = df.fillna({
            "salary": 0,
            "age": 0,
            "department": "Unknown"
        })

You can also use:

    df = df.fillna(0)

    but column-specific replacement is usually clearer.

### coalesce()

    coalesce() returns the first non-null value.

    from pyspark.sql.functions import coalesce, lit

    df = df.withColumn(
        "salary",
        coalesce(col("salary"), lit(0))
    )



Conceptually:

salary exists?
   │
 Yes → salary
   │
  No
   ↓
   0

NULL checks

### Use:

    col("salary").isNull()

    and:

    col("salary").isNotNull()

### Do not use:

    col("salary") == None

    for Spark NULL checks.

## 16. Writing Data

### Write CSV :

    df.write \
        .mode("overwrite") \
        .option("header", True) \
        .csv("output/employees")

### Write Parquet :

    df.write \
        .mode("overwrite") \
        .parquet("output/employees")

Generic DataFrameWriter API:

    df.write \
        .mode("overwrite") \
        .format("parquet") \
        .save("output/employees")

These two Parquet approaches are essentially equivalent.

    df.write.parquet(...)

        -- is a format-specific convenience method.

    df.write.format("parquet").save(...)

        -- uses the generic DataFrameWriter API.

## 17. Write Modes :

### Overwrite

    .mode("overwrite")

    Replace existing output.

### Append

    .mode("append")

    Add new data to existing output.

    Important: append does not automatically deduplicate or upsert data.

### Ignore

    .mode("ignore")

    Do nothing if the destination already exists.

### Error

    .mode("error")

    or:

    .mode("errorifexists")

    Fail if the destination already exists.

## 18. Why Does Spark Create Multiple Output Files?

Spark processes data in parallel across partitions.

When a DataFrame is written, each partition can write its data independently.

Therefore Spark generally produces multiple output files.

Conceptually:

    DataFrame
        │
        ├── Partition 1 → part-00000
        ├── Partition 2 → part-00001
        ├── Partition 3 → part-00002
        └── Partition 4 → part-00003

This is a direct consequence of Spark's distributed processing model.

## 19. Complete Day 17 Pipeline

Example:

    from pyspark.sql import SparkSession
    from pyspark.sql.functions import to_date, col, when

    spark = SparkSession.builder \
        .appName("Day-17") \
        .getOrCreate()

### Read CSV
    df = spark.read.csv(
        "employees.csv",
        header=True,
        inferSchema=True
    )

### Convert string date → date
    cleaned_df = df.withColumn(
        "hire_date",
        to_date(col("hire_date"), "dd-MM-yyyy")
    )

### Create annual salary
    trans_1_df = cleaned_df.withColumn(
        "annual_salary",
        col("salary") * 12
    )

### Create salary category
    trans_2_df = trans_1_df.withColumn(
        "salary_category",
        when(col("salary") >= 80000, "High")
        .when(col("salary") >= 50000, "Medium")
        .otherwise("Low")
    )

### Filter employees
    filter_df = trans_2_df.filter(
        col("salary") > 50000
    )

### Select required columns
    result_df = filter_df.select(
        "id",
        "name",
        "hire_date",
        "salary",
        "annual_salary",
        "salary_category"
    )

### Write as Parquet
    result_df.write \
        .mode("overwrite") \
        .parquet("output/employees")


## 20. Day 17 Interview Cheat Sheet

Concept                Syntax

Read CSV               spark.read.csv()
Read JSON              spark.read.json()
Read Parquet           spark.read.parquet()
Inspect data           df.show()
Inspect schema         df.printSchema()
Select columns         df.select()
Filter rows            df.filter()
Add/transform column   df.withColumn()
Rename                 df.withColumnRenamed()
Drop                   df.drop()
Cast                   col().cast()
Conditional logic      when().otherwise()
Replace NULL           fillna()
Parse date             to_date()
Write CSV              df.write.csv()
Write Parquet          df.write.parquet()

## 21. Day 17 Practice Exercises

1. Filter employees with salary > 50K.
2. Convert string date to date.
3. Create salary category.
4. Replace NULL values.
5. Rename columns.
6. Create derived column.
7. Filter multiple conditions.
8. Convert string → integer.
9. Create age group.
10. Write transformed data to Parquet.

## 22. Key Interview Mental Model

Think of a basic PySpark ETL pipeline as:

                DATA SOURCE
                    │
              spark.read
                    │
                    ▼
               DataFrame
                    │
          ┌─────────┴─────────┐
          │                   │
       select()            filter()
          │                   │
          └─────────┬─────────┘
                    ▼
              withColumn()
                    │
          ┌─────────┴─────────┐
          │                   │
        cast()         when/otherwise()
          │                   │
          └─────────┬─────────┘
                    ▼
             Transformed DF
                    │
                df.write
                    │
             ┌──────┴──────┐
             ▼             ▼
           CSV          Parquet