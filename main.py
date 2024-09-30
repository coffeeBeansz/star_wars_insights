import pandas as pd
from utils import create_database_engine
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    engine = create_database_engine()
    if engine is None:
        raise Exception("Database connection could not be established")
    
    query = 'SELECT title, episode_id FROM films'

    df = pd.read_sql(query, engine)

    for _, row in df.iterrows():
        print(f'The movie {row["title"]} has the episode id {row["episode_id"]}')


