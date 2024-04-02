#!/usr/bin/python3
"""
This script prints all City objects
from the database hbtn_0e_14_usa.
"""

# Import necessary modules
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create a database connection using provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State-City pairs where the state ID matches the city's state ID
    st_cty = session.query(State, City).filter(State.id == City.state_id).all()

    # Print each state and its associated city
    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
