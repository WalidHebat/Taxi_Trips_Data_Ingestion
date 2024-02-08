FROM python:3.9

RUN pip install pandas

RUN pip install sqlalchemy psycopg2

COPY yellow_tripdata_2021_jan.csv yellow_tripdata_2021_jan.csv

COPY ingest.py ingest.py

ENTRYPOINT ["python","ingest.py"]
