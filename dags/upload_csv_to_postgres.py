from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

# def xlsx_to_csv(xlsx_file, csv_file):
#     df = pd.read_excel(xlsx_file)
    
#     df.to_csv(csv_file, index=False)
#     print(f"Conversion terminée : {csv_file}")

def load_csv_with_pandas():
    csv_path = '/data/sales.csv'
    table_name = 'raw_sales_data'

    # Crée le moteur SQLAlchemy pour PostgreSQL
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres:5432/airflow_db')

    # Lire le fichier CSV (tabulé)
    df = pd.read_csv(csv_path, sep=',')

    # Charger dans PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)  # Remplace la table à chaque fois

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    'sales_ingestion',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    
    # convert_type_file = PythonOperator(
    #     task_id='convert_xlsx_to_csv',
    #     python_callable=xlsx_to_csv,
    #     op_args=["/data/xlsx/Online Retail.xlsx", "/data/csv/sales.csv"]
    # )

    load_data_postgres = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_with_pandas
    )

    # convert_type_file >> 
    load_data_postgres
