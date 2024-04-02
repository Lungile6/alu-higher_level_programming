#!/usr/bin/python3
"""get a state."""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    # Create a database engine using the provided credentials
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))

    """
    Create the necessary database tables
    (if they don't exist) based on the defined models
    """
    Base.metadata.create_all(eng)

    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    """
    Query the state from the 'states' table
    where the name matches the user input
    """
    state = session.query(State).filter_by(name=argv[4]).first()

    # Print the state ID (if found) or "Not found"
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
