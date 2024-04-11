#!/usr/bin/python3
"""
Defines a State class using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Represents a state with an id and name.
    """
    # Specify the table name
    __tablename__ = 'states'
    # Define the id column
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Define the name column
    name = Column(String(128), nullable=False)
