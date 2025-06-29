#!/usr/bin/python3
"""
Script to print the first State object from the database using SQLAlchemy ORM
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the database, queries the first State object, and prints it
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

    # Query the first State object (lowest id)
    first_state = session.query(State).order_by(State.id).first()

    # Check if any state exists and print accordingly
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
