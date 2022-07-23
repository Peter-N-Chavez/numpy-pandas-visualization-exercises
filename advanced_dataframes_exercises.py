
    # Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)
    # cd into your exercises folder for this module and run echo env.py >> .gitignore

import numpy as np
import pandas as pd
import pydataset as data

    # Create a function named get_db_url. 
    # It should accept a username, hostname, password, and database name and return a url 
    # connection string formatted like in the example at the start of this lesson.

import env

def get_db_url(hostname, username, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url

    # Use your function to obtain a connection to the employees database.

url = get_db_url(env.hostname, env.username, env.password, "employees")

    # Once you have successfully run a query:

print(pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url))

    # a. Intentionally make a typo in the database url. What kind of error message do you see?

#   "Access denied"

    # b. Intentionally make an error in your SQL query. What does the error message look like?

#   "Exception has occurred. You have an error in your SQL syntax."

    # Read the employees and titles tables into two separate DataFrames.

emps = pd.read_sql('SELECT * FROM employees', url)
titles = pd.read_sql('SELECT * FROM titles', url)

    # How many rows and columns do you have in each DataFrame? Is that what you expected?

print(emps.shape)
print(titles.shape)

    # Display the summary statistics for each DataFrame.

print(emps.describe())

    # How many unique titles are in the titles DataFrame?

utit = titles["title"].nunique()
print(utit)

    # What is the oldest date in the to_date column?

oldtit = titles.to_date.min()
print(oldtit)

    # What is the most recent date in the to_date column?

    # ** This question is strange grammatically. Using the MAX or CURDATE comparison would get 9999-01-01, 
    # but that is not a recent date. It is a place holder value that represents that someone/something is there currently.
    #  Current != most recent, necessarily. I wish this was asked in a better way. **

rectit = pd.read_sql("SELECT to_date FROM titles WHERE to_date > CURDATE() LIMIT 1", url)
print(rectit)