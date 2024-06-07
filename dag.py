from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import func

def task_1():
    func.extract()

def task_2():
    func.transform()

def task_3():
    func.load()

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': True, 
    'schedule_interval': timedelta(minutes=5)
}

# Define the DAG
with DAG(
    dag_id='ETL_Dag',
    default_args=default_args,
    #schedule_interval=None,  # Run the DAG manually
) as dag:

    # Define the tasks with dependencies
    task1 = PythonOperator(
        task_id='task_1',
        python_callable=task_1,
    )

    task2 = PythonOperator(
        task_id='task_2',
        python_callable=task_2,
        depends_on_past=True,
        #upstream_task_id=task1.task_id
    )

    task3 = PythonOperator(
        task_id='task_3',
        python_callable=task_3,
        depends_on_past=True,
        #upstream_task_ids=[task1.task_id, task2.task_id]
    )

# Set the task dependencies
task1 >> task2 >> task3
