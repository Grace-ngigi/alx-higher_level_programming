#!/usr/bin/python3
"""print the first State object from db"""

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

    update_state = session.query(State).filter(State.id == 2).first()
    if update_state:
        update_state.name = "New mexico"
        session.commit()
    session.close()
