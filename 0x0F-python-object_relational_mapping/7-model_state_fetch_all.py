#!/usr/bin/python3
"""
Lists all State objects from the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, db_name
        ),
        pool_pre_ping=True,
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
