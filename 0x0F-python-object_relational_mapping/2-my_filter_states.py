#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa where
the name matches the argument.
"""

# Import necessary modules
import MySQLdb
import sys

# Main function
if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cur = db.cursor()

    # Define the query
    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY states.id ASC"
    ).format(sys.argv[4])

    # Execute the query
    cur.execute(query)

    # Fetch all rows
    rows = cur.fetchall()

    # Check if any rows were returned
    if rows:
        # Print each row
        for row in rows:
            print(row)
    else:
        print("No states found with that name.")

    # Close cursor and database connection
    cur.close()
    db.close()
