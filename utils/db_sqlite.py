import yaml
import logging
import sqlite3


config = yaml.load(open('config.yml'))
error_logger = logging.getLogger('error_logger')


def get_db_connector():
    db_file = config["sql_db"]
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        error_logger.exception(e)
        raise Exception
