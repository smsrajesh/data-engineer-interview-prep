# Day 01 — Data Engineering Terminology

## Topic

Data Pipeline & Data Loading

---

## Keywords

1. Data Pipeline
2. Data Ingestion
3. ETL
4. ELT
5. Batch Processing
6. Full Load
7. Incremental Load
8. CDC
9. Watermark
10. Data Transformation

---

# Data Engineering Terminology :

> Quick-reference glossary for Data Engineer interview preparation.

> Format: Meaning → Think → Connect

---

## 1. Data Engineering Fundamentals :

### Data Pipeline

**Meaning:** Process that moves and processes data from source to target.

**Think:** Data Flow

**Connect:** Ingestion → Transformation → Target

---

### Data Ingestion

**Meaning:** Bringing data from source systems into a data platform.

**Think:** Get data in

**Connect:** Source → S3 → Snowflake

---

### ETL

**Meaning:** Extract, transform, then load data.

**Think:** Transform first

**Connect:** Source → Transform → Target

---

### ELT

**Meaning:** Extract, load, then transform data.

**Think:** Load first

**Connect:** S3 → Snowflake → dbt

---

## 2. Data Loading :

### Batch Processing

**Meaning:** Processing data in groups at scheduled intervals.

**Think:** Process in batches

**Connect:** Schedule → Batch → Target

---

### Full Load

**Meaning:** Loading the complete dataset.

**Think:** Load everything

**Connect:** Initial Load → Refresh

---

### Incremental Load

**Meaning:** Loading only new or changed data.

**Think:** Load the delta

**Connect:** CDC → Watermark → MERGE

---

### CDC

**Meaning:** Capturing inserts, updates, and deletes from a source.

**Think:** Capture changes

**Connect:** Source Changes → Incremental

---

### Watermark

**Meaning:** Boundary showing how far previous processing has completed.

**Think:** Where did I stop?

**Connect:** Timestamp → Incremental Load

---

## 3. Data Transformation :

### Data Transformation

**Meaning:** Converting raw data into usable/business-ready data.

**Think:** Make data useful

**Connect:** Clean → Join → Derive → Model

---

## Key Connections :

### Pipeline Flow

    Source → Ingestion → Processing → Transformation → Target

### Loading Strategy

    Full Load → Initial/Complete Load

    Incremental Load → New/Changed Data

### Incremental Processing

    CDC → Identify Changes  

    Watermark → Track Processing Boundary  

    Incremental Load → Process Delta 

    MERGE → Apply Changes

### ETL vs ELT

    ETL → Transform → Load

    ELT → Load → Transform

### Incremental Processing Connection

**CDC identifies changes → Incremental Load processes those changes → Watermark tracks processing progress.**