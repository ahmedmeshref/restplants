import json
import unittest

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

    def tearDown(self):
        """Executed after reach test to close any opened thing"""
        pass

    def test_get_home(self):
        """Test status code of get plant"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_plants(self):
        response = self.client.get("/plants?page=1")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['plants']))
        self.assertTrue(data['number_of_plants'])
        self.assertTrue(data['current_page'])

    def test_404_get_plants_from_notfound_page(self):
        response = self.client.get("/plants?page=1000")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_create_plant(self):
        response = self.client.post("/plants",
                                    json={'name': 'Snake Plant', 'scientific_name': 'Snake', 'is_poisonous': True,
                                          'primary_color': 'red'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["number_of_plants"])
        self.assertTrue(len(data["plants"]))
        self.assertTrue(data["new_plant_id"])
        self.assertTrue(data["current_page_number"])

    def test_400_bad_request_on_empty_body(self):
        response = self.client.post("/plants")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_405_if_plant_creation_not_allowed(self):
        response = self.client.post("/plants/5", json={'name': 'Snake Plant'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Not Allowed')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
