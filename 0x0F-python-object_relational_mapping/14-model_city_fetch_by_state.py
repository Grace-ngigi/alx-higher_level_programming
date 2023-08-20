#!/usr/bin/python3
"""print all city objects"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_city import City
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1],
                            sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(City, State)\
                    .filter(City.state_id)\
                    .order_by(City.id)

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
