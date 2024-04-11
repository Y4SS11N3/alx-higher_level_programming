#!/usr/bin/python3
"""
Creates the State "California"
with the City "San Francisco" in a MySQL database.
"""

# Import necessary modules
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Main execution
if __name__ == '__main__':
    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create all tables in the engine
    Base.metadata.create_all(engine)
    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create a new State object
    newState = State(name='California')
    # Create a new City object
    newCity = City(name='San Francisco')
    # Add the new City to the new State's cities
    newState.cities.append(newCity)
    # Add the new State and City to the session
    session.add(newState)
    session.add(newCity)
    # Commit the session to write the new State and City to the database
    session.commit()
