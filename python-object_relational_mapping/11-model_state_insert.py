#!/usr/bin/python3
"""Add a new state."""

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

    # Create a new state instance
    newstate = State(name='Louisiana')

    # Add the new state to the session (not yet committed to the database)
    session.add(newstate)

    # Query the newly added state from the 'states' table
    state = session.query(State).filter_by(name='Louisiana').first()

    # Print the ID of the newly added state
    print(str(state.id))

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
