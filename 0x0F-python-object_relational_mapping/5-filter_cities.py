#!/usr/bin/python3
"""Secho 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev
HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    if len(argv) != 5:
        exit()
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute('SELECT cities.name FROM states\
                INNER JOIN cities ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id', (argv[4],))
    query_rows = cur.fetchall()
    a=0
    print(", ".join([row[0] for row in query_rows]))

    cur.close()
    conn.close()
