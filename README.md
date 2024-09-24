# star_wars_insights
Graduate project 2 - Data driven

1. Install docker

2. Run in terminal:
```bash
docker pull postgres
```

3. Clone repository:
```bash
git clone https://github.com/coffeeBeansz/star_wars_insights.git
```

4. cd to repo

5. Run in terminal:
```bash
docker-compose up -d
```

5. Create empty database:
```bash
init_db.py
```

6. Fill database with data from swapi
```bash
fill_db.py
```

7. Open main.py where you can write querys and extract the data of your choosing.