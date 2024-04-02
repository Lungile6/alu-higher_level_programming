#!/usr/bin/python3
"""
This script lists all City objects
from the database hbtn_0e_101_usa.
"""

# Import necessary modules
import sys
from relationship_state import Base
# Assuming relationship_state contains the Base class
from relationship_city import City
# Assuming relationship_city contains the City class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create a database connection using provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create necessary tables (if they don't exist)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query all State objects along with their associated
    City objects (using an inner join)
    """
    st = session.query(State).join(City).order_by(City.id).all()

    # Print each city's ID, name, and the corresponding state's name
    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

    # Close the session
    session.close()
