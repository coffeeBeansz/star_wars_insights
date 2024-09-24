import requests
import psycopg2
from psycopg2 import sql

# Have a look-see on the data from the API
# response = requests.get('https://swapi.dev/api/people/')
# data = response.json()
# print(len(data['results']))

# Database connection parameters
host = "localhost"
port = "5432"
user = "user"
password = "password"
db_name = "star_wars_db"

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    dbname=db_name
)

try:
    cursor = connection.cursor()

    # Fetch data from SWAPI
    response = requests.get('https://swapi.dev/api/people/')
    people_data = response.json()

    # Insert data into the people table
    for person in people_data['results']:
        insert_people_query = '''
        INSERT INTO people (name, birth_year, eye_color, gender, hair_color, height, mass, skin_color, homeworld, films, species, starships, vehicles, url, created, edited)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        # Prepare values
        values = (
            person['name'],
            person['birth_year'],
            person['eye_color'],
            person['gender'],
            person['hair_color'],
            person['height'],
            person['mass'],
            person['skin_color'],
            person['homeworld'],
            person['films'],
            person['species'],
            person['starships'],
            person['vehicles'],
            person['url'],
            person['created'],
            person['edited']
        )

        # Execute insert query
        cursor.execute(insert_people_query, values)

    # Commit the transaction
    connection.commit()
    print("Data inserted successfully!")

    # Fetch data for films
    for person in people_data['results']:
        for film_url in person['films']:
            film_response = requests.get(film_url)
            film_data = film_response.json()

            insert_films_query = '''
            INSERT INTO films (title, episode_id, opening_crawl, director, producer, release_date, species, starships, vehicles, characters, planets, url, created, edited)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            film_values = (
                film_data['title'],
                film_data['episode_id'],
                film_data['opening_crawl'],
                film_data['director'],
                film_data['producer'],
                film_data['release_date'],
                film_data['species'],
                film_data['starships'],
                film_data['vehicles'],
                film_data['characters'],
                film_data['planets'],
                film_data['url'],
                film_data['created'],
                film_data['edited']
            )
            cursor.execute(insert_films_query, film_values)

    # Commit the transaction for films
    connection.commit()
    print("Films data inserted successfully!")

    # Fetch and insert data for starships
    starships_response = requests.get('https://swapi.dev/api/starships/')
    starships_data = starships_response.json()

    for starship in starships_data['results']:
        insert_starships_query = '''
        INSERT INTO starships (name, model, starship_class, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, films, pilots, url, created, edited)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        starship_values = (
            starship['name'],
            starship['model'],
            starship['starship_class'],
            starship['manufacturer'],
            starship['cost_in_credits'],
            starship['length'],
            starship['crew'],
            starship['passengers'],
            starship['max_atmosphering_speed'],
            starship['hyperdrive_rating'],
            starship['MGLT'],
            starship['cargo_capacity'],
            starship['consumables'],
            starship['films'],
            starship['pilots'],
            starship['url'],
            starship['created'],
            starship['edited']
        )
        cursor.execute(insert_starships_query, starship_values)

    # Commit the transaction for starships
    connection.commit()
    print("Starships data inserted successfully!")

    # Fetch and insert data for vehicles
    vehicles_response = requests.get('https://swapi.dev/api/vehicles/')
    vehicles_data = vehicles_response.json()

    for vehicle in vehicles_data['results']:
        insert_vehicles_query = '''
        INSERT INTO vehicles (name, model, vehicle_class, manufacturer, length, cost_in_credits, crew, passengers, max_atmosphering_speed, cargo_capacity, consumables, films, pilots, url, created, edited)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        vehicle_values = (
            vehicle['name'],
            vehicle['model'],
            vehicle['vehicle_class'],
            vehicle['manufacturer'],
            vehicle['length'],
            vehicle['cost_in_credits'],
            vehicle['crew'],
            vehicle['passengers'],
            vehicle['max_atmosphering_speed'],
            vehicle['cargo_capacity'],
            vehicle['consumables'],
            vehicle['films'],
            vehicle['pilots'],
            vehicle['url'],
            vehicle['created'],
            vehicle['edited']
        )
        cursor.execute(insert_vehicles_query, vehicle_values)

    # Commit the transaction for vehicles
    connection.commit()
    print("Vehicles data inserted successfully!")

    # Fetch and insert data for species
    species_response = requests.get('https://swapi.dev/api/species/')
    species_data = species_response.json()

    for species in species_data['results']:
        insert_species_query = '''
        INSERT INTO species (name, classification, designation, average_height, average_lifespan, eye_colors, hair_colors, skin_colors, language, homeworld, people, films, url, created, edited)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        species_values = (
            species['name'],
            species['classification'],
            species['designation'],
            species['average_height'],
            species['average_lifespan'],
            species['eye_colors'],
            species['hair_colors'],
            species['skin_colors'],
            species['language'],
            species['homeworld'],
            species['people'],
            species['films'],
            species['url'],
            species['created'],
            species['edited']
        )
        cursor.execute(insert_species_query, species_values)

    # Commit the transaction for species
    connection.commit()
    print("Species data inserted successfully!")

    # Fetch and insert data for planets
    planets_response = requests.get('https://swapi.dev/api/planets/')
    planets_data = planets_response.json()

    for planet in planets_data['results']:
        insert_planets_query = '''
        INSERT INTO planets (name, diameter, rotation_period, orbital_period, gravity, population, climate, terrain, surface_water, residents, films, url, created, edited)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        planet_values = (
            planet['name'],
            planet['diameter'],
            planet['rotation_period'],
            planet['orbital_period'],
            planet['gravity'],
            planet['population'],
            planet['climate'],
            planet['terrain'],
            planet['surface_water'],
            planet['residents'],
            planet['films'],
            planet['url'],
            planet['created'],
            planet['edited']
        )
        cursor.execute(insert_planets_query, planet_values)

    # Commit the transaction for planets
    connection.commit()
    print("Planets data inserted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
