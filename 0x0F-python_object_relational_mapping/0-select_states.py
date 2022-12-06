#!/usr/bin/python3
import MySQLdb
import sys


"""Script that lists all states from the database `hbtn_0e_0_usa`"""
if __name__ == '__main__':
    argv = sys.argv
    db = MySQL.connect(host='127.0.0.1:3306', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
