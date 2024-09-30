import pandas as pd
import psycopg2
from psycopg2 import sql
import requests
from utils import create_db_connection
from dotenv import load_dotenv
import os

# Import people form the database
# Database connection parameters
load_dotenv()
db_name = os.getenv('DB_NAME')

def get_data(query):

    data = None

    try:
        # Connect to the PostgreSQL database
        connection = create_db_connection(db_name)
        cursor = connection.cursor()

        cursor.execute(query)
        data = cursor.fetchall()
        

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
    return data

if __name__ == '__main__':
    query = '''SELECT title, episode_id FROM films'''
    retreived_data = get_data(query)

    print(type(retreived_data))
    print(retreived_data)

    for name, episode_id in retreived_data:
        print(f'The movie {name} has the episode id {episode_id}')
    
    # base_url = 'https://swapi.dev/api/'
    # response = requests.get(base_url)
    # endpoints = response.json()
    # print(endpoints)

    # endpoint = base_url + 'planets/schema/'
    # response = requests.get(endpoint)
    # schema = response.json()
    # print(schema)
    # for name, endpoint in content_endpoints.items():
    #     url = endpoint + 'schema/'
    #     print(url)
    #     response = requests.get(url)
    #     schema = response.json()
    #     print(schema)
    #     break