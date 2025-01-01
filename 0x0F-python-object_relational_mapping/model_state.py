#!/usr/bin/python3
"""
Module that defines the State class for the MySQL table `states`.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for all models
Base = declarative_base()


class State(Base):
    """
    Represents a state in the MySQL database.

    Attributes:
        id (int): The state's unique ID. Primary key, auto-generated, not null.
        name (str): The state's name. String of max 128 characters, not null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
