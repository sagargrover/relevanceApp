import yaml
import logging
import sqlite3


config = yaml.load(open('config.yml'))
error_logger = logging.getLogger('error_logger')


class SQLiteConnector:
    def __init__(self, sql_db):
        self.sql_db = sql_db

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.sql_db)
            return conn
        except sqlite3.Error as e:
            error_logger.exception(e)
            raise Exception
