import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

def get_brewery_api():
    import requests
    URL = 'https://api.openbrewerydb.org/v1/breweries'
    response = requests.get(URL)
    return response.json()


default_args = dict(
    owner = 'yoorim',
    email = ['ann195200@naver.com'],
    email_on_failure = False,
    retries = 5
    )

with DAG(
    dag_id="10_http_operator_dag.py",
    start_date=pendulum.datetime(2025, 6, 1, tz='Asia/Seoul'),
    schedule="30 10 * * *", # cron 표현식
    tags = ['20260116'],
    default_args = default_args,
    catchup=False
):
    
    py1 = PythonOperator(
        task_id = 'py2',
        python_callable=get_brewery_api
    )
    
py1