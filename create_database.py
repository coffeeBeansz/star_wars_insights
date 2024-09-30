import requests
from utils import create_database_engine
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

try:
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
        print(f"Table {table_name} created successfully")

except Exception as e:
    print(f"An error occurred: {e}")