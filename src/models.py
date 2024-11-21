import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    eye_color = Column(String(50), nullable=False)
    
    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    climate = Column(String(50), nullable=False)   

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id")) 
    user = relationship(User)      
    planet_id = Column(Integer, ForeignKey("planet.id")) 
    planet = relationship(Planet) 
    character_id = Column(Integer, ForeignKey("character.id")) 
    character = relationship(Character)         

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
