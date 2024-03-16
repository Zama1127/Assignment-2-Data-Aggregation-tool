import sqlite3
import csv
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests

# Connect to the SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Function to insert data from CSV into SQLite database
def insert_data_from_csv(csv_file_path):
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Insert data into SQLite database using parameterized query
                c.execute("INSERT INTO table_name (column1, column2, ...) VALUES (?, ?, ...)", (row['column1'], row['column2'], ...))
            conn.commit()
            print("Data inserted successfully from CSV.")
    except FileNotFoundError:
        print(f"File '{csv_file_path}' does not exist.")
    except Exception as e:
        print(f"Error inserting data from CSV: {e}")

# Function to insert data from HTML into SQLite database
def insert_data_from_html(html_file_path):
    try:
        with open(html_file_path, 'r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            # Extract data from HTML and insert into SQLite database
            # Replace this logic with your specific data extraction and insertion code
            for data in soup.find_all('div', class_='data'):
                value = data.text.strip()
                c.execute("INSERT INTO table_name (column) VALUES (?)", (value,))
            conn.commit()
            print("Data inserted successfully from HTML.")
    except FileNotFoundError:
        print(f"File '{html_file_path}' does not exist.")
    except Exception as e:
        print(f"Error inserting data from HTML: {e}")

# Function to insert data from XML into SQLite database
def insert_data_from_xml(xml_file_path):
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        # Extract data from XML and insert into SQLite database
        # Replace this logic with your specific data extraction and insertion code
        for child in root:
            value = child.text.strip()
            c.execute("INSERT INTO table_name (column) VALUES (?)", (value,))
        conn.commit()
        print("Data inserted successfully from XML.")
    except FileNotFoundError:
        print(f"File '{xml_file_path}' does not exist.")
    except Exception as e:
        print(f"Error inserting data from XML: {e}")

# Function to insert data from JSON into SQLite database
def insert_data_from_json(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            # Extract data from JSON and insert into SQLite database
            # Replace this logic with your specific data extraction and insertion code
            for item in data:
                value = item['key']
                c.execute("INSERT INTO table_name (column) VALUES (?)", (value,))
            conn.commit()
            print("Data inserted successfully from JSON.")
    except FileNotFoundError:
        print(f"File '{json_file_path}' does not exist.")
    except Exception as e:
        print(f"Error inserting data from JSON: {e}")

# Example usage:
csv_file_path = 'voting_stats.csv'
html_file_path = 'voting_stats.html'
xml_file_path = 'voting_stats.xml'
json_file_path = 'voting.stats.json'
xlsx_file_path = 'voting_stats.xlsx'

insert_data_from_csv(csv_file_path)
insert_data_from_html(html_file_path)
insert_data_from_xml(xml_file_path)
insert_data_from_json(json_file_path)

# Close the database connection
conn.close()
