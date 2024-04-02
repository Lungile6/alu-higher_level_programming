#!/usr/bin/python3
"""
This module contains the class definition of a State.
"""

# Import necessary modules
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create an instance of declarative_base with custom metadata
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class that defines each state.
    """
    __tablename__ = 'states'  # Name of the corresponding database table
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Unique identifier for each state
    name = Column(String(128), nullable=False)
    # State name (max length: 128 characters)
    cities = relationship("City", backref="states")
    # Relationship with City objects
