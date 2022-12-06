#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the 'states'
table of 'hbtn_0e_0_usa' where 'name' matches the argument
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)

    cur.close()
    conn.close()
