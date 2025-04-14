import snowflake.connector
import pandas as pd
import os

# Snowflake connection details (replace with your actual credentials)
SNOWFLAKE_ACCOUNT = "ekuleif-zk91983"
SNOWFLAKE_USER = "dbt_user"
SNOWFLAKE_PASSWORD = "fj2i7e85uRCtm3e"
SNOWFLAKE_DATABASE = "ECOMMERCE_DB"
SNOWFLAKE_SCHEMA = "STAGING"
SNOWFLAKE_WAREHOUSE = "ECOMMERCE_WH"  # Or your preferred warehouse
CSV_FILE_PATH = "../data/online_retail.csv"
TABLE_NAME = "raw_orders"  # Name of your staging table

def connect_to_snowflake():
    try:
        conn = snowflake.connector.connect(
            account=SNOWFLAKE_ACCOUNT,
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA,
            warehouse=SNOWFLAKE_WAREHOUSE
        )
        print("Successfully connected to Snowflake!")
        return conn
    except snowflake.connector.Error as e:
        print(f"Error connecting to Snowflake: {e}")
        return None

def create_staging_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            CREATE OR REPLACE TABLE {TABLE_NAME} (
                InvoiceNo VARCHAR,
                StockCode VARCHAR,
                Description VARCHAR,
                Quantity NUMBER,
                InvoiceDate TIMESTAMP_NTZ,
                UnitPrice NUMBER,
                CustomerID NUMBER,
                Country VARCHAR
            )
        """)
        print(f"Staging table '{TABLE_NAME}' created or replaced.")
    except snowflake.connector.Error as e:
        print(f"Error creating staging table: {e}")
    finally:
        cursor.close()

def load_csv_to_snowflake(conn,table_name):
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            COPY INTO {table_name}
            FROM @%{table_name}
            FILE_FORMAT = (TYPE = 'CSV', FIELD_OPTIONALLY_ENCLOSED_BY = '"', SKIP_HEADER = 1)
            ON_ERROR = 'CONTINUE'
        """)
        print(f"Data loaded into '{table_name}'.")
    except snowflake.connector.Error as e:
        print(f"Error loading data: {e}")
    finally:
        cursor.close()

def upload_csv_to_stage(conn, csv_path, table_name):
    cursor = conn.cursor()
    try:
        cursor.execute(f"PUT file://{os.path.abspath(csv_path)} @%{table_name} AUTO_COMPRESS=TRUE OVERWRITE=TRUE;")
        print(f"CSV file '{csv_path}' uploaded to stage for table '{table_name}'.")
    except snowflake.connector.Error as e:
        print(f"Error uploading file to stage: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    snowflake_conn = connect_to_snowflake()
    if snowflake_conn:
        create_staging_table(snowflake_conn)
        upload_csv_to_stage(snowflake_conn, CSV_FILE_PATH, TABLE_NAME)
        load_csv_to_snowflake(snowflake_conn, TABLE_NAME)
        snowflake_conn.close()