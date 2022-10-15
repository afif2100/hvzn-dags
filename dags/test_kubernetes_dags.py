from tkinter.font import names
from airflow import DAG
from airflow.decorators import task

from datetime import datetime


with DAG(
    'tutorial',
    description='A simple tutorial DAG',
    tags=['example']):
    
    
    @task.virtualenv(
        task_id="virtualenv_python", requirements=["colorama==0.4.0"], system_site_packages=False)