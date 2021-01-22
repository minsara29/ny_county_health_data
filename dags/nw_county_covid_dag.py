from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import pandas as pd
import requests as re


URL = 'https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD'

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 1, 20),
    "schedule_interval": '0 9 * * *',
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "newyork_county_covid_daily",
    default_args=default_args,
    schedule_interval=timedelta(1))


import os
cwd = os.getcwd()
print(cwd)
print("Kannan")

health_json = re.get(URL).json()
health_df = pd.DataFrame(health_json["data"])
health_data = health_df.iloc[:, [9]]
health_data.columns = ['county']
counties = health_data['county'].unique().tolist()

script_path = f"/usr/local/airflow/scripts/health_data.py"
print(script_path)
bash_command = f"python {script_path} "
print(bash_command)

for county in counties:
    task_name = str(county).replace(" ", "_") + '_task'
    print(task_name)
    county_pipeline = BashOperator(
        task_id=task_name,
        bash_command=f"{bash_command} {county}",
        dag=dag)
