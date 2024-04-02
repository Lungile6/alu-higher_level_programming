#!/usr/bin/python3
"""
This script deletes states from the database
where the state name contains the letter 'a'.
"""

# Import necessary modules
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    # Create a database connection using provided credentials
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))

    # Create tables if they don't exist
    Base.metadata.create_all(eng)

    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query states where the name contains the letter 'a'
    states = session.query(State).filter(State.name.like('%a%'))

    # Delete each matching state
    for state in states:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
