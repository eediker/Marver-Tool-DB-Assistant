# This is the file that we use for the purpose of mongodb administraiton.
import json
from pymongo import MongoClient
from pandas import DataFrame

class Mongo_Client:

    def __init__(self,connection_string="mongodb://localhost:27017",db_name = "Marver") -> None:
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db["Marver"]


    def change_collection(self,collection_name):
        self.collection = self.db[collection_name]


    def change_db(self,db_name):
        self.db = self.client[db_name]


    def list_database(self):
        return self.client.list_database_names()


    def list_collections(self):
        return self.db.list_collection_names()


    def insert_document(self,data:dict):
        collection = self.db[self.collection_name]
        return collection.insert_one(data).inserted_id

    
    def insert_documents(self,data):
        self.collection.insert_many(data)
        

    def insert_documents_from_txt(self,data_path):
        docs = []
        with open(data_path,"r") as file:
            for line in file:
                docs.append(json.loads(line))
        self.insert_documents(docs)


    def find_documents(self,cretaria:dict = {}):
        docs = self.collection.find(cretaria)
        return docs


    def get_document_by_id(self,document_id):
        from bson.objectid import ObjectId
        _id = ObjectId(document_id)
        return self.collection.find_one({"_id":_id})
    
    def get_document(self):
        return self.collection.find_one()


    def project_columns(self,keys = [],cretaria:dict = {}):
        columns = {}
        columns["_id"] = 0
        for key in keys:
            columns[key] = 1
        docs = self.collection.find(cretaria,columns)
        df = DataFrame(data=docs)
        return df


    def specify_range(self,min,max,name:str):
        dict = {
            "$and":[
                {name: {"$gte":min}},
                {name: {"$lte":max}}
            ],
        }
        return dict

    
    def rename_document_property(self,document_id,ex:str,new:str):
        from bson.objectid import ObjectId
        _id = ObjectId(document_id)

        update = {
            "$rename":{
                ex:new
            }
        }
        self.collection.update_one({"_id":_id},update)


    def set_field(self,document_id,key,value):
        from bson.objectid import ObjectId
        _id = ObjectId(document_id)
        update = {
            "$set":{
                key: value
            }
        }
        self.collection.update_one({"_id":_id},update)


    def remove_keys(self,document_id,key):
        from bson.objectid import ObjectId
        _id = ObjectId(document_id)
        update = {
            "$unset":{
                key:""
            }
        }
        self.collection.update_one({"_id":_id},update)
    

    def update_number(self,document_id,key:str,value:int):
        from bson.objectid import ObjectId
        _id = ObjectId(document_id)
        update = {
            "$inc":{
                key: value
            }
        }
        self.collection.update_one({"_id":_id},update)
    

    def delete_doc_by_id(self,document_id):
        from bson.objectid import ObjectId
        _id = ObjectId(document_id)
        self.collection.delete_many({"_id":_id})


    def delete_docs_by_cretaria(self,cretaria):
        self.collection.delete_many(cretaria)

    def return_keys(self):
        keys = []
        for key in self.get_document().keys():
            keys.append(key)
        return keys
