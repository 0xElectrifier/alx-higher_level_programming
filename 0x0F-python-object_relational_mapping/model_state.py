#!/usr/bin/python
"""Implements ORM through the SQLAlchemy
Contains the class definition of a 'State' and an instance Base"""
from mysqlalchemy.ext.declarative import declarative_base
from mysqlalchemy import Column, Integer

Base = declarative_base()
class State(Base):
    """Defines a 'State' instance"""
    __tablename__ = 'states'
    id = Column(
