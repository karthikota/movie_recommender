# Command-Line Movie Recommendation System

## Overview
A Python CLI tool that recommends movies based on your mood, retrieving data from a MySQL database.  
Perfect showcase of backend and SQL skills for SDE internships.

---

## Features
- User enters a mood at the terminal prompt.
- SQL database is queried for matching movie recommendations.
- Results are displayed in a neat table.

---

## Files

- `movie_cli.py` – Main Python script for the CLI app.
- `mysql_setup.sql` – SQL for quick database/table/data setup.
- `README.md` – This guide.

---

## Setup

### 1. MySQL Database

Open MySQL Workbench or terminal, and run:

Open MySQL Workbench or terminal, and execute all the SQL commands inside mysql_setup.sql.


Change MySQL root password if yours is not `YES`.

---

### 2. Python Environment

Required packages:
- mysql-connector-python
- tabulate

Install with:
pip install mysql-connector-python tabulate


---

### 3. Update Credentials

Edit `movie_cli.py` and set:
MYSQL_USER = "root"
MYSQL_PASS = "YOUR_MYSQL_PASSWORD"
MYSQL_DB = "movies_db"


---

## Usage

python movie_cli.py


When prompted, enter a mood (e.g., happy, intense, romantic, sad).

#### Example output:

Welcome to the Movie Recommendation CLI!
Enter your mood (e.g., happy, sad, romantic, intense): happy

Recommended Movies:
+-------------------+---------+--------+
| Title | Genre | Mood |
+-------------------+---------+--------+
| Forrest Gump | Comedy | happy |
| La La Land | Romance | happy |
+-------------------+---------+--------+


---

## Notes

- For production, you could easily add more moods, genres, or even wrap this with a GUI or web API.

---

## Author

Sriram Karthikeya Kota

