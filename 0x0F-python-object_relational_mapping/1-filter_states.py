#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' (upper N)
from the database 'hbtn_0e_0_usa'.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Get a cursor
    cur = db.cursor()

    # Execute the query to get the states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Print the results
    for row in cur.fetchall():
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
