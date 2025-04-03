from extract.extract_base import ExtractBase
import psycopg2
import pandas as pd

class ExtractDB(ExtractBase):

    def __init__(self, config):
        self.config = config

    def load_data(self, config):
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5432"
        )

        df = pd.read_sql('SELECT * FROM "in";', conn)
        print(df)
        conn.close()
        return df
