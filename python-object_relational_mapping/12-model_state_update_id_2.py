#!/usr/bin/python3
"""
This script updates a state in the database.
"""

# Import necessary modules
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
# Assuming model_state contains the State class

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

    # Query the State table for the state with ID 2
    state = session.query(State).filter_by(id=2).first()

    # Update the name of the state to "New Mexico"
    state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
