#!/usr/bin/python3
"""lists all states from the database hbtn_oe_o_usa"""

if __name__ == "__main__":
    import MYSQLdb
    import sys

    db = MYSQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
