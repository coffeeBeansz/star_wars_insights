import os
import psycopg2
import json

def get_queries(queries_file):
    with open(queries_file, 'r') as file:
        queires = file.read()

    queries = queires.split(';')
    queries = [query.strip() for query in queries if query.strip() != '']
    return queries

def create_db_connection(db_name):
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    
    connection = psycopg2.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        dbname = db_name
    )
    return connection

def insert_data_into_table(cursor, query, data, table_format):
    for item in data:
        values = prepare_item_for_inserting_into_table(item, table_format)
        cursor.execute(query, values)

def prepare_item_for_inserting_into_table(item, table_format):
    values = ()
    for key in table_format:
        values += (item[key],)
    return values
