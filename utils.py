from sqlalchemy import create_engine
import os

def create_database_engine():
    # Port 5432 on the container is exposed to port 5432 on localhost (loopback ip address: 127.0.0.1)
    # 127.0.0.1:5432 means that we are listening to port 5432 on localhost (my machine)
    # to which the swapi_postgres container is 'connected', as is specified in the docker-compose file
    # under "port:""
    host = "127.0.0.1"
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
    