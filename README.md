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
