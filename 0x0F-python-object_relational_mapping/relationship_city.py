#!/usr/bin/python3
"""
Defines a City class using SQLAlchemy ORM.
"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Represents a city in the database.
    """
    # Specify the table name
    __tablename__ = 'cities'
    # Define the id column
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Define the name column
    name = Column(String(128), nullable=False)
    # Define the state_id column
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
