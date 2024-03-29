#!/usr/bin/python3
"""Script that deletes all State objects with
a name containing 'a' from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
