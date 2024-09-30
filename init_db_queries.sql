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