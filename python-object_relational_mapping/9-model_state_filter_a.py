#!/usr/bin/python3
"""Contains letter"""

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

    # Define a search pattern for state names (contains the letter 'a')
    s = '%a%'

    """
    Query states from the 'states'
    table where the name contains the letter 'a'
    """
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)

    # Print the ID and name of each matching state
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
