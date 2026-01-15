# 최종 형상
airflow_practice/
 ├─  config/      ← airflow 설정 파일을 넣어두는 자리 (기본 설정은 yaml에 정의됐고, 주로 커스텀 시, 추가)
 ├─  dags/        ← DAG Python 파일 저장 폴더
 ├─  ⭐️data/      ← (필요 시, yaml에 추가) 작업한 내용물 담을 디렉토리 (로컬에도 남을 수 있도록)
 ├─  logs/        ← Task 로그 저장 폴더
 ├─  plugins/     ← 추가 Python 플러그인 (custom operator, hook) 저장 폴더
 ├─  .env         ← Docker 컨테이너와 내 컴퓨터 권한 충돌을 막기 위한 설정 (KEY-VALUE 형태)
 ├─  requirements.txt         ← 파이썬 라이브러리 & 버전 명시
 └─  docker-compose.yaml ← airflow Docker 컨테이너 생성을 위한 설정 값

# 작업 디렉토리를 생성 & Airflow용 기본 폴더 만들기
mkdir -p ./dags ./logs ./plugins ./config ./data
touch requirements.txt
