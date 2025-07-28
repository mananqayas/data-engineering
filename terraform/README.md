# Terraform

Terraform is an Infrastructure as Code (IaC) tool used for creating cloud and on-premsis infrastructure using code.

It is developed by Hashicorp.

## Why Terraform

- Simplicity in keeping track of infrastructure
- Easier collaboration
- Reproducibility
- Version control of source code
- Ensure resources are removed

## What Terraform is not used for

- Does not manage and update code on infrastructure
- Does not give you the ability to change immutable resources
- Not used to manage resources not defined in your terraform files

## Key Terraform Commands

<!--

Main commands:
  init          Prepare your working directory for other commands
  validate      Check whether the configuration is valid
  plan          Show changes required by the current configuration
  apply         Create or update infrastructure
  destroy       Destroy previously-created infrastructure -->

```bash

# Prepare your working directory for other commands
terraform init
# Check whether the configuration is valid
terraform validate
# Check changes required by the current configuration
terraform plan
# Create or update infrastructure
terraform apply
# Destroy previously-created infrastructure
terraform destroy
```

## Create Storage Bucket and BigQuery Dataset in GCP

Using terraform variables, I created all the necessary variables for reusablity on other terraform projects.

Here is the terraform variables file:

```bash

variable "projectId" {
  description = "Project ID"
  default     = "data-engineering-467303"

}
variable "credentials" {

  description = "My Credentials"
  default     = "./data-engineering-467303-17efdb3b433e.json"

}
variable "region" {
  description = "Region"
  default     = "us-central1"

}
variable "location" {
  description = "Project Location"
  default     = "US"

}
variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset_by_manan"

}


variable "gcs_bucket_name" {

  description = "Bucket bucket name"
  default     = "data-engineering-467303-terra-bucket"

}

variable "gcs_storage_class" {

  description = "Bucket storage class"
  default     = "STANDARD"

}

```

Here is main.tf file, which uses "hashicorp/google" provider with inline credentails where file path is stored in variables for security best practices.

```
// using hashicorp/google version 5.6.0 provider
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"

    }
  }
}
// instantiating the provider connection with project Id, and region from variables.tf file
provider "google" {
  credentials = file(var.credentials)
  project     = var.projectId
  region      = var.region
}

// creating a Storage Bucket resource
resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

// creatting a BigQuery dataset
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bq_dataset_name
}
```
