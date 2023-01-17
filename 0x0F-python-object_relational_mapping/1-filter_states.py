#!/usr/bin/python3
"""Script that lists all `states` with a `name` starting with `N` from
a database"""
import sys
import MySQLdb

if __name__ == '__main__':
    argv = sys.argv
    conn = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    conn.close()
