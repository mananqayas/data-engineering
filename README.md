# Data engineering

This repo outlines my data engineering learnings. It includes learning hands-on tools used in modern data engineering workflows.

What it includes:

- Used Containerization (Deploy pipeline script as a docker container for repeatability)

- Worked with OLTP databases (Postgres, MySQL)

- Created simple data ingestion pipelines frome external sources and stored them in relational databases using Python scripts and Docker

- Used Kaggle datasets to explore real-world usecases

## [Docker](docker)

My Docker learning includes:

- Learned how to create custom images, run containers locally and in production

- Used Python to created pipeline script for batch processing

- `pandas` and `matplotlib` are used for data manipulation and visualization

- Used Jupiter Notebook for creating Python scripts

- Worked with Postgres database using `pgcli`, `psql`, and PgAdmin

## [Terraform](terraform)

My Terraform learning includes:

- Installed Terraform CLI
- Created Service Account in GCP for API access
- Set up a Terraform project locally
- Authenticated the project using environment variables
- Set up hashicorp/google provider to create GCP resources
- Created Google Storage Bucket and BigQuery dataset using HCL language in `main.tf`
- Created `variables.tf` file to add any reusable variables throughout the project
- Used different terraform commands, like `init`, `fmt`, `plan`, `validate`, `apply`, and `destroy` to manage the project

## [Workflow orchestration with Kestra](workflow-orchestration)

Workflow orchestration is a core part of **modern data engineering**. Without it, data pipelines break down quickly without scale.

### What is Workflow Orchestration?

Workflow orchestration is the process of **scheduling, managing, monitoring and automating** the execution of tasks in a data pipeline.

Think of it like a **conductor in an orchestra**:

- It doesn't do the work (like playing an instrument),
- But it **coordinates** when and how each musician (task) plays,
- Ensuring everything runs in the right order, with the right dependencies, and recovers from failures.

Without orchestration, you'd be:

- Writing custom scripts to run everything
- Manually handling retries, failures, and dependencies
- Completely blind when something breaks at 2AM

## [Data Warehouse - Google BigQuery](data-warehouse)

A data warehouse is a centralized system to **store, organize, and analyze large volumes of structured data** from multiple sources - specifically designed for **analytics and business intelligence (BI).**

## 🏢 Think of it like:

> A super-organized digital warehouse where raw materials (data) from different factories (databases, APIs, CRMs) are cleaned, stacked neatly, and made easy to find and analyze for decision-making.

## What is the purpose of a Data Warehouse

| Goal              |                             Description                              |
| :---------------- | :------------------------------------------------------------------: |
| ✅ Analytics      |              Enable fast querying across huge datasets               |
| ✅ Consolidation  | Combine data from multiple systems (Sales, Marketing, Finance, etc.) |
| ✅ History        |              Store long-term historical data for trends              |
| ✅ Data quality   |                Cleaned, structured, standardized data                |
| ✅ Reporting & BI |             Used by tools like Tableau, Power BI, Looker             |

## 📊 How is it different from a regular database?

| Feature       | Operational DB(e.g., PostgreSQL) | Data Warehouse                       |
| :------------ | :------------------------------: | ------------------------------------ |
| Optimized for |       Transactions (CRUD)        | Analytics (queries, aggregates)      |
| Date model    |            Normalized            | Denormalized (star/snowflow schemas) |
| Writes        |             Frequent             | Periodic (batch/stream)              |
| Queries       |         Short, frequent          | Long, complex                        |
| Storage       |        Smaller, real-time        | Historical, large-scale              |
| Users         |         Apps, developers         | Analysts, data scientists            |

## 🔁 Workflow: How data flows into a data warehouse

1. **Extract** data from sources e.g. APIs, OLTP databases (MySQL, PostgreSQL etc)
2. **Transform** it (cleaning, joining, aggregating)
3. **Load** it into warehouse (ETL or ELT process)
4. **Query** it using SQL or BI tools

This is part of the **data engineering lifecyle.**

I worked on Google BigQuery warehouse, most of the data warehouse provide the similar features.

**Here are the examples of Cloud Data Warehouses**

| Product                  |   Provider   | Highlights                               |
| :----------------------- | :----------: | ---------------------------------------- |
| BigQuery                 | Google Cloud | Serverless, fast, pay-per-query          |
| Snowflake                | Independent  | Cloud-native, separates compute/storage  |
| Amazon Redshift          |     AWS      | Scalable, integrates with AWS ecosystem  |
| Azure Synapse            |  Microsoft   | Deep integration with Power BI and Azure |
| ClickHouse               |  Yandex OSS  | Super-fast OLAP queries                  |
| Databricks SQL Warehouse |  Databricks  | Optimized for lakehouse architecture     |

## 📐 Schema Design in Warehouses

Data warehouses often use:

- **Star schema:** Fact table + many dimensions table
- **Snowflake schema:** Dimensions further normalized
- **Flat tables:** For fast query performance (common in modern cloud DWs)

## 📈 Real-World Example

E-commerce company data warehouse:

| Source     | Data              |
| :--------- | :---------------- |
| Shopify    | Orders, customers |
| Google Ads | Clicks, spend     |
| Stripe     | Payments          |
| Zendesk    | Support tickets   |
