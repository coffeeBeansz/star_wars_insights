import psycopg2
from psycopg2 import sql

# Database connection parameters
host = "localhost"
port = "5432"
user = "user"
password = "password"
db_name = "star_wars_db"

try:
    # Create an empty database
    connection = psycopg2.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        dbname = 'postgres'
    )

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
    connection = psycopg2.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        dbname = db_name
    )

    cursor = connection.cursor()
    print("Connected to the database")

    create_poeple_table_query = '''
    CREATE TABLE IF NOT EXISTS people (
        id SERIAL PRIMARY KEY,
        name TEXT,
        birth_year TEXT,
        eye_color TEXT,
        gender TEXT,
        hair_color TEXT,
        height TEXT,
        mass TEXT,
        skin_color TEXT,
        homeworld TEXT,
        films TEXT[],
        species TEXT[],
        starships TEXT[],
        vehicles TEXT[],
        url TEXT,
        created TIMESTAMP WITH TIME ZONE,
        edited TIMESTAMP WITH TIME ZONE
    );
    '''
    cursor.execute(create_poeple_table_query)

    create_films_table_query = '''
    CREATE TABLE IF NOT EXISTS films (
        id SERIAL PRIMARY KEY,
        title TEXT,
        episode_id INTEGER,
        opening_crawl TEXT,
        director TEXT,
        producer TEXT,
        release_date DATE,
        species TEXT[],
        starships TEXT[],
        vehicles TEXT[],
        characters TEXT[],
        planets TEXT[],
        url TEXT,
        created TIMESTAMP WITH TIME ZONE,
        edited TIMESTAMP WITH TIME ZONE
    );
    '''
    cursor.execute(create_films_table_query)

    create_starships_table_query = '''
    CREATE TABLE IF NOT EXISTS starships (
        id SERIAL PRIMARY KEY,
        name TEXT,
        model TEXT,
        starship_class TEXT,
        manufacturer TEXT,
        cost_in_credits TEXT,
        length TEXT,
        crew TEXT,
        passengers TEXT,
        max_atmosphering_speed TEXT,
        hyperdrive_rating TEXT,
        MGLT TEXT,
        cargo_capacity TEXT,
        consumables TEXT,
        films TEXT[],
        pilots TEXT[],
        url TEXT,
        created TIMESTAMP WITH TIME ZONE,
        edited TIMESTAMP WITH TIME ZONE
    );
    '''
    cursor.execute(create_starships_table_query)

    create_vehicles_table_query = '''
    CREATE TABLE IF NOT EXISTS vehicles (
        id SERIAL PRIMARY KEY,
        name TEXT,
        model TEXT,
        vehicle_class TEXT,
        manufacturer TEXT,
        length TEXT,
        cost_in_credits TEXT,
        crew TEXT,
        passengers TEXT,
        max_atmosphering_speed TEXT,
        cargo_capacity TEXT,
        consumables TEXT,
        films TEXT[],
        pilots TEXT[],
        url TEXT,
        created TIMESTAMP WITH TIME ZONE,
        edited TIMESTAMP WITH TIME ZONE
    );
    '''
    cursor.execute(create_vehicles_table_query)

    create_species_table_query = '''
    CREATE TABLE IF NOT EXISTS species (
        id SERIAL PRIMARY KEY,
        name TEXT,
        classification TEXT,
        designation TEXT,
        average_height TEXT,
        average_lifespan TEXT,
        eye_colors TEXT,
        hair_colors TEXT,
        skin_colors TEXT,
        language TEXT,
        homeworld TEXT,
        people TEXT[],
        films TEXT[],
        url TEXT,
        created TIMESTAMP WITH TIME ZONE,
        edited TIMESTAMP WITH TIME ZONE
    );
    '''
    cursor.execute(create_species_table_query)

    create_planets_table_query = '''
    CREATE TABLE IF NOT EXISTS planets (
        id SERIAL PRIMARY KEY,
        name TEXT,
        diameter TEXT,
        rotation_period TEXT,
        orbital_period TEXT,
        gravity TEXT,
        population TEXT,
        climate TEXT,
        terrain TEXT,
        surface_water TEXT,
        residents TEXT[],
        films TEXT[],
        url TEXT,
        created TIMESTAMP WITH TIME ZONE,
        edited TIMESTAMP WITH TIME ZONE
    );
    '''
    cursor.execute(create_planets_table_query)
    
    connection.commit()

except Exception as e:
    print(f'An error occured: {e}')

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()