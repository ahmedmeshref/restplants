import json
import unittest

from flaskr import create_app
from flaskr.models import setup_db, db, Plant
from flaskr.main.utils import plants_per_page


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
        response = self.client.get("/plants")
        data = json.loads(response.data)
        plants = db.session.query(Plant).count()
        if plants:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(len(data['plants']))
            self.assertTrue(data['number_of_plants'])
            self.assertTrue(data['current_page'])

    def test_404_get_plants_from_not_existing_page(self):
        # get total existing plants
        total_pages = db.session.query(Plant).count() // plants_per_page
        response = self.client.get(f"/plants?page={total_pages+100}")
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

    def test_400_create_plant_with_empty_body(self):
        response = self.client.post("/plants")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_405_plant_creation_not_allowed(self):
        response = self.client.post("/plants/5", json={'name': 'Snake Plant'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Not Allowed')

    def test_update_plant(self):
        existing_plant = db.session.query(Plant).first()
        if existing_plant:
            id = existing_plant.id
            response = self.client.patch(f"/plants/{id}", json={'primary_color': 'Red'})
            data = json.loads(response.data)

            get_plant = self.client.get(f"/plants/{id}")
            updated_plant_data = json.loads(get_plant.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(get_plant.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(data["id"], id)
            self.assertEqual(updated_plant_data['plant']['primary_color'], 'Red')

    def test_400_update_plant_with_empty_body(self):
        existing_plant = db.session.query(Plant).first()
        if existing_plant:
            response = self.client.patch(f"/plants/{existing_plant.id}")
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data["success"], False)
            self.assertEqual(data['message'], 'Bad Request')

    def test_405_update_plant_using_not_allowed_route(self):
        response = self.client.patch("/plants", json={'name': 'Snake Plant'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Not Allowed')

    def test_delete_plant(self):
        existing_plant = db.session.query(Plant).first()
        if existing_plant:
            id = existing_plant.id
            response = self.client.delete(f"/plants/{id}")
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(data["deleted_plant_id"], id)

    def test_404_delete_non_existing_plant(self):
        response = self.client.delete("/plants/0")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Resource Not Found')

    def test_search_resource_by_name(self):
        response = self.client.get("/plants/search/ahmed")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        if data:
            self.assertTrue(data['no_plants'])
            self.assertTrue(data['current_page'])
            self.assertTrue(len(data['plants']))
        else:
            self.assertEqual(data['no_plants'], 0)
            self.assertEqual(data['current_page'], 1)
            self.assertEqual(data['plants'], [])

    def test_404_search_without_name(self):
        response = self.client.get("/plants/search/")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
