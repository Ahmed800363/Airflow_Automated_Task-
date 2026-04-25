from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime,timedelta

def fun1():
    for i in range(10):
        print(i)


with DAG (dag_id = 'email_send',
        start_date = datetime(2025,3,14),
        schedule_interval = timedelta(minutes=5),
        catchup = False
        ) as dag:
    
    task_email = EmailOperator(
           task_id = "send_Email",
           to = 'ahmedmohamedalqadi9999@gmail.com',
           subject = "test airflow",
           html_content = '<h1>hello , ahmed mohamed my name is ahmed ramanda this massege to tell to i love you </h1>'
        )
    task_bash = BashOperator(
        task_id = 'task_bash',
        bash_command = 'python /data/task.py'
        )
    task_python= PythonOperator(
          task_id = "task_python",
          python_callable = fun1 
        )
task_email >> task_bash >> task_python 
           