INSERT INTO people (
    name,
    birth_year,
    eye_color,
    gender,
    hair_color,
    height,
    mass,
    skin_color,
    homeworld,
    films,
    species,
    starships,
    vehicles,
    url,
    created,
    edited
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);

INSERT INTO films (
    title,
    episode_id,
    opening_crawl,
    director,
    producer,
    release_date,
    species,
    starships,
    vehicles,
    characters,
    planets,
    url,
    created,
    edited
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);

INSERT INTO starships (
    name,
    model,
    starship_class,
    manufacturer,
    cost_in_credits,
    length,
    crew,
    passengers,
    max_atmosphering_speed,
    hyperdrive_rating,
    MGLT,
    cargo_capacity,
    consumables,
    films,
    pilots,
    url,
    created,
    edited
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);

INSERT INTO vehicles (
    name,
    model,
    vehicle_class,
    manufacturer,
    length,
    cost_in_credits,
    crew, passengers,
    max_atmosphering_speed,
    cargo_capacity,
    consumables,
    films,
    pilots,
    url,
    created,
    edited
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);

INSERT INTO species (
    name,
    classification,
    designation,
    average_height,
    average_lifespan,
    eye_colors,
    hair_colors,
    skin_colors,
    language,
    homeworld,
    people,
    films,
    url,
    created,
    edited
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);

INSERT INTO planets (
    name,
    diameter,
    rotation_period,
    orbital_period,
    gravity,
    population,
    climate,
    terrain,
    surface_water,
    residents,
    films,
    url,
    created,
    edited
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);