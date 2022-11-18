# Data Modeling with Postgres

## Project Summary

In this Project we learned how to create an ETL process, extracting data from JSON files and inserting them into a Postgres database fulfilling the data modeling star schema requirements.

- Learned about data modeling, star schema design
- Learned about creating this model design in Postgres
- Learned how to implement an ETL process using python


## Project Description

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

### Project Data

#### Song Data
The files are partitioned by the first three letters of each song's track ID. For example, here are file paths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```
- **Song data JSON example**: 
```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

#### Log Data
The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

```
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```
- **Log data JSON example**: 

```
{"artist":"N.E.R.D. FEATURING MALICE","auth":"Logged In","firstName":"Jayden","gender":"M","itemInSession":0,"lastName":"Fox","length":288.9922,"level":"free","location":"New Orleans-Metairie, LA","method":"PUT","page":"NextSong","registration":1541033612796.0,"sessionId":184,"song":"Am I High (Feat. Malice)","status":200,"ts":1541121934796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.3; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"101"}
```

## Data Model description

The schema consists of one Fact table (songplays) and four dimension tables (Songs, Artists, Time, Users), each dimension table has a primary key that can be used to join the table back to the fact table.

### Justification for RMDBS:
- There data is not large enough to suggest a big data solution
- The data needs to be stored in away to answer a variety of business questions (that aren't predetermined)
- The structure enables efficient aggregation
- The source data is structured and we know what fields and their data types we need.


## Python Environment setup

- Python 3 
- Psycopg2 package
- Read and write access to a Postgres database. 

## Files in repository

- Data Folder and files: Contains the Song data needed for Songs and Artists tables and the Log Data needed for the time and users tables.
- sql_queries.py: This contains all the required sql statements; create tables, insert into tables, drop tables, song select query for building the songsplay table.
- create_tables.py: Will create the database if it does not exist. Contains the loops to run through all the sql_queries when called by the etl.py file
- etl.py: This will read in the song and log file data, process the data and insert it into the tables.
- etl.pynb: A python notebook used to explore, test and design the etl process.
- test.pynb: A python notebook that can be used to test if your data has loaded properly and your tables are built correctly.

### How to run the scripts

Run the following commands in Python 3 Console or at the Terminal.

##### Python 3 Console line:
- %run create_tables.py
- %run etl.py

##### Terminal

- python create_tables.py
- python etl.py 
