import os
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "prestige_worldwide"
database_path = "postgres://{}@{}/{}".format("jamesmiller", "localhost:5000", database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()

  migrate = Migrate(app, db)

class Movie(db.Model):
  __table__name = "movies"

  id = Column(Integer, primary_key=True)
  title = Column(String, default="Working Title")
  release_date = Column(String) #release_date = "2020/07/04"
  cast_filled = Column(Boolean, default=True)

  def __init__(self, title, release_date, cast_filled):
    self.title = title
    self.release_date = release_date
    self.cast_filled = cast_filled

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      "id": self.id,
      "title": self.title,
      "release_date": self.release_date,
      "cast_filled": self.cast_filled
    }

class Actor(db.Model):
  __tablename__ = "actors"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(Integer, nullable=False)
  gender = Column(String, nullable=True)
  seeking_role = Column(Boolean, default=True)

  def __init__(self, name, age, gender, seeking_role):
    self.name = name
    self.age = age
    self.gender = gender
    self.seeking_role = seeking_role

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      "id": self.id,
      "name": self.name,
      "age": self.age,
      "gender": self.gender,
      "seeking_role": self.seeking_role
    }

class MovieCast(db.Model):
  __tablename__ = "cast"
  id = Column(Integer, primary_key=True)
  movie_id = Column(Integer, ForeignKey('movie.id'))
  actor_id = Column(Integer, ForeignKey('actor.id'))