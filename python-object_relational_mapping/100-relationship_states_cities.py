#!/usr/bin/python3
"""
This script creates the State "California" with
the City "San Francisco" in a database.
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

    # Create a new State object named "California"
    newState = State(name='California')

    # Create a new City object named "San Francisco"
    newCity = City(name='San Francisco')

    # Associate the city with the state (one-to-many relationship)
    newState.cities.append(newCity)

    # Add the state and city objects to the session
    session.add(newState)
    session.add(newCity)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
