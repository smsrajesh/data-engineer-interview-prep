# Day 02 — Data Engineering Terminology

## Topic :

Data Warehousing & Dimensional Modeling

---

## Keywords :

1. Data Warehouse
2. Data Lake
3. Data Lakehouse
4. Fact Table
5. Dimension Table
6. Grain
7. Measure
8. Dimension
9. Star Schema
10. Surrogate Key

---

# Data Engineering Terminology :

> Quick-reference glossary for Data Engineer interview preparation.
>
> Format: Meaning → Think → Connect

---

## 1. Data Platforms :

### Data Warehouse

**Meaning:** Centralized analytical data platform optimized for OLAP workloads.

**Think:** Centralized → Analytics → OLAP

**Connect:** ETL/ELT → Data Warehouse → BI

---

### Data Lake

**Meaning:** Centralized storage for large volumes of raw, structured, and semi-structured data.

**Think:** Raw → Flexible → Large-scale

**Connect:** Source → Data Lake → Processing

---

### Data Lakehouse

**Meaning:** Combines the flexibility of a Data Lake with analytical capabilities associated with a Data Warehouse.

**Think:** Lake + Warehouse

**Connect:** Data Lake → Lakehouse → Analytics

---

## 2. Dimensional Modeling :

### Fact Table

**Meaning:** Stores business events, measures, and foreign keys to related dimensions.

**Think:** What happened? How much?

**Connect:** Grain → Measure → Dimension

---

### Dimension Table

**Meaning:** Stores descriptive context used to analyze business events in fact tables.

**Think:** Who? What? When? Where?

**Connect:** Dimension → Fact → Analysis

---

### Grain

**Meaning:** Defines what one row in a fact table represents.

**Think:** One row = ?

**Connect:** Grain → Fact → Measures

---

### Measure

**Meaning:** A business metric that can be analyzed or aggregated.

**Think:** Sales → Quantity → Profit

**Connect:** Measure → Fact → Aggregation

---

### Dimension

**Meaning:** A business perspective or context used to analyze facts and measures.

**Think:** Who? What? When? Where?

**Connect:** Dimension → Fact → Measure

---

### Star Schema

**Meaning:** Dimensional model with a central fact table connected directly to dimension tables.

**Think:** Fact in center

**Connect:** Fact → Dimensions → Analytics

---

### Surrogate Key

**Meaning:** System-generated identifier used to uniquely identify a dimension record.

**Think:** Artificial → Unique → No business meaning

**Connect:** Surrogate Key → Dimension → Primary Key → SCD

---

## Key Connections :

### Concept Flow

    Data Sources → Data Lake → Data Warehouse/Lakehouse → Dimensional Model → Fact + Dimensions → Analytics

### Dimensional Modeling

    Business Process → Grain → Fact Table → Measures

    Business Context → Dimension Table → Descriptive Attributes

### Fact & Dimension

    Fact → What happened?

    Measure → How much?

    Dimension → By whom/what/when/where?

### Schema

    Fact Table + Dimension Tables → Star Schema

### Keys

    Business Key → Surrogate Key → Dimension Record

---

## Learning Rules

- 10 new keywords per day.
- Previous terminology must be recalled regularly.
- Use active recall before definitions.
- Mix old and new concepts.
- Build a connected mental model.
- Keep terminology notes short.
- Do not duplicate detailed technology explanations.
- Do not complete one technology before moving to another.
- Learn horizontally across the Data Engineering stack.
- Do not introduce Kafka/streaming yet.

## Learning Rounds

Round 1 — Big Picture

Round 2 — Core

Round 3 — Intermediate

Round 4 — Advanced Core

Round 5 — Performance

Round 6 — Production

## Main Areas

- Data Engineering Fundamentals
- SQL
- Python
- PySpark / Spark
- Snowflake
- AWS
- dbt
- Airflow
- Data Warehousing
- Data Modeling
- Data Quality
- Data Reliability
- Data Governance
