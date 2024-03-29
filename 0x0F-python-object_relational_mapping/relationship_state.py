#!/usr/bin/python3
""" class definition of a State"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """define a table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
