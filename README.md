Weather Data Engineering Pipeline

A Python-based ETL pipeline that collects weather data from a REST API, processes and validates the data using Pandas, and loads the cleaned dataset into PostgreSQL for further analysis using SQL.

The project was created as a practical exercise to develop and demonstrate core Data Engineering skills, including API integration, data transformation, data quality validation, database loading, and pipeline monitoring.

Project Overview

The pipeline follows a simple ETL architecture:

REST API → Python → Pandas → Data Validation & Transformation → SQLite → SQL Analysis

The pipeline retrieves weather information from a public API, stores the raw response, transforms the data into a structured format, performs data quality checks, and loads the resulting dataset into a PostgreSQL database.

Technologies:

Python – pipeline development

Requests_Cache – Cached REST API communication

Pandas – data processing and transformation

SQLite – persistent data storage

Git / GitHub – version control

Pipeline Architecture:

                ┌──────────────┐
                │  Open Meteo  │
                │     API      │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   Extract    │
                │   Python     │
                │  requests    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Transform   │
                │   Pandas     │
                └──────┬───────┘
                       │
                       ▼
              ┌──────────────────┐
              │  Data Validation |
              │        &         |
              │     Logging      │
              └────────┬─────────┘
                       │
                       ▼
                ┌──────────────┐
                │    SQLite    │
                │   Database   │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ SQL Analysis │
                └──────────────┘



How the Pipeline Works

The complete pipeline can be executed through the main Python script:

python app.py

The pipeline then:

1) Connects to the weather API

2) Retrieves the latest weather data

3) Loads the data into a Pandas DataFrame

4) Performs data cleaning and transformation

5) Runs data quality checks

6) Loads valid data into SQlite DB

7) Records the pipeline/data quality status

8) Makes the processed data available for SQL analysis



Future Improvements:

- Potential improvements to the project include:

- Containerising the pipeline with Docker

- Automating execution with a workflow orchestrator

- Adding automated tests

- Expanding data quality monitoring

- Adding more weather locations

- Implementing incremental data loading

- Creating a dashboard for analysing historical weather data
