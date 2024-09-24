import pandas as pd
import psycopg2
from psycopg2 import sql

# Import people form the database
# Database connection parameters
host = "localhost"
port = "5432"
user = "user"
password = "password"
db_name = "star_wars_db"

def get_data(query):

    data = None

    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=db_name
        )

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
    query = '''SELECT name FROM people'''
    names = get_data(query)

    for name in names:
        print(name[0])
    
    # # Get all episode_id whwere the name is 'Luke Skywalker'
    # query = '''SELECT episode_id FROM people WHERE name = 'Luke Skywalker' '''
    # episode_ids = get_data(query)

    # for episode_id in episode_ids:
    #     print(episode_id[0])