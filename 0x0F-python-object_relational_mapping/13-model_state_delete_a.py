#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the db.
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
            f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
            f'{db_name}', pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = (
            session.query(State)
            .filter(State.name.like('%a%')).all()
    )

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
