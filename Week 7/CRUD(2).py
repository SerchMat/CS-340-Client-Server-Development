from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json import dumps

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to        
        self.client = MongoClient('localhost:48315',
                                  username="myUserAdmin",
                                  password="Mateos11",
                                  authSource='AAC')
        self.database = self.client['AAC']

    #Create Metod
    def create(self, data):
        if data is not None:            
            result = self.database.animals.insert(data) # data should be added into dictionary  
            if inster != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
       
    #Read Method
    def read(self, criteria=None):
        if criteria is not None:
            data = seld.database.animals.find(criteria,{"_id": False}) #Data should read in the dictionary
            for documents in data:
                print(document)
        else:
            data = self.database.animals.find({},{"_id":False})
        return data
                
    #Update Method
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {'$set':{updateData}}) #Data should be avaible to update  
            return result.raw_result
        else:
            return "{}"
        
        #Return the dataset else error
        return result.raw_result
            
    #Delete Method
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)#Data will delet from the dictionary
        else:
            return "{}"
        
         #Return the dataset else error
        return result.raw_result

