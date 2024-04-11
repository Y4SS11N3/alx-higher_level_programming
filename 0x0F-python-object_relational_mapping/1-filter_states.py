#!/usr/bin/python3

"""Fetch 'N'-prefixed state rows from MySQL DB"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id"
    )
    print('\n'.join(map(str, cur.fetchall())))
    cur.close()
    db.close()
