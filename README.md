# Alpha Vantage Crypto Prices ETL Data Pipeline

## Overview
An ETL (Extract, Transform, Load) data pipeline that serves the latest crypto price changes using Apache Airflow. The pipeline extracts cryptocurrency exchange rate data from Alpha Vantage API, transforms the data to calculate changes in the exchange rates, and loads the transformed data into a PostgreSQL database. The pipeline is designed to run periodically to keep the data up-to-date.

## Project Structure
```.
├── dag.py
├── func.py
├── requirements.txt
├── README.md
└── table.csv
```

### dag.py:

This file defines the Airflow DAG and its tasks. The DAG consists of three main tasks: task_1, task_2, and task_3, which correspond to the extract, transform, and load phases of the ETL process.

### func.py:

This file contains the functions used by the DAG tasks:

- extract(): Extracts cryptocurrency exchange rate data from the Alpha Vantage API and stores it in a CSV file.
- transform(): Transforms the data by calculating the changes in exchange rates and appending the updated data back to the CSV file.
- load(): Loads the transformed data into a PostgreSQL database.

## Setup and Installation

### Prerequisites
- Python 3.8+
- Apache Airflow
- PostgreSQL
- Alpha Vantage API key

### Installation
1. Clone the repository:
```
git clone https://github.com/MinaBasem/etl-data-pipeline.git
cd etl-data-pipeline
```

2. Install the required Python packages:
```
pip install -r requirements.txt
```

3. Set up the PostgreSQL database and create the necessary table:
```
CREATE TABLE prices_and_change (
    Timestamp TIMESTAMP,
    BTC FLOAT,
    BTC_change VARCHAR(20),
    ETH FLOAT,
    ETH_change VARCHAR(20),
    LTC FLOAT,
    LTC_change VARCHAR(20),
    XRP FLOAT,
    XRP_change VARCHAR(20),
    SOL FLOAT,
    SOL_change VARCHAR(20)
);
```
4. Configure the Airflow connection for PostgreSQL:

  In the Airflow web UI, navigate to Admin -> Connections, and add a new connection:
```
Conn Id: postgres_default
Conn Type: Postgres
Host: <postgresql_host>
Schema: Crypto (database name)
Login: postgres
Password: ####
Port: 5432
```

### Running the DAG
1. Start the Airflow scheduler and web server in a terminal:
```
airflow db init
airflow scheduler
airflow webserver
```
2. Access the Airflow web UI (usually at http://localhost:8080), and trigger the ETL_Dag.
