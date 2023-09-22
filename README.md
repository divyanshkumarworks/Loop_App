# Loop_App

## Introduction
Welcome to the LOOP_APP(Restaurant Online Status Monitoring System). This system is designed to monitor the online status of several restaurants in the United States and provide detailed reports on the occurrences of restaurants going offline during their business hours. This documentation will guide you through the installation, configuration, and usage of the system.

## Problem Statement
Loop is responsible for monitoring the online status of multiple restaurants across the US. Each restaurant is expected to be online during its business hours. However, occasionally, restaurants may go offline for unknown reasons. To address this issue, restaurant owners require a report detailing the frequency of such incidents in the past.

## Demo
![loopapp](https://github.com/divyanshkumarworks/Loop_App/assets/134360630/aa77bd3f-5409-4aa9-9c27-a5cf1b6be08e)

## Getting Started: 🚀

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋
1. first of all, You need to install python for running pip command
2. create a project folder
3. setup Postgresql for your pc  

### Local Development
1. Clone the repository inside this folder
```bash
https://github.com/divyanshkumarworks/Loop_App.git
```

2. Install Dependencies
```bash
pip3 install -r requirements.txt
```

5. Run database migrations using:
```bash
python manage.py makemigrations

python manage.py migrate
```
it will create the database schemas, tables and relationships. 

6. And then run:
```bash
python manage.py runserver
```
this command will run the local server. 

## API Endpoints

1. `/trigger_report` triggers report generation from the data provided (stored in DB)
    1. No input 
    2. Output - report_id (random string), report_id is used for polling the status of report completion 
    
    **Request/Response**
    ```bash
    http://127.0.0.1:8000/trigger_report

    {
        "report_id": 14
    }
    ```
3. `/get_report` returns the status of the report or the csv
    1. Input - report_id
    2. Output
        - if report generation is not complete, return “Running” as the output
        - if report generation is complete, return “Complete” along with the CSV file with the schema described above.
        - if any kind of error occurs in between the process and the request is not completed, it returns “Error occurred” as the output

    **Request/Response**
    ```bash
    http://127.0.0.1:8000/trigger_report/14

    {
        "status": "Complete",
        "csv_file": "C:\\Users\\rishu\\projects\\Loop_App\\media\\reports/14.csv"
    }
    ```
