import requests
import psycopg2
from psycopg2 import sql
from utils import create_db_connection, insert_data_into_table, get_queries
from dotenv import load_dotenv
import os
import json

# Database connection parameters
load_dotenv()
db_name = os.getenv('DB_NAME')


try:
    connection = create_db_connection(db_name)
    cursor = connection.cursor()

    with open('fill_db_endpoints.json', 'r') as file:
        endpoints = json.load(file)['endpoints']
    
    with open('table_formats.json', 'r') as file:
        table_formats = json.load(file).values()

    queries = get_queries('fill_db_queries.sql')

    for query, endpoint, table_format in zip(queries, endpoints, table_formats):
        response = requests.get(endpoint)
        data = response.json()['results']
        insert_data_into_table(cursor, query, data, table_format)
    
    connection.commit()
    print("Data inserted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
