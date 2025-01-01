#!/usr/bin/python3
"""
Module that defines the State class for the MySql table `states`.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declaractive import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a state in the MySQL database.


    Attributes:
        id (int): The state's unique ID. Primary key, auto-generated\
                not null.
        name (str): The state's name. String of max 128 characters,\
                not null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
