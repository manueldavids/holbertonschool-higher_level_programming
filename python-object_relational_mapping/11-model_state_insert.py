#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database using SQLAlchemy ORM
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the database, creates a new State object "Louisiana",
    adds it to the database, and prints the new state's id
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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the transaction to save the new state to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
