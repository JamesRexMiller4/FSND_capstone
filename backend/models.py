import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "prestige_worldwide"
database_path = "postgres://{}@{}/{}".format("jamesmiller", "localhost:5000", database_name)

def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()


class Movies(db.Model):
  __table__name = "movies"

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(String)
  actors = Column(String)

  def __init__(self, title, release_date, actors):
    self.title = title
    self.release_date = release_date
    self.actors = actors

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
      "actors": self.actors
    }