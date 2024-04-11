#!/usr/bin/python3
"""
Lists all states and their cities from a MySQL database.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

# Main execution
if __name__ == "__main__":
    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create all tables in the engine
    Base.metadata.create_all(engine)
    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query all states, ordered by id, and their cities
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
