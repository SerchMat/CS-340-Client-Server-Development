from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

#Sergio Mateos
#CS 340 Client/Server Development
#Southern New Hampshire University

class AnimalShelter(object):
    
    #Property variables
    records_updated = 0 #keep a record of the records updated in an operation; CYA
    records_matched = 0 #keep a record of the records macthed in an operation; CYA
    records_deleted = 0 #keep a record of the records deleted in an operation; CYA

    #Constructor to init the mongodb
    def __init__(self, _password, _username = 'aacuser'):
        
        userName = urllib.parse.quote_plus(_username)
        password = urllib.parse.quote_plus(_password)
        
        self.client = MongoClient('mongodb://%s:%s@localhost:48315/?authSource=AAC' % (userName, password))
        self.dataBase = self.client['AAC']
       
    #Mehtod to create a record
    def createRecord(self, data):
        if data:
            _insertValid = self.dataBase.animals.insert_one(data)
            #check the status of the inserted value 
            return True if _insertValid.acknowledged else False
	
        else:
            raise Exception("No document to save. Data is empty.")
    
    #GetRecord for certain criteria
    def getRecordId(self, postId):
        _data = self.dataBase.find_one({'_id': ObjectId(postId)})
                                  
        return _data
    
    #Get records with criteria
    def getRecordCriteria(self, criteria):
        if criteria:
            _data = self.dataBase.animals.find(criteria, {'_id' : 0})
                                 
        else:
            _data = self.dataBase.animals.find({},{'_id' : 0})
                                  
        return _data
    
    #Update a record
    def updateRecord(self, query, newValue):
        if not query:
            raise Exception("No search criteria is present.")
        elif not newValue:
            raise Exception("No update value is present.")
        else:
            _updateValid = self.dataBase.animals.update_many(query, {"$set": newValue})
            self.records_updated = _updateValid.modified_count
            self.records_matched = _updateValid.matched_count

            return True if _updateValid.modified_count > 0 else False
    
    #Delete a record
    def deleteRecord(self, query):
        if not query:
            raise Exception("No search criteria is present.")
        
        else:
            _deleteValid = self.dataBase.animals.delete_many(query)
            self.records_deleted = _deleteValid.deleted_count

            return True if _deleteValid.deleted_count > 0 else False                   
