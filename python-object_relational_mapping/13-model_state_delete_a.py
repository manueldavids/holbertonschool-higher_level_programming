#!/usr/bin/python3
"""
Script to delete all State objects with a name containing 'a'.
Uses SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the database, finds all State objects whose name contains 'a',
    deletes them, and commits the changes
    """
    # Create engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects whose name contains 'a'
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
