## Data Science Project: 


## Introduction
This is my first data science project. After having a basic grasp of Pandas, NumPy and Matplotlib, which are indispensable tools for performing a variety of data science tasks with Python, I decided to do this project to further solidify my skills.

This project is mainly concerned with doing some elementary data analysis on the results of 74000 students from the National High School Exam in 2020 in Ho Chi Minh city, Vietnam.

## Technologies
- Programming Language: Python
- Tools: Python Pandas, Python Matplotlib

## Project Description

### Data Collection by Web Scraping ?

You can view an exam taker's results at 'diemthi.hcm.edu.vn' by entering his id number which has the format '020xxxxx' where xxxxx goes from 00001 to about 74719. To retrieve this data (in HTML form) and display it on a Python terminal, I used this command "curl -F "SoBaoDanh=your-id-number" diemthi.hcm.edu.vn/Home/Show". This will return a very nasty-looking, unreadable display of one's results. 

Knowing that around 75000 students took this exam in 2020, I created 'data_collection.py' to automate this data-fetching process. This file, when being run, essentially executes the above 'curl' command 75000 times with id numbers incrementing by 1 and stores everything in a variable before writing it to a txt file called 'raw_data.txt' (this file is very heavy (195MB) and thus cannot be stored on GitHub). 'raw_data.txt' contains all the raw-form results of each of those 75000 students, and each of the result line is in serious need of cleaning and processing.

### Data Cleaning and Processing

In my opinion I believe this is the most arduous part of this project :))

At first I tried to clean just the first line (result of first person) in 'raw_data.txt' to figure out the how a line should be cleaned and presented in such a human-readable way. There are a lot of HTML tags, weird characters and whitespaces that need to be removed, and also the names of students are in Vietnamese so I had to convert all the unicodes to their respective letters. I downloaded the Unicode conversion system from the internet and created 'unicode.py' to store it as a dictionary which can then be accessed easily. Finally, 'one_row_processing.py' was created to handle all of the above logic, for ONE LINE ONLY. Hence, 'data_processing.py' was created to do that for all the lines in 'raw_data.txt' and save everything in a nicely readable csv file, 'clean_data.csv' that could be used for our data analysis.

Upon reading the 'clean_data.csv' file in Jupyter Notebook and playing around with the data, I realised that some students have 00/00 as their birthday, which is totally invalid. Once again, I had to change these faulty birthdays to 01/01 (which does not influence the answers to our questions below), and convert the birthday column to datetime object to make the dates easier to work with.

### Data Analysis

In this section I used Python Pandas & Python Matplotlib in a Jupyter Notebook file to analyse and answer some questions about the results of 75000 students:

- For each subject, how many students took it? How many didn't ?
- How many subjects did a student usually take ?
- What is the average score of students categorised by the number of subjects they take; by their age?
- Is it true that average score decreases as age increases ?
- What are the 20 most popular first names and last names ?
- What is the longest name ?

To answer these questions I made use of many different pandas & matplotlib methods. They include:

- Adding columns and creating new DataFrame
- Using .iloc[] to filter data satisfying some conditions
- Using the .apply() method
- Using groupby to perform aggregate analysis
- Plotting bar charts and lines graphs to visualize our results
- Labeling our graphs

## Launch

You do not have to do anything. Just simply go to data_analysis folder and look at 'data_analysis.ipynb'
