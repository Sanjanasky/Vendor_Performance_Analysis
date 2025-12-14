import pandas as pd
import os
import time
from sqlalchemy import create_engine
import logging

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    logging.info(f"Table '{table_name}' ingested successfully.")

def load_raw_data():
    start = time.time()

    for file in os.listdir('data'):
        if file.endswith('.csv'):
            df = pd.read_csv('data/' + file)
            logging.info(f'Ingesting {file} into database...')
            ingest_db(df, file[:-4], engine)

    end = time.time()
    total_time = round((end - start) / 60, 2)

    logging.info('---------------- Ingestion Complete ----------------')
    logging.info(f'Total Time Taken : {total_time} minutes')

if __name__ == "__main__":
    load_raw_data()
