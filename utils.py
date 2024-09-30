from sqlalchemy import create_engine
import os

def create_database_engine():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    
    try: 
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    