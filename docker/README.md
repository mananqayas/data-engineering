# Docker for Data Engineering

[Docker Official Docs](https://docs.docker.com/)

Docker is a containerization service used to run applications in isolated containers. Containers are running instances of images, and images contain instructions including base image, runtime environment of application and other options.

Docker is used in modern application delivery across development and production environments reliably and securely. It is also used in MLOps, Microsevices and Cloud-native applications. Containers are orchestration using Kubernetes system for scalable applications.

## Docker image

To build a docker image, we use Dockerfile, it looks like this:

```Dockerfile

# Base image
FROM python:3.9

# Working directory is a directory in container where our app code is stored
WORKDIR /app

# COPY command is used to copy files from local filesytem to container's filesystem
COPY pipeline.py .

# RUN command is a image build time command, in this case installing pandas library while building a new image
RUN pip install pandas

ENTRYPOINT [ "python", "pipeline.py" ]

```

<!-- building the images -->

#### Building the image

```bash

docker build -t my-image .
```

-t argument is used is to tag the image name, and we can also add version like, **<u>my-image:latest</u>**

. is used to point to the Dockerfile, in this case it is current working directory.

<!-- listing the images -->

#### Listing the images

```bash

docker images
```

<!-- deleteing the images -->

#### Deleting the images

```bash

docker rmi [imageId] or [name]
```

## Docker container

We use a Docker image to run a container, this container runs our packaged application with it's own networking and container port, we can map container local port if any, we can map container port with host port using -p argument.

#### Running a container

```bash

docker run -it my-image bash
```

Here we run the container in interactive mode, where after starting, it takes us inside the container runtime where we can interact with it's file system, runtime and our containerized application. Cool!

#### Listing running containers

```bash

docker ps
```

#### Listing all containers - stopped, running etc

```bash

docker ps -a
```

#### Stopping a container

```bash

docker stop [containerId] | [name]
```

#### Starting a container

```bash

docker start [containerId] | [name]
```

#### Deleting a container

```bash

docker rm [containerId] | [name]
```

## Ingest CSV New York yelllow taxi data into Postgres database using Docker and Python

- Python code:

```python
import argparse
import kagglehub
import shutil
import os
from time import time
from sqlalchemy import create_engine
import pandas as pd
print(pd.__version__)

# print(args.username)

def main(params):
    user = params.username
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params. table_name
    data = params.data
    csv_name = 'output.csv'


    print("printing user", user)
    print("printing password", password)
    print("printing host", host)
    print("printing port", port)
    print("printing db name", db)
    print("printing table", table_name)

    os.system(f"wget {data} -O {csv_name}")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    engine.connect()

    path = kagglehub.dataset_download(f"elemento/{data}")

    file_name=""

    dest_dir = os.getcwd()
    if path != dest_dir:
        for filename in os.listdir(path):
            file_name = filename
            shutil.copy(os.path.join(path, filename), dest_dir)

    df_iter = pd.read_csv(file_name, iterator=True, chunksize=100000)

    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')
    count = 5
    while count > 0:
        t_start = time()
        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()

        print('inserted another chunk, took %.3f second' % (t_end - t_start))

        print(f"Adding {count} times")
        count = count - 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data into postgres")

    parser.add_argument("--username", required=True,  help="Username for Postgres database")
    parser.add_argument("--password", required=True,help="Password for Postgres database")
    parser.add_argument("--host", required=True, help="Host for Postgres database")
    parser.add_argument("--port", required=True, help="Port for Postgres database")
    parser.add_argument("--db", required=True, help="Postgres database")
    parser.add_argument("--table_name", required=True, help="Postgres database table")
    parser.add_argument("--data", required=True, help="Kaggle data")

    args = parser.parse_args()
    main(args)
```

- **Dockerfile**

```Dockerfile
FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2  kagglehub

WORKDIR /app
COPY ingest-data.py .
RUN mkdir -p /root/.kaggle
COPY kaggle.json /root/.kaggle/kaggle.json
RUN chmod 600 /root/.kaggle/kaggle.json

ENTRYPOINT [ "python", "ingest-data.py" ]
```

Postgres database and the pipeline containers must be in the same Docker network for networking communication.

- **Build Docker image**

```bash
docker build -f DockerfileV2 -t inject-csv-to-sql:latest .
```

- **Run Postgres database container**

```bash
docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v $(pwd)/ny_taxi_pg_data:/var/lib/postgresql/data \
--network=pd-network \
-p 5432:5432 \
--name pg-database \
postgres:13
```

- **Run Docker container for data ingestion**

```bash

docker run -it \
# Docker network
  --network=pd-network \
#   Image name for data ingestion Python script
  inject-csv-to-sql:latest \
#   Argument for database username
  --username root \
#   Argument for database password
  --password root \
#   Argument for database host
#   --host should be name of the Postgres database container
  --host pg-database \
#   Argument for database port
  --port 5432 \
#   Argument for database name
  --db ny_taxi \
#   Table name for the database - you can choose any suitable name
  --table_name taxi_data_table \
#   Argument for data - you get this from Kaggle CLI command, make sure to authenticate using Kaggle.json with volume mount
  --data nyc-yellow-taxi-trip-data
```
