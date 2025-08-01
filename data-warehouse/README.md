# BigQuery

Google BigQuery is a **cornerstone tool in modern data engineering and machine learning** pipelines, especially on Google Cloud Platform (GCP).

## 🧠 What is BigQuery

**BigQuery** is a **serverless, fully-managed, cloud-native data warehouse** built by **Google Cloud.**

It is designed for:

- **Analytics**
- **Massive-scale SQL querying**
- **Near real-time reporting**
- **Machine learning integration**

## 🚀 Key Features / Benefits

| Feature                       | Benefit                                                      |
| :---------------------------- | ------------------------------------------------------------ |
| **Serverless**                | No infrastructure to manage - scales automatically           |
| **Fast SQL Engine**           | Columnar storage + distributed query engine                  |
| **Massive scale**             | Handles petabytes of data with ease                          |
| **Pay-per-query**             | You only pay for the data scanned ($5/TB)                    |
| **Partitioning & Clustering** | Boosts performance + lowers cost                             |
| **Streaming ingest**          | Real-time data via INSERT API or Pub/Sub                     |
| **Built-in-ML (BQML)**        | Train models directory inside BigQuery using SQL             |
| **Secure**                    | IAM, encryption, audit logs, row-level security              |
| **Federated queries**         | Query data in GCS, Sheets, Bigtable, Spanner without loading |

## 🔍 Internals - How BigQuery Works Under the Hood

| Component                       | Description                                               |
| :------------------------------ | --------------------------------------------------------- |
| Dremel Execution Engine         | Columnar execution mode for massive parallelism           |
| Colossus File System            | Google's distributed storage backend                      |
| Slot based architecture         | Query compute is divided into units called slots          |
| Tree based query execution      | Dremel uses a multi-level aggregation tree for efficiency |
| Columnar storage                | Reads only needed columns -> minimizes I/O                |
| Separation of storage & compute | Enables elastic scalability and concurrency               |

## ⚙️ Best Practices

#### ✅ Schema Design

- Use **nested & repeated fields** (denormalization to reduce joins)
- Prefer **wide tables** over highly normalized ones

#### ✅ Partioning

- Use **time-based partitioning** for date/time fields (e.g., created_at)
- Reduces data scanned and improved performance

#### ✅ Clustering

- Use **clustering** on common filter fields (e.g., user_id, country)
- Helps optimize sorting and prune irrelevant data faster

#### ✅ Query Optimization

- Use SELECT only_needed_columns
- AVOID SELECT \*
- Filter early using WHERE clauses
- Use approximate aggregation functions (APPROX_COUNT_DISTINCT)
- Monitor slot usage via GCP Console

#### ✅ Cost Control

- Use EXPLANATION or DRY RUN to estimate query cost
- Enable custom quotas
- Schedule query jobs with limiters

#### ✅ Security

- Use **IAM roles** to control access
- Row-level security and column-level encryption where needed

## 📊 BigQuery in Machine Learning (BQML)

BiqQuery lets you **train and use ML models directly in SQL** - this is **BigQuery ML (BQML)**

#### ✅ Benefits of BQML:

- No need to move data into Python or Jupyter notebooks
- Fast, scalable, and great for experimentation
- Supports **batch prediction, real-time prediction, and model evaluation**
- Easy to integrate with **Vertex AI** or **Looker/Tableau**

## 🤖 Supported Models in BQML:

| Model type                        | Use case                               |
| :-------------------------------- | -------------------------------------- |
| LINEAR_REG                        | Regression problems                    |
| LOGISTIC_REG                      | Binary classification                  |
| KMEANS                            | Clustering (unsupervised)              |
| ARIMA_PLUS, ML.ARIMA_EVALUATE     | Time-series forecasting                |
| BOOSTED_TREE_CLASSIFIER/REGRESSOR | Gradient boosting                      |
| DNN_CLASSIFIER/REGRESSOR          | Deep neural networks                   |
| TENSORFLOW                        | Bring your own TF model                |
| AUTO_ML                           | Use Vertex AI AutoML behind the scenes |

### Example: Train Logistic Regression in SQL

```sql
CREATE OR REPLACE MODEL `project.dataset.model_name`
OPTIONS(model_type='logistic_reg') AS
SELECT
  feature1,
  feature2,
  label
FROM
  `project.dataset.training_data`
```

### 🧰 Predict

| Use case                 | Description                                             |
| :----------------------- | ------------------------------------------------------- |
| 🔎 Customer segmentation | Run clustering on user behavior                         |
| 💰 Churn prediction      | Predict user churn based on historical actions          |
| 📦 Demand forecasting    | Use ARIMA on sales data for future inventory            |
| 📈 Marketing attribution | Analyze multi-touchpoint attribution with complex joins |
| ⚠️ Fraud detection       | Real-time scoring using model endpoints                 |
| 📄 Reporting dashboards  | Use BI tools connected to BigQuery                      |
