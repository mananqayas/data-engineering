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

#### What worklows I completed using Kestra:

Kestra is an open-source, event-driven orchestration platform that simplifies building both scheduled and event-driven workflows. By adopting Infrastructure as Code practices for data and process orchestration, Kestra enables you to build reliable workflows with just a few lines of YAML.

[Kestra official website](https://kestra.io/)

**ETL Pipeline for Green and Yellow Taxi data from NYC's Taxi and Limousine Commission (TLC) using Postgresql database**

Following tasks are completed for this [ETL pipeline](workflow-orchestration/ingest-csv-to-postgresql.yaml):

1. Setup local instance of Kestra service using [docker compose](workflow-orchestration/docker-compose.yaml)
2. Extract green and yellow taxi datasets from CSV files
3. Using jdbc postgresql plugin, copied the CSV files to postgres staging tables
4. Merged data from staging to main tables for 12 months in a local postgresql database instance
5. [Used DBT](workflow-orchestration/dbt-with-postgres.yaml) (Data Build Tool) to transform raw data into analytics ready tables and stored them in postgres database
6. Setup [scheduling and backfills](workflow-orchestration/schedling-and-backfills.yaml) for future and past datasets respectively

**ETL Pipeline with Scheduled and Backfills**

Following tasks are completed for this [ETL pipeline](workflow-orchestration/gcp-setup-workflow.yaml):

1. Setup production instance of Kestra in GCP using Docker
2. Setup Google Compute Engine, Google Cloud Storage Bucket, and Cloud SQL for high availability
3. Created Service Account for Least Privilege access to resources
4. Setup Kestra workflow to ingest green and yellow taxi datasets from CSV to Gloud Cloud Storage as a datalake
5. Created [cron schedules](workflow-orchestration/gcp-scheduling-and-backfills.yaml) for future ingestion automatically and backfilled past data
6. Created Google BigQuery dataset and tables for both green and yellow datasets using Kestra
7. [Used DBT](workflow-orchestration/gcp-dbt.yaml) (Data Built Tool) to transform raw data into analytics ready tables and stored them in BigQuery dataset
