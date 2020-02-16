import csv
import yaml
config = yaml.load(open('config.yml'))

from utils.db_sqlite import get_db_connector


conn = get_db_connector()
cur = conn.cursor()


conn.execute(
    '''
    CREATE TABLE DATA
         (ID INT NOT NULL,
         TEXT TEXT NOT NULL,
         CLASS_ID INT NOT NULL,
         PRIMARY KEY (ID)
         );
    ''')


file_path = config["resource_dir"] + config["csv_file_name"]

with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    to_db = []
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {", ".join(row)}')

        else:
            sql = ''' INSERT INTO data(text,class_id)
                        VALUES(?,?) '''
            to_db.append(( line_count, row[0], row[2]))
        line_count += 1
cur.executemany("INSERT INTO data (id, text, class_id) VALUES (?, ?, ?);", to_db)
conn.commit()
conn.close()



