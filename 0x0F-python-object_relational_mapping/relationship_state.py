#!/usr/bin/python3
"""
Defines a State class using SQLAlchemy ORM,
with a relationship to the City class.
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Represents a state in the database.
    """
    # Specify the table name
    __tablename__ = 'states'
    # Define the id column
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Define the name column
    name = Column(String(128), nullable=False)
    # Define the relationship to the City class
    cities = relationship("City", backref="states")
