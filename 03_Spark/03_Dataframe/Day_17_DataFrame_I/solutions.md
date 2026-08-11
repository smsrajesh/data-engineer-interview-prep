PySpark --- Day 17: DataFrame I --- Practice Questions & Answers

21. Day 17 Practice Exercises :

1. Filter employees with salary > 50K

    Question :

    Filter employees whose salary is greater than 50,000.

    Answer :

    from pyspark.sql.functions import col

    result_df = df.filter(
        col("salary") > 50000
    )

    result_df.show()

2. Convert string date to date

    Question :

    Convert the hire_date column from string to date using thedd-MM-yyyy format.

    Answer :

    from pyspark.sql.functions import to_date, col

    result_df = df.withColumn(
        "hire_date",
        to_date(col("hire_date"), "dd-MM-yyyy")
    )

    result_df.printSchema()
    result_df.show()

3. Create salary category

    Question :

    Create a salary_category column using these rules:

    salary >= 80000 → High
    salary >= 50000 → Medium
    otherwise       → Low

    Answer :

    from pyspark.sql.functions import when, col

    result_df = df.withColumn(
        "salary_category",
        when(col("salary") >= 80000, "High")
        .when(col("salary") >= 50000, "Medium")
        .otherwise("Low")
    )

    result_df.show()

    Important :

    The order of the conditions matters because Spark evaluates them fromtop to bottom.

4. Replace NULL values

    Question :

    Replace NULL values in the salary column with 0.

    Answer :

    result_df = df.fillna({
        "salary": 0
    })

    result_df.show()

    Alternative :

    from pyspark.sql.functions import coalesce, col, lit

    result_df = df.withColumn(
        "salary",
        coalesce(col("salary"), lit(0))
    )

    result_df.show()

5. Rename columns

    Question :

    Rename:

    name   → employee_name
    salary → monthly_salary

    Answer :

    result_df = (
        df.withColumnRenamed("name", "employee_name")
        .withColumnRenamed("salary", "monthly_salary")
    )

    result_df.show()

6. Create derived column

    Question :

    Create an annual_salary column using:

    annual_salary = salary * 12

    Answer :

    result_df = df.withColumn(
        "annual_salary",
        col("salary") * 12
    )

    result_df.show()

7. Filter multiple conditions

    Question :

    Filter employees who satisfy both:

    salary > 50000
    age > 25

    Answer :

    result_df = df.filter(
        (col("salary") > 50000) &
        (col("age") > 25)
    )

    result_df.show()

    Important :

    For PySpark Column expressions:

    AND → &
    OR  → |
    NOT → ~

    Put each condition inside parentheses.

8. Convert string → integer

    Question :

    Convert the salary and age columns from string to integer.

    Answer :

    result_df = (
        df.withColumn(
            "salary",
            col("salary").cast("integer")
        )
        .withColumn(
            "age",
            col("age").cast("integer")
        )
    )

    result_df.printSchema()
    result_df.show()

    Remember :

    cast() is used to explicitly convert a column from one datatype to another.

9. Create age group

    Question :

    Create an age_group column using these rules:

    age < 25       → Young
    25 <= age <= 40 → Adult
    age > 40       → Senior

    Answer :

    from pyspark.sql.functions import when, col

    result_df = df.withColumn(
        "age_group",
        when(col("age") < 25, "Young")
        .when(col("age") <= 40, "Adult")
        .otherwise("Senior")
    )

    result_df.show()

    Important :

    The second condition only needs:

    col("age") <= 40

    because employees with age < 25 have already been handled by the first when().

10. Write transformed data to Parquet

    Question :

    Write the transformed DataFrame to Parquet using overwrite mode.

    Answer :

    result_df.write \
        .mode("overwrite") \
        .parquet("output/employees")

    Generic DataFrameWriter API :

    result_df.write \
        .mode("overwrite") \
        .format("parquet") \
        .save("output/employees")

    Both approaches write the DataFrame as Parquet.

### 21.1  Complete Practice Pipeline

The exercises above can be combined into a single DataFrametransformation pipeline.

    from pyspark.sql import SparkSession
    from pyspark.sql.functions import (
        col,
        to_date,
        when
    )

    spark = SparkSession.builder \
        .appName("Day-17") \
        .getOrCreate()

    # Read CSV

    df = spark.read.csv(
        "employees.csv",
        header=True,
        inferSchema=True
    )

    # Convert string date → date

    df = df.withColumn(
        "hire_date",
        to_date(col("hire_date"), "dd-MM-yyyy")
    )

    # Create annual salary

    df = df.withColumn(
        "annual_salary",
        col("salary") * 12
    )

    # Create salary category

    df = df.withColumn(
        "salary_category",
        when(col("salary") >= 80000, "High")
        .when(col("salary") >= 50000, "Medium")
        .otherwise("Low")
    )

    # Filter employees

    df = df.filter(
        col("salary") > 50000
    )

    # Select required columns

    result_df = df.select(
        "id",
        "name",
        "hire_date",
        "salary",
        "annual_salary",
        "salary_category"
    )

    #Write as Parquet

    result_df.write \
        .mode("overwrite") \
        .parquet("output/employees")



### 21.2 Quick Revision

1. filter()              → filter rows
2. to_date()             → string → date
3. when().otherwise()    → conditional logic
4. fillna()              → replace NULL values
5. withColumnRenamed()   → rename columns
6. withColumn()          → create/transform columns
7. filter() + &          → multiple conditions
8. cast("integer")       → datatype conversion
9. when().otherwise()    → create age groups
10. write.parquet()      → write DataFrame as Parquet