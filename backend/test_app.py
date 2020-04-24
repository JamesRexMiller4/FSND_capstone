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
    setup_db(self.app, self.database_path)

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

  def test_get_cast_members(self):
    res = self.client().get('/casts')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["casts"])

  def test_post_movie(self):
    res = self.client().post('/movies', json={"title": "Soul", "release_date": "2020/06/19", "cast_filled": True})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["id"])
    self.assertEqual(data["title"], 'Soul')
    self.assertEqual(data["release_date"], '2020/06/19')
    self.assertEqual(data["cast_filled"], True)

  def test_post_actor(self):
    res = self.client().post('/actors', json={"name": "John Goodman", "age": 67, "gender": 'Male', "seeking_role": True})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["id"])
    self.assertEqual(data["name"], 'John Goodman')
    self.assertEqual(data["age"], 67)
    self.assertEqual(data["gender"], 'Male')
    self.assertEqual(data["seeking_role"], True)

  def test_post_cast(self):
    res = self.client().post('/casts', json={"movie_id": 5, "actor_id": 29})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["id"])
    self.assertEqual(data["movie_id"], 5)
    self.assertEqual(data["actor_id"], 29)

  def test_delete_movie(self):
    res = self.client().delete('/movies/4')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertEqual(data["deleted"], 4)

  def test_delete_actors(self):
    res = self.client().delete('/actors/27')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertEqual(data["deleted"], 27)

  def test_delete_cast_member(self):
    res = self.client().delete('/casts/22')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertEqual(data["deleted"], 22)

  def test_patch_movie(self):
    res = self.client().patch('/movies/5', json={"release_date": "2042/04/19"})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertEqual(data["id"], 5)

  def test_patch_actor(self):
    res = self.client().patch('/actors/29', json={"seeking_role": False})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertEqual(data["id"], 29)

  def test_404_get_movies_error(self):
    res = self.client().get('/movieesss')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 404)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Resource not found.")

  def test_404_get_actors_error(self):
    res = self.client().get('/factors')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 404)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Resource not found.")

  def test_422_post_movie_error(self):
    res = self.client().post('/movies', json={"title": "Bill and Ted's Biggest Adventure Yet", "release_date": "Space === Time", "cast_filled": "Maybe" })
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 422)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Request cannot be processed.")
  
  def test_422_post_actor_error(self):
    res = self.client().post('/actors', json={"name": "Pete", "age": "42", "gender": "Male", "seeking_role": "Maybe" })
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 422)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Request cannot be processed.")

  def test_422_post_cast_member_error(self):
    res = self.client().post('/casts', json={"movie": "4", "actor_1": "42"})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 422)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Request cannot be processed.")

  def test_404_delete_movie_error(self):
    res = self.client().delete('/movies/999999')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 404)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Resource not found.")

  def test_404_delete_actor_error(self):
    res = self.client().delete('/actors/999999')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 404)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Resource not found.")

  def test_404_delete_cast_member_error(self):
    res = self.client().delete('/casts/999999')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 404)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Resource not found.")

  def test_422_patch_movie_error(self):
    res = self.client().patch('/movies/1', json={"spaghetti": "2021/04/19"})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 422)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Request cannot be processed.")

  def test_422_patch_actor_error(self):
    res = self.client().patch('/actors/4', json={"password": "SuperStrongPassword123"})
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 422)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "Request cannot be processed.")
  