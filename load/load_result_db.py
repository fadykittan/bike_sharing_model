from load.load_result_base import LoadResultBase
from sqlalchemy import create_engine
import pandas as pd

class LoadResultDB(LoadResultBase):

    def __init__(self, config):
        self.config = config

    def save(self, result, file_name):
        # Database credentials
        dbname = "postgres"
        user = "postgres"
        password = 'mysecretpassword'
        host = 'localhost'
        port = 5432
        table_name = "out"

        # Create SQLAlchemy engine
        url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
        print(url)
        engine = create_engine(url)

        df = pd.DataFrame(result, columns=["count"])

        # Save to PostgreSQL table
        df.to_sql(table_name, engine, if_exists='append', index=False)