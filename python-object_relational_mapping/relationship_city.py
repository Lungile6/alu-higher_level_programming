#!/usr/bin/python3
"""
This module contains the class definition of a City.
"""

# Import necessary modules
from relationship_state import Base
# Assuming relationship_state contains the Base class
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city.
    """
    __tablename__ = 'cities'  # Name of the corresponding database table
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    # City name (max length: 128 characters)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # Foreign key referencing the State table
