0x00. MySQL Advanced
Overview
This project focuses on advanced MySQL concepts, including triggers, views, indexes, stored procedures, and more. By completing this assignment, you’ll gain a deeper understanding of how to optimize queries, create tables with constraints, and implement various features in MySQL.

Concepts Covered

Creating tables with constraints
Optimizing queries by adding indexes
Implementing stored procedures and functions
Working with views in MySQL
Using triggers effectively
Requirements
All files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
Ensure that all your files end with a new line.
Add comments just before your SQL queries (i.e., syntax above).
Start each file with a comment describing the task.
Use uppercase for SQL keywords (e.g., SELECT, WHERE).
A README.md file at the root of the project folder is mandatory.
The length of your files will be tested using wc.
Getting Started
Use “container-on-demand” to run MySQL.
Ask for a container with Ubuntu 18.04 and Python 3.7.
Connect via SSH or the WebTerminal.
Start MySQL in the container using: $ service mysql start.
Importing a SQL Dump
Create a new database: $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p.
Import the SQL dump: $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows.
Verify the data: $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows.
