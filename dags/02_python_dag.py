import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

def random_language():
        import random
        lang_list = ['Python','Java','Rust']
        lang = random.sample(lang_list, 1)
        return lang

default_args = dict(
    owner = 'yoorim',
    email = ['ann195200@naver.com'],
    email_on_failure = False,
    retries = 3
    )

with DAG(
    dag_id="02_python_dag",
    start_date=pendulum.datetime(2026, 1, 16, tz='Asia/Seoul'),
    schedule="30 10 * * *", # cron 표현식
    tags = ['20260116'],
    default_args = default_args,
    catchup=False
):
    py1 = PythonOperator(
        task_id = 'py1'
        python_callable=random_language
    )
    
py1