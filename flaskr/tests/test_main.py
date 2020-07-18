import os
import unittest

from config import TestingConfig
from flaskr import create_app
from flaskr.models import setup_db


class PlantTest(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client
        with self.app.app_context():
            # setup db for app
            setup_db(self.app)

    def tearDown(self):
        """Executed after reach test to close any opened thing"""
        pass

    def test_get_plant(self):
        """Test status code of get plant"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
