#libraries
import pandas as pd


#local imports
from utils.db_sqlite import SQLiteConnector
from exceptions.exception import DatabaseNotFound


class InputPipeline:
    def __init__(self):
        pass

    def get_data_in_df(self, db_type, db_name, table_name=None):
        if db_type.lower() == "sqlite":
            conn = SQLiteConnector(db_name).get_connection()
            df = pd.read_sql_query("SELECT * FROM " + table_name, conn)
            return df
        else:
            raise DatabaseNotFound

