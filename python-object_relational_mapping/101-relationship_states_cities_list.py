#!/usr/bin/python3
"""
This script lists all State objects and
their corresponding City objects contained in the database.
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
    Query all State objects along with
    their associated City objects (outer join)
    """
    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    # Print each state and its corresponding cities
    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Close the session
    session.close()
