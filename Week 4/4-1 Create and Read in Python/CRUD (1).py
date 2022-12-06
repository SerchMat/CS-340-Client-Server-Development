from pymongo import MongoClient
from bson.objectid import ObjectId

#Sergio Mateos
#CS 360
#Southern New Hampshire University

class AnimalShelter(object):
    """ """
    def __init__(self, username, password):
        # init to connect to mongodb  without authentication
        #self.client = MongoClient('mongodb://localhost:54011')
        # init to connect to mongodb  with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:48315'%("aacuser", "Mateos1")
        self.database = self.client['AAC']
                               
    # Create Method
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # Data should be a dictionary
            print("animal added succesfully")
            return True
        else:
            raise Exception("Nothing to save due to parameter being empty")
    
    # Read Method
    def read(self, data):
        return self.database.animals.find_one(data) # Returns a single document as a python dictionary

