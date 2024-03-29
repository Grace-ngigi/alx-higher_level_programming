#!/usr/bin/python3
"""lists all state objects"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1],
                            sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
