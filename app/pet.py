import requests
import json


class Pet:

    def __init__(self):
        self.path = 'http://petstore.swagger.io/v2/pet/'
        self.response = None
        self.data = {}
        self.headers = {'accept': 'application/json'}

    def __getattr__(self, name):
        return self.data[name]

    @staticmethod
    def create(body):
        pet = Pet()
        pet.headers['content-type'] = 'application/json'
        pet.response = requests.post('%s' % pet.path,
                                     data=json.dumps(body), headers=pet.headers)
        pet.data = pet.response.json()
        return pet

    @staticmethod
    def update(body):
        pet = Pet()
        pet.headers['content-type'] = 'application/json'
        pet.response = requests.put('%s' % pet.path,
                                    data=json.dumps(body), headers=pet.headers)
        pet.data = pet.response.json()
        return pet

    @staticmethod
    def find(id_pet):
        if not isinstance(id_pet, int):
            raise ValueError

        pet = Pet()
        pet.response = requests.get('%s%d' % (pet.path, id_pet))
        pet.data = pet.response.json()
        return pet

    @staticmethod
    def delete(id_pet):
        if not isinstance(id_pet, int):
            raise ValueError

        pet = Pet()
        pet.response = requests.delete('%s%d' % (pet.path, id_pet))
        return pet
