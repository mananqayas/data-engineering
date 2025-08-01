# What worklows I completed using Kestra:

Kestra is an open-source, event-driven orchestration platform that simplifies building both scheduled and event-driven workflows. By adopting Infrastructure as Code practices for data and process orchestration, Kestra enables you to build reliable workflows with just a few lines of YAML.

[Kestra official website](https://kestra.io/)

## ETL Pipeline for Green and Yellow Taxi data from NYC's Taxi and Limousine Commission (TLC) using Postgresql database

Following tasks are completed for this [ETL pipeline](ingest-csv-to-postgresql.yaml):

1. Setup local instance of Kestra service using [docker compose](docker-compose.yaml)
2. Extract green and yellow taxi datasets from CSV files
3. Using jdbc postgresql plugin, copied the CSV files to postgres staging tables
4. Merged data from staging to main tables for 12 months in a local postgresql database instance
5. [Used DBT](dbt-with-postgres.yaml) (Data Build Tool) to transform raw data into analytics ready tables and stored them in postgres database
6. Setup [scheduling and backfills](schedling-and-backfills.yaml) for future and past datasets respectively

## ETL Pipeline with Scheduled and Backfills

Following tasks are completed for this [ETL pipeline](gcp-setup-workflow.yaml):

1. Setup production instance of Kestra in GCP using Docker
2. Setup Google Compute Engine, Google Cloud Storage Bucket, and Cloud SQL for high availability
3. Created Service Account for Least Privilege access to resources
4. Setup Kestra workflow to ingest green and yellow taxi datasets from CSV to Gloud Cloud Storage as a datalake
5. Created [cron schedules](gcp-scheduling-and-backfills.yaml) for future ingestion automatically and backfilled past data
6. Created Google BigQuery dataset and tables for both green and yellow datasets using Kestra
7. [Used DBT](gcp-dbt.yaml) (Data Built Tool) to transform raw data into analytics ready tables and stored them in BigQuery dataset
