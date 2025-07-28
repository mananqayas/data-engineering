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