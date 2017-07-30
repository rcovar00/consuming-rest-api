import sys
sys.path.append('./')
from app.pet import Pet
from unittest import TestCase


class PetTest(TestCase):

    def test_create(self):
        pet_data = {"id": 2000, "category": {"id": 0, "name": "Beagle"}, "name": "Snoopy", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}], "status": "available"}
        pet = Pet.create(pet_data)
        self.assertEqual(200, pet.response.status_code)
        self.assertEqual('Snoopy', pet.name)
        self.assertEqual('Beagle', pet.category['name'])

    def test_update(self):
        pet_data = {"id": 2000, "category": {"id": 0, "name": "Labrador"}, "name": "Max", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}], "status": "available"}
        pet = Pet.update(pet_data)
        self.assertEqual(200, pet.response.status_code)
        self.assertEqual('Max', pet.name)
        self.assertEqual('Labrador', pet.category['name'])

    def test_find(self):
        pet = Pet.find(2000)
        self.assertEqual(200, pet.response.status_code)
        Pet.delete(2000)

    def test_delete(self):
        pet_data = {"id": 3000}
        Pet.create(pet_data)
        pet = Pet.delete(3000)
        self.assertEqual(200, pet.response.status_code)


class PetBadInPutTest(TestCase):

    def test_create(self):
        pet_data = {"id": "ASA8980DSF"}
        pet = Pet.create(pet_data)
        self.assertNotEqual(200, pet.response.status_code)

    def test_update(self):
        pet_data = {"id": "21A"}
        pet = Pet.update(pet_data)
        self.assertNotEqual(200, pet.response.status_code)

    def test_find(self):
        self.assertRaises(ValueError, Pet.find, 'SF')
        self.assertRaises(ValueError, Pet.find, 345.4)

    def test_delete(self):
        self.assertRaises(ValueError, Pet.delete, 'a')
        self.assertRaises(ValueError, Pet.delete, 5.56)
