import pandas as pd
import sqlite3
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET

# Read data from CSV file and convert to DataFrame
def read_csv_to_df(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df

# Read data from HTML file and convert to DataFrame
def read_html_to_df(html_file_path):
    with open(html_file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]
    return df

# Read data from XML file and convert to DataFrame
def read_xml_to_df(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    data = []
    for child in root:
        data.append(child.attrib)
    df = pd.DataFrame(data)
    return df

# Read data from JSON file and convert to DataFrame
def read_json_to_df(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    return df

# Connect to SQLite database
conn = sqlite3.connect('data_aggregation.db')
cursor = conn.cursor()

# Create tables in SQLite database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS csv_data (
        id INTEGER PRIMARY KEY,
        col1 TEXT,
        col2 TEXT,
        col3 TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS html_data (
        id INTEGER PRIMARY KEY,
        col1 TEXT,
        col2 TEXT,
        col3 TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS xml_data (
        id INTEGER PRIMARY KEY,
        col1 TEXT,
        col2 TEXT,
        col3 TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS json_data (
        id INTEGER PRIMARY KEY,
        col1 TEXT,
        col2 TEXT,
        col3 TEXT
    )
''')

# Read data from files and insert into SQLite database
csv_df = read_csv_to_df('voting_stats.csv')
csv_df.to_sql('csv_data', conn, if_exists='replace', index=False)

html_df = read_html_to_df('voting_stats.html')
html_df.to_sql('html_data', conn, if_exists='replace', index=False)

xml_df = read_xml_to_df('voting_stats.xml')
xml_df.to_sql('xml_data', conn, if_exists='replace', index=False)

json_df = read_json_to_df('voting.stats.json')
json_df.to_sql('json_data', conn, if_exists='replace', index=False)

# Commit changes and close connection
conn.commit()
conn.close()