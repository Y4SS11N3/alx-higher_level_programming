#!/usr/bin/python3
"""
Fetches states matching a user-provided string from a MySQL database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create a cursor object
    cur = db.cursor()
    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    # Fetch all the rows
    rows = cur.fetchall()
    # Print each row
    for row in rows:
        print(row)
    # Close the cursor and the database connection
    cur.close()
    db.close()
