#!/usr/bin/python3
"""
Script to print the State object with the name passed as argument
using SQLAlchemy ORM (SQL injection free)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the database, queries for a specific State by name,
    and prints the state id or 'Not found'
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

    # Query for the State object with the specific name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Check if state exists and print accordingly
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
