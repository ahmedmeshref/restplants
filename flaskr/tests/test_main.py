import os
import unittest

from config import TestingConfig
from flaskr import create_app
from flaskr.models import setup_db, db


class PlantTest(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            # setup db for app
            setup_db(self.app)
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """Executed after reach test to close any opened thing"""
        pass

    def test_home(self):
        """Test status code of get plant"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_plants(self):
        response = self.client.get("/plants/1")
        self.assertEqual(response.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
