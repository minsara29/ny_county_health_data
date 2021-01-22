# ny_county_health_data


API:
https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD
By following the ETL process, extract the data for each county in New York state from
the above API, and load them into individual tables in the database. Each county table
should contain following columns :
❖ Test Date
❖ New Positives
❖ Cumulative Number of Positives
❖ Total Number of Tests Performed
❖ Cumulative Number of Tests Performed
❖ Load date


# Implementation:

Airflow created daily scheduled dag
a. Utilized docker to run the Airflow and Postgres database locally
b. There is one dag containing all tasks needed to perform the end
to end ETL process
c. Dynamic concurrent task creation and execution in Airflow for each county
based on number of counties available in the response

# Solution & Desing 
Used :Python3, Sqlite3, request 
Airflow docker used : https://github.com/puckel/docker-airflow

pip install pysqlite3 
pip install requests
pip install apache-airflow


## Modules :

# health_data.py 
  - is a main module. It gets the data from API : https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD using request module 

# database_script.py
  - Sqlite database modules - Utilize SQLite in memory database for data storage

# nw_county_covid_dag.py
  - airflow Dag file. Scheduled daily that would run at 9:00 AM and ingest the data into the system
  
# unittest modules
  test_database_script.py and test_healthData.py
  
  


