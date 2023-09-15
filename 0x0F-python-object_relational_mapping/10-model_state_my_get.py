#!/usr/bin/python3
"""Script that prints the State
object with the given name from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == state_name).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()
