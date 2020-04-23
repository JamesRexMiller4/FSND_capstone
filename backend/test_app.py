import os
import unittest2
import json
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movie, Actor, CastMember

class CastingAgencyTestCase(unittest2.TestCase):
  def setUp(self):
    self.app = create_app()
    self.client= self.app.test_client
    self.database_name = 'prestige_worldwide_test'
    self.database_path = 'postgres://{}@{}/{}'.format("jamesmiller", "localhost:5432", self.database_name)

    setup_db(self.app)

    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)
      self.db.create_all()

  def teardown(self):
    pass

  def test_get_movies(self):
    res = self.client().get("/movies")
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["movies"])

  def test_get_actors(self):
    res = self.client().get("/actors")
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["actors"])