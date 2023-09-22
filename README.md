# Loop_App

## Introduction
Welcome to the LOOP_APP(Restaurant Online Status Monitoring System). This system is designed to monitor the online status of several restaurants in the United States and provide detailed reports on the occurrences of restaurants going offline during their business hours. This documentation will guide you through the installation, configuration, and usage of the system.

## Problem Statement
Loop is responsible for monitoring the online status of multiple restaurants across the US. Each restaurant is expected to be online during its business hours. However, occasionally, restaurants may go offline for unknown reasons. To address this issue, restaurant owners require a report detailing the frequency of such incidents in the past.

## Demo
![loopapp](https://github.com/divyanshkumarworks/Loop_App/assets/134360630/aa77bd3f-5409-4aa9-9c27-a5cf1b6be08e)

## API Endpoints

1. /trigger_report endpoint that will trigger report generation from the data provided (stored in DB)
    1. No input 
    2. Output - report_id (random string) 
    3. report_id will be used for polling the status of report completion
2. /get_report endpoint that will return the status of the report or the csv
    1. Input - report_id
    2. Output
        - if report generation is not complete, return “Running” as the output
        - if report generation is complete, return “Complete” along with the CSV file with the schema described above.
        - if any kind of error occurred in between the process and not able to complete the request, it returns “Error occurred” as the output
