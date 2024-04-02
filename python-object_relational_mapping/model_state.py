#!/usr/bin/python3
"""firrst state model"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()


class State(Base):
    """Class representing a state"""
    __tablename__ = 'states'  # Name of the database table

    # Define columns for the 'states' table
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String(128), nullable=False)
    # State name column (not nullable)
