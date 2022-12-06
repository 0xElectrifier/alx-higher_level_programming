#!/usr/bin/python3
"""Script that lists all states from the database `hbtn_0e_0_usa`"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = sys.argv
    db = MySQLdb.connect(host='127.0.0.1', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
