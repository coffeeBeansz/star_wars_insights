with open ('../tmp/test_cron.txt', 'a') as f:
    f.write('Hello, World!\n')

import requests
import pandas as pd
import os
from sqlalchemy import create_engine

with open ('../tmp/test_cron.txt', 'a') as f:
    f.write('ping!\n')

with open ('../tmp/test_cron.txt', 'a') as f:
    f.write('pong!\n')

def create_database_engine():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    with open ('../tmp/test_cron.txt', 'a') as f:
        f.write(f'{host} {port} {username} {password} {database}\n')

    connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    
    try: 
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        with open ('../tmp/test_cron.txt', 'a') as f:
            f.write(f"An error occurred: {e}\n")
        return None

with open ('../tmp/test_cron.txt', 'a') as f:
    f.write('ding!\n')

try:

    with open ('../tmp/test_cron.txt', 'a') as f:
        f.write('dong!\n')

    base_url = 'https://swapi.dev/api/'
    response = requests.get(base_url)

    if response.status_code != 200:
        raise Exception(response.status_code)

    endpoints = response.json()
    
    engine = create_database_engine()
    if engine is None:
        raise Exception("Database connection could not be established")

    for table_name, endpoint in endpoints.items():
        response = requests.get(endpoint)
        data = response.json()
        df = pd.DataFrame(data['results'])
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        with open ('../tmp/test_cron.txt', 'a') as f:
            f.write(f"Table {table_name} created successfully\n")

except Exception as e:
    with open ('../tmp/test_cron.txt', 'a') as f:
        f.write(f"An error occurred: {e}\n")