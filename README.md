# 최종 형상

```
airflow_practice
 ├─  config     ← airflow 설정 파일을 넣어두는 자리 (기본 설정은 yaml에 정의됐고, 주로 커스텀 시, 추가)
 ├─  dags        ← DAG Python 파일 저장 폴더
 ├─  ⭐️data      ← (필요 시, yaml에 추가) 작업한 내용물 담을 디렉토리 (로컬에도 남을 수 있도록)
 ├─  logs        ← Task 로그 저장 폴더
 ├─  plugins     ← 추가 Python 플러그인 (custom operator, hook) 저장 폴더
 ├─  .env         ← Docker 컨테이너와 내 컴퓨터 권한 충돌을 막기 위한 설정 (KEY-VALUE 형태)
 ├─  requirements.txt         ← 파이썬 라이브러리 & 버전 명시
 └─  docker-compose.yaml ← airflow Docker 컨테이너 생성을 위한 설정 값
```

0. 작업 디렉토리를 생성 & Airflow용 기본 폴더 만들기
```
mkdir -p ./dags ./logs ./plugins ./config ./data
touch requirements.txt
```
1. Airflow 설치
- `docker-compose.yaml`
- `curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.1.5/docker-compose.yaml'` 
2. docker-compose.yaml 파일 수정
AIRFLOW__CORE__LOAD_EXAMPLES: 'true' → ‘false’
```
  volumes:
		...
  - ./data:/opt/airflow/data
  - ./requirements.txt:/requirements.txt
  environment:
	  ...
	  _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-} #--> 해당 값이 있다면 삭제 후 
   _PIP_ADDITIONAL_REQUIREMENTS_FILE: /requirements.txt
```
3. .env 파일 만들기 (권한 문제 방지)
`echo "AIRFLOW_UID=50000" > .env`
4. Airflow 초기화
`docker compose up airflow-init`
5. Airflow docker 컨테이너 생성
`docker compose up -d `
6. Airflow 접속
[http://localhost:8080](http://localhost:8080/)
7. DAG 파일 만들기: dags 폴더 안에 .py 파일 넣으면 Airflow UI에 DAG가 자동으로 나타남.
