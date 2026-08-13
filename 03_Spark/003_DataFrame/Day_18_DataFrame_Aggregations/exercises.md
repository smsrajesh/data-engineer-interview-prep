PySpark --- Day 18: DataFrame_Aggregations --- Interview Questions

### Interview Questions :

1. What is groupBy() in PySpark?

2. What does groupBy() return?

3. Why can groupBy() cause a shuffle?

4. Why is shuffle expensive?

5. What is a partition?

6. What is partial aggregation?

7. How does partial aggregation reduce shuffle cost?

8. What is the difference between df.count() and count("column")?

9. What is the difference between count() and countDistinct()?

10. What is cardinality?

11. Why can countDistinct() be expensive for high-cardinality columns?

12. What is approx_count_distinct()?

13. How does sum() handle NULL values?

14. How does avg() handle NULL values?

15. Why can't we simply average partition averages?

16. How can Spark calculate an average in a distributed environment?

17. What is the difference between min() and least()?

18. What is the difference between max() and greatest()?

19. What is agg()?

20. What is the difference between df.agg() and df.groupBy().agg()?

21. Why use aliases for aggregation columns?

22. Why is one groupBy().agg() generally preferable to multipleseparate grouped aggregations?