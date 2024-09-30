import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
from utils import get_queries, create_db_connection

# Database connection parameters
load_dotenv()
db_name = os.getenv('DB_NAME')

try:
    # Create an empty database
    connection = create_db_connection('postgres')
    connection.autocommit = True
    cursor = connection.cursor()

    try:
        cursor.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(db_name)))
        print(f"Database '{db_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


    # Create the tables inside the database
    connection = create_db_connection(db_name)
    cursor = connection.cursor()

    queries = get_queries('init_db_queries.sql')
    n_tables = len(queries)
    
    for i, query in enumerate(queries):
        cursor.execute(query)
        print(f'Table {i+1}/{n_tables} created successfully')
    
    connection.commit()

except Exception as e:
    print(f'An error occured: {e}')

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()