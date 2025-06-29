#!/usr/bin/python3
"""
Script to update a State object's name in the database using SQLAlchemy ORM
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the database, finds the State with id = 2,
    updates its name to 'New Mexico', and commits the change
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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if the state exists before updating
    if state_to_update:
        # Update the name to 'New Mexico'
        state_to_update.name = 'New Mexico'
        # Commit the changes to the database
        session.commit()
    else:
        print("State with id = 2 not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
