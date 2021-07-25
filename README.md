# OLYMPICS 2020 SCRAPPER

Scrapes the standings page of Olympics to create a well formatted csv.

The goal is to run this everyday and collect a history of standings to create a dashboard.

## Dependencies
---

This was made using python 3.8.10 and subsequent libraries.  
The following libraries will be required:

* beautifulSoup
* requests
* csv
* datetime

A compliation of all requirements can be found in the **requirements.txt** file, and can be installed with this command:

$> pip install -r requirements.txt

## Run
---

In order to the program, you will first need the above dependencies. To try and run the program:

$> python app.py

## Data
---

The data has been scrapped from `https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm?utm_campaign=dp_google` url.
