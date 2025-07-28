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

