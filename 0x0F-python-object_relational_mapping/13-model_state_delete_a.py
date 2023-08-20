#!/usr/bin/python3
"""delete State object from db"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    del_states = session.query(State).filter(State.name.like('%a%'))
    for state in del_states:
        session.delete(state)
    session.commit()
    session.close()
