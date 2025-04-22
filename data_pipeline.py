from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past':False,
    'start_date': datetime(2025, 4, 19),
    'retries':1,
    'retries_delay': timedelta(minutes=5)
}

with DAG(

    'Pipeline-data-mongo',
    default_args=default_args,
    description='extract data by API and ingest in MongoDB',
    schedule_interval=timedelta(days=1),
    catchup=False,

) as dag :

    t1 = BashOperator(
        task_id='extract_data',
        bash_command='python /home/andre/Documents/projetos/2025/airflow_test/pr_mongodb_basic/test_request.py',
    )

    t2 = BashOperator(
        task_id='ingest_data',
        bash_command='python /home/andre/Documents/projetos/2025/airflow_test/pr_mongodb_basic/ingest_data_mongo.py',
    )

    t1 >> t2




