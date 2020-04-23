import os
import unittest2
import json
import app
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movie, Actor, CastMember

class CastingAgencyTestCase(unittest2.TestCase):
  def setUp(self):
    self.app = create_app()
    self.client= self.app.test_client
    self.database_name = 'prestige_worldwide_test'
    self.database_path = 'postgres://{}@{}/{}'.format("jamesmiller", "localhost:5432", self.database_name)

    setup_db(self.app, self.database_path)

    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)
      self.db.create_all()

  def teardown(self):
    pass